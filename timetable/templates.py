from textwrap import dedent


template = dedent(
    """---
title: "OSSFE conference - March 10th - 12th 2026"
authors:
  - name: James Dark
    affiliations:
      - Plasma Science and Fusion Centre, MIT
    email: ossfecontact@gmail.com
  - name: Rémi Delaporte-Mathurin
    affiliations:
      - Plasma Science and Fusion Centre, MIT
    email: ossfecontact@gmail.com
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../template
---

Here you will find the schedule and abstracts for the OSSFE 2025 conference

# Schedule
{tables}
"""
)

template_list_of_posters = dedent(
    """---
title: "List of posters"
---

Here you will find the posters for the OSSFE 2026 conference

The poster session will take place at {poster_session_1_time_slot} on March 10th 
and {poster_session_2_time_slot} on March 11th in the Foyer.

"""
)

table_template = dedent(
    """\
## Session {session_id}: {time_slot}

Room: {room}

*Chair*: {chair}

Number of presentations: {num_presentations}

{table}
"""
)

opening_session = dedent(
    """\
## 🎉 Welcome statement by the organising committee: {time_slot}

Room: {room}

Presenter: Remi Delaporte-Mathurin
"""
)

closing_session = dedent(
    """\
## 🏆 Awards ceremony and closing remarks: {time_slot}

Room: {room}

Presenter: Remi Delaporte-Mathurin
"""
)

poster_session = dedent(
    """\
## 🖼️  Poster Session: {time_slot}

A full list of the posters and their abstracts can be found in the [List of posters](list_of_posters.md)
"""
)

tutorial_session = dedent(
    """\
## 🛠️ Tutorial Session: {time_slot}

Room: {room}

A series of tutorials will be available to attend for the following packages:

{demos}
"""
)

panel_session = dedent(
    """\
## 🗣️ Panel Session: {time_slot}

Room: {room}

*Chair*: {chair}

A panel session will be held with the following members:
{table}
"""
)

break_template = dedent(
    """\
## ☕ Break: {time_slot}

Take the opportunity to make yourself tea or coffee and network with other attendees in the lobby!
"""
)

lunch_template = dedent(
    """\
## 🍽️ Lunch break: {time_slot}

"""
)
