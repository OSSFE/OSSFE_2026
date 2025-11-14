"""
TimeSlot configuration and management for conference scheduling.

Provides a flexible, data-driven approach to defining conference sessions.
"""

from datetime import datetime, timedelta, timezone
from typing import Dict, List, Optional

# Conference timezone
TZ = timezone(timedelta(hours=+1), name="cet")

# Session duration configurations (in seconds)
DURATIONS = {
    "Plenary": 30 * 60,
    "Oral": 20 * 60,
    "Tutorial": 30 * 60,
}


class TimeSlot:
    """Represents a conference time slot with scheduling information."""

    def __init__(
        self,
        start: datetime,
        end: datetime,
        room: Optional[str] = None,
        session_type: Optional[str] = None,
        chair: Optional[str] = None,
    ):
        self.start = start
        self.end = end
        self.room = room
        self.type = session_type
        self.chair = chair

    @property
    def num_presentations(self) -> int:
        """Calculate number of presentations based on duration and type."""
        if self.type not in DURATIONS:
            return 1
        duration = self.end - self.start
        return int(duration.total_seconds() / DURATIONS[self.type])

    @property
    def day(self) -> str:
        """Get formatted day name from date."""
        return self.start.strftime("%A")

    @property
    def date(self) -> str:
        """Get formatted date string."""
        return self.start.strftime("%Y-%m-%d")

    def __str__(self) -> str:
        """Format time slot as 'HH:MM - HH:MM'."""
        return f"{self.start.strftime('%H:%M')} - {self.end.strftime('%H:%M')}"


# Session schedule configuration - data-driven approach
# This makes it easy to modify the schedule without changing code
SESSION_SCHEDULE: Dict[str, Dict] = {
    # Special sessions
    "session_welcome": {
        "start": (2026, 3, 10, 8, 40),
        "end": (2026, 3, 10, 9, 0),
        "room": "Auditorium",
        "type": "Opening",
    },
    "session_closing": {
        "start": (2026, 3, 11, 17, 10),
        "end": (2026, 3, 11, 17, 20),
        "room": "Auditorium",
        "type": "Closing",
    },
    "session_panel": {
        "start": (2026, 3, 10, 13, 40),
        "end": (2026, 3, 10, 14, 40),
        "room": "Auditorium",
        "chair": "TBC, Affiliation",
    },
    "session_proxima_tour": {
        "start": (2026, 3, 12, 9, 30),
        "end": (2026, 3, 12, 10, 0),
    },
    "session_hackathon": {
        "start": (2026, 3, 12, 10, 20),
        "end": (2026, 3, 12, 12, 20),
    },
    "session_lunch_proxima": {
        "start": (2026, 3, 12, 12, 20),
        "end": (2026, 3, 12, 13, 40),
    },
    # Poster sessions
    "session_poster_1": {
        "start": (2026, 3, 10, 11, 20),
        "end": (2026, 3, 10, 12, 20),
        "room": "Foyer",
    },
    "session_poster_2": {
        "start": (2026, 3, 11, 11, 20),
        "end": (2026, 3, 11, 12, 20),
        "room": "Foyer",
    },
    # Plenary sessions
    **{
        f"session_plenary_{i}": {
            "start": start,
            "end": end,
            "room": "Auditorium",
            "type": "Plenary",
            "chair": "TBC, Affiliation",
        }
        for i, (start, end) in enumerate(
            [
                ((2026, 3, 10, 9, 0), (2026, 3, 10, 10, 0)),
                ((2026, 3, 11, 9, 0), (2026, 3, 10, 10, 0)),
                ((2026, 3, 11, 13, 40), (2026, 3, 10, 14, 40)),
            ],
            start=1,
        )
    },
    # Tutorial sessions
    **{
        f"session_tut_{i}": {
            "start": start,
            "end": end,
            "room": "Seminar room 1",
            "type": "Tutorial",
            "chair": "TBC, Affiliation",
        }
        for i, (start, end) in enumerate(
            [
                ((2026, 3, 10, 10, 20), (2026, 3, 10, 11, 20)),
                ((2026, 3, 10, 14, 40), (2026, 3, 10, 15, 40)),
                ((2026, 3, 10, 16, 0), (2026, 3, 10, 17, 0)),
                ((2026, 3, 11, 10, 20), (2026, 3, 11, 11, 20)),
                ((2026, 3, 11, 14, 40), (2026, 3, 11, 15, 40)),
                ((2026, 3, 11, 16, 0), (2026, 3, 11, 17, 0)),
            ],
            start=1,
        )
    },
    # Oral sessions
    **{
        f"session_oral_{letter}": {
            "start": start,
            "end": end,
            "room": room,
            "type": "Oral",
            "chair": "TBC, Affiliation",
        }
        for letter, (start, end, room) in zip(
            "ABCDEFGHIJKL",
            [
                ((2026, 3, 10, 10, 20), (2026, 3, 10, 11, 20), "Auditorium"),
                ((2026, 3, 10, 10, 20), (2026, 3, 10, 11, 20), "Projektraum"),
                ((2026, 3, 10, 14, 40), (2026, 3, 10, 15, 40), "Auditorium"),
                ((2026, 3, 10, 14, 40), (2026, 3, 10, 15, 40), "Projektraum"),
                ((2026, 3, 10, 16, 0), (2026, 3, 10, 17, 0), "Auditorium"),
                ((2026, 3, 10, 16, 0), (2026, 3, 10, 17, 0), "Projektraum"),
                ((2026, 3, 11, 10, 20), (2026, 3, 11, 11, 20), "Auditorium"),
                ((2026, 3, 11, 10, 20), (2026, 3, 11, 11, 20), "Projektraum"),
                ((2026, 3, 11, 14, 40), (2026, 3, 11, 15, 40), "Auditorium"),
                ((2026, 3, 11, 14, 40), (2026, 3, 11, 15, 40), "Projektraum"),
                ((2026, 3, 11, 16, 0), (2026, 3, 11, 17, 0), "Auditorium"),
                ((2026, 3, 11, 16, 0), (2026, 3, 11, 17, 0), "Projektraum"),
            ],
        )
    },
}

