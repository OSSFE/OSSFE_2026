from datetime import datetime, timezone, timedelta
from typing import NamedTuple
from enum import IntEnum, auto

PLENARY_TALK_DURATION_MIN = 30
PLENARY_TALK_DURATION_SEC = PLENARY_TALK_DURATION_MIN * 60

TALK_DURATION_MIN = 20
TALK_DURATION_SEC = TALK_DURATION_MIN * 60

type_to_duration = {
    "Plenary": PLENARY_TALK_DURATION_SEC,
    "Oral": TALK_DURATION_SEC,
    "Tutorial": PLENARY_TALK_DURATION_SEC,
}

cet = timezone(timedelta(hours=+1), name="cet")  # Central European Time (UTC+1)


class TimeSlot:
    """
    Rooms: Talk room 1, Talk room 2, breakout room, Poster room 1, Poster room 2
    types : plenary, oral
    """

    start: datetime
    end: datetime
    room: str
    type: str
    chair: str

    day: str

    num_presentations: int

    @property
    def num_presentations(self):
        if type_to_duration[self.type] is None:
            return 1
        duration = self.end - self.start
        return int(duration.total_seconds() / type_to_duration[self.type])

    @property
    def day(self):
        if self.start.day == 10:
            return "Tuesday"
        elif self.start.day == 11:
            return "Wednesday"

    def __init__(self, start, end, room=None, type=None, chair=None):
        self.start = start
        self.end = end
        self.room = room
        self.type = type
        self.chair = chair

    def __str__(self):
        start_minute = str(self.start.minute).zfill(2)
        end_minute = str(self.end.minute).zfill(2)
        return f"{self.start.hour}:{start_minute} - {self.end.hour}:{end_minute}"


