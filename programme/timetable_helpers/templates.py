from textwrap import dedent


schedule_template = dedent(
    """---
title: "OSSFE 2026 Programme"
subtitle: "OSSFE 2026 technical programme committee"
authors:
  - name: James Dark
    affiliations:
      - Plasma Science and Fusion Centre, MIT
    email: ossfecontact@gmail.com
  - name: Nathan Cummings
    affiliations:
      - UK Atomic Energy Authority
  - name: Alex Tinguely
    affiliations:
      - Plasma Science and Fusion Centre, MIT
  - name: Jin whan Bae
    affiliations:
      - Oak Ridge National Laboratory

license: CC-BY-4.0
exports:
  - format: pdf
    template: ../template
site:
  hide_toc: false
---

Here you will find the schedule and abstracts for the OSSFE 2026 conference

---
# Tuesday
{tables_day_1}

# Wednesday
{tables_day_2}

# Thursday 
{tables_day_3}
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

---
"""
)

oral_session = dedent(
    """\
### Oral Session {session_id}

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

---
"""
)

closing_session = dedent(
    """\
## 🏆 Awards ceremony and closing remarks: {time_slot}

Room: {room}

Presenter: Remi Delaporte-Mathurin

---
"""
)

poster_session = dedent(
    """\
## 🖼️  Poster Session: {time_slot}

A full list of the posters and their abstracts can be found in the [List of posters](list_of_posters.md)

---
"""
)

tutorial_session = dedent(
    """\
### 🛠️ Tutorial Session {session_id}

Room: {room}

A series of tutorials will be available to attend for the following packages:

Number of tutorials: {num_presentations}

{table}

---
"""
)

panel_session = dedent(
    """\
## 🗣️ Panel Session: {time_slot}

Room: {room}

*Chair*: {chair}

A panel session will be held with the following members:
{table}

---
"""
)

break_template = dedent(
    """\
## ☕ Break: {time_slot}

Coffee, tea refreshments and pastries will be served in the Foyer.

---
"""
)

lunch_template = dedent(
    """\
## 🍽️ Lunch break: {time_slot}

Lunch is provided in the Munich Urban Colab restaurant (ground floor) for all conference attendees.

---
"""
)

lunch_proxima = dedent(
    """\
## 🍽️ Lunch break: {time_slot}

Lunch is provided in the Proxima Fusion office for all Hackathon attendees.

---
"""
)

proxima_tour = dedent(
    """\
## 🚶 Proxima Fusion tour: {time_slot}

|  |  |
|---|---|
| ![](../assets/proxima_image.png) | ![](../assets/proxima_facilty.png) |

Join us for an optional social event and get a behind-the-scenes look at Proxima Fusion's facilities.

---
"""
)


hackathon = dedent(
    """\
## 🖳 OSSFE Hackathon: {time_slot}

An optional add-on event for conference attendees. 
This will be an oppertunity to interact work together with open-source developers on projects of interest and see the
contiribution process first-hand.

*Structure and details to be announced*

---
"""
)
