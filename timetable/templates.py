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
site:
  hide_toc: false
---

Here you will find the schedule and abstracts for the OSSFE 2025 conference

# Tuesday 
{tables_day_1}

# Wednesday 
{tables_day_2}
"""
)

template_list_of_posters = dedent(
    """---
title: "List of posters"
site:
  hide_toc: false
---

Here you will find the posters for the OSSFE 2026 conference which will both take place in the Foyer.

Poster session 1 ({poster_session_1_time_slot} Tuesday):
{poster_session_1}

Poster session 2 ({poster_session_2_time_slot} Wednesday):
{poster_session_2}
"""
)

plenary_session = dedent(
    """\
## Plenary Session {session_id}: {time_slot}

Room: {room}

*Chair*: {chair}

Number of presentations: {num_presentations}

{table}
"""
)

oral_session = dedent(
    """\
## Oral Session {session_id}: {time_slot}

Room: {room}

*Chair*: {chair}

Number of presentations: {num_presentations}

{table}
"""
)

opening_session = dedent(
    """\
## 🎉 Welcome statement: {time_slot}

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
## 🛠️ Tutorial Session {session_id}: {time_slot}

Room: {room}

A series of tutorials will be available to attend for the following packages:

Number of presentations: {num_presentations}

{table}
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