def session_to_time(session_id: str):
    if session_id == "session_welcome":
        return TimeSlot(
            start=datetime(2026, 3, 10, 8, 40, tzinfo=cet),
            end=datetime(2026, 3, 10, 9, 00, tzinfo=cet),
            room="Auditorium",
            type="Opening",
        )
    elif session_id == "session_closing":
        return TimeSlot(
            start=datetime(2026, 3, 11, 17, 10, tzinfo=cet),
            end=datetime(2026, 3, 11, 17, 20, tzinfo=cet),
            room="Auditorium",
            type="Closing",
        )
    elif session_id == "session_panel":
        return TimeSlot(
            start=datetime(2026, 3, 10, 13, 40, tzinfo=cet),
            end=datetime(2026, 3, 10, 14, 40, tzinfo=cet),
            room="Auditorium",
            chair="TBC, Affiliation",
        )
    elif session_id == "session_poster_1":
        return TimeSlot(
            start=datetime(2026, 3, 10, 11, 20, tzinfo=cet),
            end=datetime(2026, 3, 10, 12, 20, tzinfo=cet),
            room="Foyer",
        )
    elif session_id == "session_poster_2":
        return TimeSlot(
            start=datetime(2026, 3, 11, 11, 20, tzinfo=cet),
            end=datetime(2026, 3, 11, 12, 20, tzinfo=cet),
            room="Foyer",
        )
    elif session_id == "session_plenary_1":
        return TimeSlot(
            start=datetime(2026, 3, 10, 9, 00, tzinfo=cet),
            end=datetime(2026, 3, 10, 10, 00, tzinfo=cet),
            room="Auditorium",
            type="Plenary",
            chair="TBC, Affiliation",
        )
    elif session_id == "session_plenary_2":
        return TimeSlot(
            start=datetime(2026, 3, 11, 9, 00, tzinfo=cet),
            end=datetime(2026, 3, 11, 10, 00, tzinfo=cet),
            room="Auditorium",
            type="Plenary",
            chair="TBC, Affiliation",
        )
    elif session_id == "session_plenary_3":
        return TimeSlot(
            start=datetime(2026, 3, 11, 13, 40, tzinfo=cet),
            end=datetime(2026, 3, 11, 14, 40, tzinfo=cet),
            room="Auditorium",
            type="Plenary",
            chair="TBC, Affiliation",
        )
    elif session_id == "session_tut_1":
        return TimeSlot(
            start=datetime(2026, 3, 10, 10, 20, tzinfo=cet),
            end=datetime(2026, 3, 10, 11, 20, tzinfo=cet),
            room="Seminar room 1",
            type="Tutorial",
            chair="TBC, Affiliation",
        )
    elif session_id == "session_tut_2":
        return TimeSlot(
            start=datetime(2026, 3, 10, 14, 40, tzinfo=cet),
            end=datetime(2026, 3, 10, 15, 40, tzinfo=cet),
            room="Seminar room 1",
            type="Tutorial",
            chair="TBC, Affiliation",
        )
    elif session_id == "session_tut_3":
        return TimeSlot(
            start=datetime(2026, 3, 10, 16, 00, tzinfo=cet),
            end=datetime(2026, 3, 10, 17, 00, tzinfo=cet),
            room="Seminar room 1",
            type="Tutorial",
            chair="TBC, Affiliation",
        )
    elif session_id == "session_tut_4":
        return TimeSlot(
            start=datetime(2026, 3, 11, 10, 20, tzinfo=cet),
            end=datetime(2026, 3, 11, 11, 20, tzinfo=cet),
            room="Seminar room 1",
            type="Tutorial",
            chair="TBC, Affiliation",
        )
    elif session_id == "session_tut_5":
        return TimeSlot(
            start=datetime(2026, 3, 11, 14, 40, tzinfo=cet),
            end=datetime(2026, 3, 11, 15, 40, tzinfo=cet),
            room="Seminar room 1",
            type="Tutorial",
            chair="TBC, Affiliation",
        )
    elif session_id == "session_tut_6":
        return TimeSlot(
            start=datetime(2026, 3, 11, 16, 00, tzinfo=cet),
            end=datetime(2026, 3, 11, 17, 00, tzinfo=cet),
            room="Seminar room 1",
            type="Tutorial",
            chair="TBC, Affiliation",
        )
    elif session_id == "session_oral_A":
        return TimeSlot(
            start=datetime(2026, 3, 10, 10, 20, tzinfo=cet),
            end=datetime(2026, 3, 10, 11, 20, tzinfo=cet),
            room="Auditorium",
            type="Oral",
            chair="TBC, Affiliation",
        )
    elif session_id == "session_oral_B":
        return TimeSlot(
            start=datetime(2026, 3, 10, 10, 20, tzinfo=cet),
            end=datetime(2026, 3, 10, 11, 20, tzinfo=cet),
            room="Projektraum",
            type="Oral",
            chair="TBC, Affiliation",
        )
    elif session_id == "session_oral_C":
        return TimeSlot(
            start=datetime(2026, 3, 10, 14, 40, tzinfo=cet),
            end=datetime(2026, 3, 10, 15, 40, tzinfo=cet),
            room="Auditorium",
            type="Oral",
            chair="TBC, Affiliation",
        )
    elif session_id == "session_oral_D":
        return TimeSlot(
            start=datetime(2026, 3, 10, 14, 40, tzinfo=cet),
            end=datetime(2026, 3, 10, 15, 40, tzinfo=cet),
            room="Projektraum",
            type="Oral",
            chair="TBC, Affiliation",
        )
    elif session_id == "session_oral_E":
        return TimeSlot(
            start=datetime(2026, 3, 10, 16, 00, tzinfo=cet),
            end=datetime(2026, 3, 10, 17, 00, tzinfo=cet),
            room="Auditorium",
            type="Oral",
            chair="TBC, Affiliation",
        )
    elif session_id == "session_oral_F":
        return TimeSlot(
            start=datetime(2026, 3, 10, 16, 00, tzinfo=cet),
            end=datetime(2026, 3, 10, 17, 00, tzinfo=cet),
            room="Projektraum",
            type="Oral",
            chair="TBC, Affiliation",
        )
    elif session_id == "session_oral_G":
        return TimeSlot(
            start=datetime(2026, 3, 11, 10, 20, tzinfo=cet),
            end=datetime(2026, 3, 11, 11, 20, tzinfo=cet),
            room="Auditorium",
            type="Oral",
            chair="TBC, Affiliation",
        )
    elif session_id == "session_oral_H":
        return TimeSlot(
            start=datetime(2026, 3, 11, 10, 20, tzinfo=cet),
            end=datetime(2026, 3, 11, 11, 20, tzinfo=cet),
            room="Projektraum",
            type="Oral",
            chair="TBC, Affiliation",
        )
    elif session_id == "session_oral_I":
        return TimeSlot(
            start=datetime(2026, 3, 11, 14, 40, tzinfo=cet),
            end=datetime(2026, 3, 11, 15, 40, tzinfo=cet),
            room="Auditorium",
            type="Oral",
            chair="TBC, Affiliation",
        )
    elif session_id == "session_oral_J":
        return TimeSlot(
            start=datetime(2026, 3, 11, 14, 40, tzinfo=cet),
            end=datetime(2026, 3, 11, 15, 40, tzinfo=cet),
            room="Projektraum",
            type="Oral",
            chair="TBC, Affiliation",
        )
    elif session_id == "session_oral_K":
        return TimeSlot(
            start=datetime(2026, 3, 11, 16, 00, tzinfo=cet),
            end=datetime(2026, 3, 11, 17, 00, tzinfo=cet),
            room="Auditorium",
            type="Oral",
            chair="TBC, Affiliation",
        )
    elif session_id == "session_oral_L":
        return TimeSlot(
            start=datetime(2026, 3, 11, 16, 00, tzinfo=cet),
            end=datetime(2026, 3, 11, 17, 00, tzinfo=cet),
            room="Projektraum",
            type="Oral",
            chair="TBC, Affiliation",
        )

    raise ValueError(f"Unknown session {session_id}")


breaks = [
    TimeSlot(
        start=datetime(2026, 3, 10, 10, 00, tzinfo=cet),
        end=datetime(2026, 3, 10, 10, 20, tzinfo=cet),
    ),
    TimeSlot(
        start=datetime(2026, 3, 10, 15, 40, tzinfo=cet),
        end=datetime(2026, 3, 10, 16, 00, tzinfo=cet),
    ),
    TimeSlot(
        start=datetime(2026, 3, 11, 10, 00, tzinfo=cet),
        end=datetime(2026, 3, 11, 10, 20, tzinfo=cet),
    ),
    TimeSlot(
        start=datetime(2026, 3, 11, 15, 40, tzinfo=cet),
        end=datetime(2026, 3, 11, 16, 00, tzinfo=cet),
    ),
]

lunches = [
    TimeSlot(
        start=datetime(2026, 3, 10, 12, 20, tzinfo=cet),
        end=datetime(2026, 3, 10, 13, 40, tzinfo=cet),
    ),
    TimeSlot(
        start=datetime(2026, 3, 11, 12, 20, tzinfo=cet),
        end=datetime(2026, 3, 11, 13, 40, tzinfo=cet),
    ),
]