# Breaks schedule
BREAKS: List[tuple] = [
    ((2026, 3, 10, 10, 0), (2026, 3, 10, 10, 20)),
    ((2026, 3, 10, 15, 40), (2026, 3, 10, 16, 0)),
    ((2026, 3, 11, 10, 0), (2026, 3, 11, 10, 20)),
    ((2026, 3, 11, 15, 40), (2026, 3, 11, 16, 0)),
    ((2026, 3, 12, 10, 0), (2026, 3, 12, 10, 20)),
]

# Lunches schedule
LUNCHES: List[tuple] = [
    ((2026, 3, 10, 12, 20), (2026, 3, 10, 13, 40)),
    ((2026, 3, 11, 12, 20), (2026, 3, 11, 13, 40)),
]


def session_to_time(session_id: str) -> TimeSlot:
    """
    Convert session ID to TimeSlot object.

    Args:
        session_id: Session identifier (e.g., "session_oral_A")

    Returns:
        TimeSlot object with scheduling information

    Raises:
        ValueError: If session_id is not found in schedule
    """
    if session_id not in SESSION_SCHEDULE:
        raise ValueError(f"Unknown session: {session_id}")

    config = SESSION_SCHEDULE[session_id]
    return TimeSlot(
        start=datetime(*config["start"], tzinfo=TZ),
        end=datetime(*config["end"], tzinfo=TZ),
        room=config.get("room"),
        session_type=config.get("type"),
        chair=config.get("chair"),
    )


def get_breaks() -> List[TimeSlot]:
    """Get all break time slots."""
    return [TimeSlot(datetime(*start, tzinfo=TZ), datetime(*end, tzinfo=TZ)) for start, end in BREAKS]


def get_lunches() -> List[TimeSlot]:
    """Get all lunch time slots."""
    return [TimeSlot(datetime(*start, tzinfo=TZ), datetime(*end, tzinfo=TZ)) for start, end in LUNCHES]


# Maintain backwards compatibility
breaks = get_breaks()
lunches = get_lunches()
