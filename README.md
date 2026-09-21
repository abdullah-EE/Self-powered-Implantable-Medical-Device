# Self-Powered Implantable Biosensor — Energy Harvesting Feasibility Study

An early-stage engineering study exploring whether **thermoelectric and piezoelectric energy harvesting** could support an ultra-low-power implantable sensing system.

The goal is not to claim a battery-free medical device. The goal is to build an order-of-magnitude power model and understand the engineering constraints that determine whether energy harvesting could meaningfully extend implant lifetime.

## Core question

Can small amounts of energy harvested from **body heat and motion** support a sensing architecture that:

1. spends most of its time in an ultra-low-power state,
2. stores harvested energy,
3. measures or logs data intermittently, and
4. transmits only in short bursts when enough energy is available?

## Conceptual architecture

~~~text
Body heat ─→ Thermoelectric harvester ─┐
                                       ├─→ Power management ─→ Energy storage
Body motion → Piezoelectric harvester ─┘                         │
                                                                ↓
                                                     Sensor + low-power MCU
                                                                │
                                                        Burst transmission
~~~

## Models in this repository

- energy_model.py — first-pass thermoelectric power estimate
- piezo_model.py — first-pass piezoelectric power estimate
- integrated_model.py — experimental attempt to combine both harvesting paths

The models use simplified assumptions and are intended for **feasibility reasoning**, not medical-device validation.

## Engineering focus

The interesting constraint is the power budget. Implantable sensing is only plausible when the load is treated as a duty-cycled system rather than assuming an always-on radio.

This project therefore focuses on:

- harvested power in the microwatt range
- energy storage between active periods
- low-power sensing
- duty cycling
- burst communication
- understanding where assumptions dominate the result

## Current status

Early computational feasibility work. The repository contains Python models and initial power-budget reasoning; it does not contain a fabricated implant or validated biomedical hardware.

## Run the models

~~~bash
python energy_model.py
python piezo_model.py
python integrated_model.py
~~~

## Why I built it

This project was an exploration at the intersection of **electrical engineering, energy harvesting, low-power electronics, and biomedical systems**. More importantly, it was an exercise in testing an ambitious idea against a power budget before treating it as a viable device.

## Important note

This is an educational engineering feasibility project, **not a medical device and not medical advice**.
