from typing import Sequence
import argparse
from pathlib import Path
from faker import Faker
import csv

# create list of strings
plenary_slots = [f"P{i}" for i in range(1, 7)]
plenary_sessions = [f"session_plenary_{(i // 2) + 1}" for i in range(6)]

oral_slots = [f"{letter}{i}" for letter in "ABCDEFGHIJKL" for i in range(1, 4)]
oral_sessions = [f"session_oral_{'ABCDEFGHIJKL'[i // 3]}" for i in range(36)]

tutorial_slots = [f"T{i}" for i in range(1, 13)]
tutorial_sessions = [f"session_tut_{(i // 2) + 1}" for i in range(12)]

slots = plenary_slots + oral_slots + tutorial_slots
sessions = plenary_sessions + oral_sessions + tutorial_sessions


def authors(fake: Faker, n: int) -> str:
    authors = []
    for i in range(n):
        authors.append(fake.name())
    return ", ".join(authors)


def affiliations(fake: Faker, n: int) -> str:
    affiliations = []
    for i in range(n):
        affiliations.append(fake.company())
    return ", ".join(affiliations)


def abstract_id_to_decision(abstract_id: int) -> str:
    if abstract_id <= 6:
        return "Plenary"
    elif abstract_id <= 42:
        return "Oral"
    elif abstract_id <= 54:
        return "Tutorial"
    else:
        return "Poster"


def abstract_id_to_slot_id(abstract_id: int) -> str:
    if abstract_id <= 54:
        return slots[abstract_id - 1]
    elif abstract_id <= 64:
        return "session_poster_1"
    else:
        return "session_poster_2"


def abstract_id_to_session(abstract_id: int) -> str:
    if abstract_id <= 54:
        return sessions[abstract_id - 1]
    elif abstract_id <= 64:
        return "session_poster_1"
    else:
        return "session_poster_2"


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("path", type=Path)
    parser.add_argument("N", type=int, default=10)
    args = vars(parser.parse_args(argv))

    fake = Faker()
    fake.seed_instance(4321)

    path = Path(args["path"]).with_suffix(".csv")

    fieldnames = [
        "Abstract ID",
        "Email",
        "First name",
        "Last name",
        "Affiliation",
        "Topic",
        "Title",
        "Abstract",
        "List of authors and affiliations",
        "Link to open-source software repository (if applicable)",
        "Abstract decision",
        "Slot",
        "Session",
    ]
    with path.open("w") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

        for i in range(args["N"]):
            num_authors = fake.random_int(1, 5)
            id = i + 1

            decision = abstract_id_to_decision(id)
            slot_id = abstract_id_to_slot_id(id)
            session_id = abstract_id_to_session(id)

            data = {
                "Abstract ID": int(i + 1),
                "Email": fake.email(),
                "First name": fake.first_name(),
                "Last name": fake.last_name(),
                "Affiliation": fake.company(),
                "Topic": fake.word(),
                "Title": fake.sentence(),
                "Abstract": fake.text(),
                "List of authors and affiliations": "; ".join(
                    [f"{fake.name()}, {fake.company()}" for _ in range(num_authors)]
                ),
                "Link to open-source software repository (if applicable)": fake.url(),
                "Abstract decision": decision,
                "Slot": slot_id,
                "Session": session_id,
            }
            writer.writerow(data)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
