"""
Generate conference timetable from abstracts CSV file.

Highly configurable script that works for conferences of any length.
"""

from collections import defaultdict
from pathlib import Path
from typing import Dict, List, Tuple

import pandas as pd

from timetable.templates import (
    break_template,
    closing_session,
    lunch_template,
    opening_session,
    oral_session,
    panel_session,
    plenary_session,
    poster_session,
    template,
    template_list_of_posters,
    tutorial_session,
)
from timetable.timeslot import TimeSlot, get_breaks, get_lunches, session_to_time

# Configuration - modify these for different conferences
SESSION_CONFIGS = {
    "Oral": {"template": oral_session, "prefix": "session_oral_"},
    "Plenary": {"template": plenary_session, "prefix": "session_plenary_"},
    "Tutorial": {"template": tutorial_session, "prefix": "session_tut_"},
}


def generate_filename(last_name: str, title: str) -> str:
    """Generate standardized filename: lastname-firstword.md"""
    first_word = title.replace("-", " ").split()[0].lower()
    return f"{last_name.lower()}-{first_word}.md".replace(" ", "").replace("/", "").replace(":", "").replace(",", "")


def create_presentation_row(row: pd.Series) -> dict:
    """Create a single presentation data row."""
    filename = generate_filename(row["Last name"], row["Title"])
    return {
        "ID": row["Slot"],
        "Title": f"[{row['Title']}](abstract_files/{filename})",
        "Presenter": f"{row['First name']} {row['Last name']}",
        "Institution": row["Affiliation"],
    }


def process_session_group(session_id: str, group: pd.DataFrame, template: str, prefix: str) -> Tuple[TimeSlot, str]:
    """Process a session group into formatted markdown."""
    time_slot = session_to_time(session_id)
    table = pd.DataFrame([create_presentation_row(row) for _, row in group.iterrows()]).to_markdown(index=False)

    return (
        time_slot,
        template.format(
            session_id=session_id.replace(prefix, ""),
            time_slot=time_slot,
            room=time_slot.room,
            chair=time_slot.chair,
            num_presentations=time_slot.num_presentations,
            table=table,
        ),
    )


def process_presentation_type(df: pd.DataFrame, decision_type: str) -> List[Tuple[TimeSlot, str]]:
    """Process all sessions of a given presentation type."""
    filtered = df[df["Abstract decision"] == decision_type].copy()
    if filtered.empty:
        return []

    filtered["slot_number"] = filtered["Slot"].str.extract(r"(\d+)").astype(int)
    grouped = filtered.sort_values(by=["Session", "slot_number"]).groupby("Session", sort=True)

    config = SESSION_CONFIGS[decision_type]
    return [
        process_session_group(session_id, group, config["template"], config["prefix"])
        for session_id, group in sorted(grouped, key=lambda x: session_to_time(x[0]).start)
    ]


def create_special_sessions() -> List[Tuple[TimeSlot, str]]:
    """Create all special sessions (opening, closing, poster, panel)."""
    sessions = []

    # Opening and closing
    for session_id, tmpl in [("session_welcome", opening_session), ("session_closing", closing_session)]:
        slot = session_to_time(session_id)
        sessions.append((slot, tmpl.format(time_slot=slot, room=slot.room)))

    # Posters
    for session_id in ["session_poster_1", "session_poster_2"]:
        slot = session_to_time(session_id)
        sessions.append((slot, poster_session.format(time_slot=slot)))

    # Panel
    panel_slot = session_to_time("session_panel")
    panel_data = [{"Presenter": "[TBC](bios/last_name.md)", "Affiliation": "TBC"}] * 4
    sessions.append(
        (
            panel_slot,
            panel_session.format(
                time_slot=panel_slot,
                room=panel_slot.room,
                chair=panel_slot.chair,
                table=pd.DataFrame(panel_data).to_markdown(index=False),
            ),
        )
    )

    return sessions


def create_poster_table(df: pd.DataFrame, session_id: str) -> str:
    """Create markdown table for poster session."""
    filtered = df[(df["Abstract decision"] == "Poster") & (df["Slot"] == session_id)].sort_values(by=["Abstract ID"])

    data = [
        {
            "ID": str(row["Abstract ID"]),
            "Title": f"[{row['Title']}](abstract_files/{generate_filename(row['Last name'], row['Title'])})",
            "Presenter": f"{row['First name']} {row['Last name']}",
            "Affiliation": row["Affiliation"],
        }
        for _, row in filtered.iterrows()
    ]

    return pd.DataFrame(data).to_markdown(index=False)


def organize_by_day(sessions: List[Tuple[TimeSlot, str]]) -> Dict[str, List[str]]:
    """Organize and sort sessions by day."""
    by_day = defaultdict(list)
    for slot, content in sorted(sessions, key=lambda x: x[0].start):
        by_day[slot.day].append(content)
    return dict(by_day)


def main() -> None:
    """Generate conference timetable files."""
    # Load and clean data
    df = pd.read_csv("abstracts.csv").replace(r"\n", " ", regex=True)

    # Collect all sessions
    all_sessions = (
        [session for ptype in SESSION_CONFIGS for session in process_presentation_type(df, ptype)]
        + create_special_sessions()
        + [(slot, break_template.format(time_slot=slot)) for slot in get_breaks()]
        + [(slot, lunch_template.format(time_slot=slot)) for slot in get_lunches()]
    )

    # Organize by day
    by_day = organize_by_day(all_sessions)
    days = sorted(by_day.keys())  # Automatically handles any number of days

    # Write program file (handles 2 days for now, can be extended)
    Path("program.md").write_text(
        template.format(
            tables_day_1="\n\n".join(by_day.get(days[0], [])),
            tables_day_2="\n\n".join(by_day.get(days[1], [])) if len(days) > 1 else "",
        )
    )

    # Write poster list
    Path("list_of_posters.md").write_text(
        template_list_of_posters.format(
            poster_session_1_time_slot=session_to_time("session_poster_1"),
            poster_session_2_time_slot=session_to_time("session_poster_2"),
            poster_session_1=create_poster_table(df, "session_poster_1"),
            poster_session_2=create_poster_table(df, "session_poster_2"),
        )
    )


if __name__ == "__main__":
    main()
