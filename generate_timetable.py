import pandas as pd
from pathlib import Path
from timetable.templates import (
    template,
    oral_session,
    opening_session,
    closing_session,
    poster_session,
    tutorial_session,
    panel_session,
    break_template,
    lunch_template,
    template_list_of_posters,
)
from timetable.timeslot import session_to_time


def main():
    columns_to_keep = [
        "Abstract ID",
        "Email Address",
        "First name",
        "Last name",
        "Affiliation",
        "Title",
        "Abstract",
        "List of authors and affiliations",
        "Link to open-source software repository (if applicable)",
        "Abstract decision",
        "Slot",
        "Session",
    ]

    df = pd.read_csv("abstracts.csv", usecols=columns_to_keep)

    # remove all linebreaks that would cause the markdown to break
    df = df.replace(r"\n", " ", regex=True)

    df_plenary = df[df["Abstract decision"] == "Oral"].copy()
    df_oral = df[df["Abstract decision"] == "Oral"].copy()
    df_poster = df[df["Abstract decision"] == "Poster"].copy()
    df_tutorial = df[df["Abstract decision"] == "Tutorial"].copy()

    # sort orals
    df_oral.loc[:, "slot_number"] = df_oral["Slot"].str.extract(r"(\d+)").astype(int)

    # Group by day and session
    grouped = df_oral.sort_values(by=["Session", "slot_number"]).groupby("Session", sort=True)

    # sort by time
    grouped = sorted(grouped, key=lambda x: session_to_time(x[0]).start)

    # Create a table for each group
    # Store tuples of (time_slot, formatted_session) for later sorting
    sessions_day_1 = []
    sessions_day_2 = []
    for session, group in grouped:
        data = []
        time_slot = session_to_time(session)

        for idx, (_, item) in enumerate(group.iterrows(), start=1):
            # filename is last-name of author + first word of title
            last_name = item["Last name"]
            first_word_title = item["Title"].replace("-", " ").split()[0]
            filename = f"{last_name}-{first_word_title}.md".lower()

            # remove invalid characters
            filename = filename.replace(" ", "").replace("/", "").replace(":", "").replace(",", "")

            title = f"[{item['Title']}](abstract_files/{filename})"
            presenter = f"{item['First name']} {item['Last name']}"

            # breakpoint()
            talk_id = item["Slot"]

            institution_of_first_author = item["Affiliation"]

            data.append(
                {
                    "ID": talk_id,
                    "Title": title,
                    "Presenter": presenter,
                    "Institution": institution_of_first_author,
                }
            )

        session_id = session.replace("session_oral_", "")

        df_table = pd.DataFrame(data)
        table = df_table.to_markdown(index=False)
        formatted_session = oral_session.format(
            session_id=session_id,
            time_slot=time_slot,
            room=time_slot.room,
            chair=time_slot.chair,
            num_presentations=time_slot.num_presentations,
            table=table,
        )
        if time_slot.day == "Wednesday":
            sessions_day_1.append((time_slot, formatted_session))
        else:
            sessions_day_2.append((time_slot, formatted_session))

    # sort tutorials
    df_tutorial.loc[:, "slot_number"] = df_oral["Slot"].str.extract(r"(\d+)").astype(int)

    # Group by day and session
    grouped_tutorials = df_tutorial.sort_values(by=["Session", "slot_number"]).groupby("Session", sort=True)

    # sort by time
    grouped_tutorials = sorted(grouped_tutorials, key=lambda x: session_to_time(x[0]).start)

    # Create a table for each group
    for session, group in grouped_tutorials:
        data = []
        time_slot = session_to_time(session)

        for idx, (_, item) in enumerate(group.iterrows(), start=1):
            # filename is last-name of author + first word of title
            last_name = item["Last name"]
            first_word_title = item["Title"].replace("-", " ").split()[0]
            filename = f"{last_name}-{first_word_title}.md".lower()

            # remove invalid characters
            filename = filename.replace(" ", "").replace("/", "").replace(":", "").replace(",", "")

            title = f"[{item['Title']}]({filename})"
            presenter = f"{item['First name']} {item['Last name']}"

            # breakpoint()
            talk_id = item["Slot"]

            institution_of_first_author = item["Affiliation"]

            data.append(
                {
                    "ID": talk_id,
                    "Title": title,
                    "Presenter": presenter,
                    "Institution": institution_of_first_author,
                }
            )

        # remove the session_id from the session string

        session_id = session.replace("session_tut_", "")
        df_table = pd.DataFrame(data)
        table = df_table.to_markdown(index=False)
        formatted_session = tutorial_session.format(
            session_id=session_id,
            time_slot=time_slot,
            room=time_slot.room,
            num_presentations=time_slot.num_presentations,
            table=table,
        )
        if time_slot.day == "Wednesday":
            sessions_day_1.append((time_slot, formatted_session))
        else:
            sessions_day_2.append((time_slot, formatted_session))

    # create item for opening session
    S_opening_time_slot = session_to_time("session_welcome")
    opening_session_str = opening_session.format(
        time_slot=S_opening_time_slot,
        room=S_opening_time_slot.room,
    )
    sessions_day_1.append((S_opening_time_slot, opening_session_str))

    # create item for closing session
    S_closing_time_slot = session_to_time("session_closing")
    closing_session_str = closing_session.format(
        time_slot=S_closing_time_slot,
        room=S_closing_time_slot.room,
    )
    sessions_day_2.append((S_closing_time_slot, closing_session_str))

    # create item for poster session
    # S_poster_1_time_slot = session_to_time("session_poster_1")
    # S_poster_2_time_slot = session_to_time("session_poster_2")
    # poster_session_str = poster_session.format(
    #     time_slot=S_poster_1_time_slot,
    #     room_1=S_poster_1_time_slot.room,
    #     room_2=S_poster_2_time_slot.room,
    # )
    # tables.insert(4, poster_session_str)

    # # create item for demos session
    # S_demos_time_slot = session_to_time("S_demos")

    # data = []
    # for index, (_, item) in enumerate(df_demo.iterrows(), start=1):
    #     # filename is last-name of author + first word of title
    #     last_name = item["List of authors and affiliation"].split(",")[0].split()[0]
    #     first_word_title = item["Title"].replace("-", " ").split()[0]
    #     filename = f"{last_name}-{first_word_title}.md".lower()

    #     # remove invalid characters
    #     filename = filename.replace(" ", "").replace("/", "").replace(":", "").replace(",", "")

    #     title = f"[{item['Title']}](abstracts/{filename})"
    #     presenter = item["Name"]

    #     institution_of_first_author = ""
    #     try:
    #         author_affiliation_list = item["List of authors and affiliation"].split(";")
    #         parts = author_affiliation_list[0].strip().split(",", 1)  # Split only at the first comma
    #         institution_of_first_author = parts[1].strip()
    #     except:
    #         pass
    #     data.append(
    #         {
    #             "ID": f"T{index}",
    #             "Title": title,
    #             "Presenter": presenter,
    #             "Institution": institution_of_first_author,
    #         }
    #     )
    # df_table = pd.DataFrame(data)
    # table = df_table.to_markdown(index=False)
    # demo_session_str = demo_session.format(
    #     time_slot=S_demos_time_slot,
    #     room=S_demos_time_slot.room,
    #     demos=table,
    # )
    # tables.insert(5, demo_session_str)

    # create item for panel session
    S_panel_time_slot = session_to_time("session_panel")
    presenters = [
        "[Paul Wilson](bios/wilson.md)",
        "[Martin Yagi](bios/yagi.md)",
        "[David Bernhodlt](bios/bernholdt.md)",
        "[Matt Vernacchia](bios/vernacchia.md)",
        "[Aiden Fowler](bios/fowler.md)",
    ]
    affiliations = [
        "[University of Wisconsin-Madison](https://www.wisc.edu/)",
        "[First Light Fusion](https://firstlightfusion.com/)",
        "[ORNL](https://www.ornl.gov/)",
        "[CFS](https://cfs.energy/)",
        "[MIT](https://www.mit.edu/)",
    ]
    panel_data = []
    for presenter, affiliation in zip(presenters, affiliations):
        panel_data.append({"Presenter": presenter, "Affiliation": affiliation})

    panel_df_table = pd.DataFrame(panel_data)
    panel_table = panel_df_table.to_markdown(index=False)
    panel_session_str = panel_session.format(
        time_slot=S_panel_time_slot,
        room=S_panel_time_slot.room,
        chair=S_panel_time_slot.chair,
        table=panel_table,
    )
    sessions_day_1.append((S_panel_time_slot, panel_session_str))

    # # create items for breaks
    # break_1_time_slot = TimeSlot(
    #     start=datetime(2025, 3, 18, 8, 10, tzinfo=edt),
    #     end=datetime(2025, 3, 18, 8, 30, tzinfo=edt),
    # )
    # break_2_time_slot = TimeSlot(
    #     start=datetime(2025, 3, 18, 13, 50, tzinfo=edt),
    #     end=datetime(2025, 3, 18, 14, 10, tzinfo=edt),
    # )
    # tables.insert(2, break_template.format(time_slot=break_1_time_slot))
    # tables.insert(11, break_template.format(time_slot=break_2_time_slot))

    # # create item for lunch
    # lunch_time_slot = TimeSlot(
    #     start=datetime(2025, 3, 18, 11, 50, tzinfo=edt),
    #     end=datetime(2025, 3, 18, 12, 50, tzinfo=edt),
    # )
    # tables.insert(9, lunch_template.format(time_slot=lunch_time_slot))

    # Handle posters

    # Separate into two groups based on 'slot_id'
    df_poster_1 = df_poster[df_poster["Slot"] == "session_poster_1"]
    df_poster_2 = df_poster[df_poster["Slot"] == "session_poster_2"]

    # sort by abstract_id
    df_poster_1 = df_poster_1.sort_values(by=["Abstract ID"])
    df_poster_2 = df_poster_2.sort_values(by=["Abstract ID"])

    def create_markdown_table(df_poster):
        data = []

        for _, item in df_poster.iterrows():
            # Extract last name and first word of title
            last_name = item["Last name"]
            first_word_title = item["Title"].replace("-", " ").split()[0]
            filename = f"{last_name}-{first_word_title}.md".lower()

            # Remove invalid characters
            filename = filename.replace(" ", "").replace("/", "").replace(":", "").replace(",", "")

            title = f"[{item['Title']}](abstracts/{filename})"
            presenter = f"{item['First name']} {item['Last name']}"
            institution_of_first_author = item["Affiliation"]
            poster_id = item["Abstract ID"]
            data.append(
                {
                    "ID": f"{poster_id}",  # Assign unique ID
                    "Title": title,
                    "Presenter": presenter,
                    "Affilaition": institution_of_first_author,
                }
            )

        df_posters_md = pd.DataFrame(data)
        posters_md = df_posters_md.to_markdown(index=False)

        return posters_md

    # Generate markdown tables
    posters_md_1 = create_markdown_table(df_poster_1)
    posters_md_2 = create_markdown_table(df_poster_2)

    # Sort sessions by time slot
    sessions_day_1.sort(key=lambda x: x[0].start)
    sessions_day_2.sort(key=lambda x: x[0].start)

    # Extract just the formatted session strings
    tables_day_1 = [session[1] for session in sessions_day_1]
    tables_day_2 = [session[1] for session in sessions_day_2]

    # (Path("book") / "programme.md").write_text(
    (Path("program.md")).write_text(
        template.format(
            tables_day_1="\n\n".join(tables_day_1),
            tables_day_2="\n\n".join(tables_day_2),
        )
    )
    (Path("list_of_posters.md")).write_text(
        template_list_of_posters.format(
            poster_session_1_time_slot=session_to_time("session_poster_1"),
            poster_session_2_time_slot=session_to_time("session_poster_2"),
            poster_session_1=posters_md_1,
            poster_session_2=posters_md_2,
        )
    )


if __name__ == "__main__":
    main()
