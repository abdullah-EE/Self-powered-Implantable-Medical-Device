# Power Budget and Feasibility Analysis

Goal: figure out if an implantable biosensor can realistically power itself using only harvested energy from the human body (heat and motion), without needing constant battery replacements.

This document estimates:
1. How much power we can harvest (in microwatts, µW)
2. How much power the device needs to operate
3. Whether the device can run continuously, or only in short bursts

---

## 1. Harvested Power Sources

### A. Thermoelectric harvesting (body heat)
We assume a very small thermoelectric generator (TEG) sitting across a temperature difference between inside tissue and skin.

- Deep tissue temperature: ~37 °C
- Near-surface/skin temp: ~32 °C  
- ΔT (temperature difference): ~5 °C

The `energy_model.py` script uses:
- Seebeck coefficient ~200 µV/K
- Matched load resistance ~50 Ω
- Efficiency ~3%
- Active area ~1 cm²

Result:
- Estimated output is around **tens of microwatts (µW)** under ideal contact.
- Typical baseline modeled value: about **30–40 µW** continuous.

This is not huge power, but it is 24/7 as long as the gradient exists.

---

### B. Piezoelectric harvesting (motion / pressure / vibration)
We assume a small piezoelectric element that flexes or compresses with body motion. It converts mechanical strain into electrical charge.

The `piezo_model.py` script assumes:
- Force per cycle: about 1 newton of squeeze
- Frequency: ~2 compressions per second (like normal movement or pulse vibration)
- Capacitance: ~100 nF
- Load resistance: 1 MΩ
- Efficiency: ~80%

Result:
- Estimated output is also in the **few µW to tens of µW** range depending on motion.
- Importantly, this is not constant: it depends on movement. Less motion = less power.

---

### C. Combined harvesting
If we add both sources:
- Thermoelectric gives baseline power, even at rest.
- Piezoelectric adds "bonus" power when you move, breathe, walk, etc.

The `integrated_model.py` script sums both models and reports total harvested power in µW.

Example rough target:
- Thermoelectric: ~35 µW
- Piezoelectric: ~8 µW (average over time)
- **Total estimated: ~43 µW**

This total number can go up or down based on placement and the real environment, but these are reasonable order-of-magnitude values for early feasibility.

---

## 2. Power Consumption of the Implant

The device is assumed to have 3 main loads:

### (1) Sensing
- A low-power biosensor can sample things like temperature, heart rhythm, or pressure using <5 µW average if duty-cycled (sensor is not running at full speed nonstop; it “wakes,” samples, sleeps).

### (2) Microcontroller / processing
- Modern ultra-low-power microcontrollers can idle in deep sleep below 1 µW and briefly wake to process/store data using tens of µW to a few hundred µW, but only for milliseconds.
- If the controller sleeps most of the time and only wakes in bursts, we can average this down to a few µW total.

### (3) Wireless transmission
- Radio is the expensive part.
- A wireless burst (ex: BLE-style packet, NFC-like dump, etc.) can easily spike into milliwatt range, which is way higher than what we harvest.
- So continuous live streaming is NOT realistic.
- But saving data locally and transmitting RARELY (for example, once every few minutes or once an hour) is realistic, because you can charge a tiny storage element (thin-film battery or capacitor) and then dump the data.

In other words:
- Always-on sensing = yes
- Always-on transmitting = no
- Occasional burst transmit = possible

---

## 3. Duty Cycle Strategy (How this actually works)

You don’t run everything full power all the time. You run in phases:

1. **Harvest mode / logging mode**
   - Sensor measures slowly (like once per second or once per few seconds)
   - Microcontroller stores those readings to local memory
   - Radio is OFF
   - Average power draw target here: ~10 µW or less

2. **Burst transmit mode**
   - After enough energy is stored, the device wakes radio
   - Sends a packet (for example: last 10 minutes of data)
   - Goes back to sleep

So instead of needing 5,000+ µW constantly for a radio, you only need short spikes that you “budget for” using stored energy. That’s how you survive on ~40 µW continuous harvest.

This is what makes the system feasible.

---

## 4. Is it realistic?

Summary of the numbers:
- Harvested total power: ~30–50 µW range under decent conditions
- Target continuous load during sensing/logging: ~10 µW or less
- Transmission: spiky, but not constant

Conclusion:
- **Yes, it is theoretically possible to support a very low-power implant in a duty-cycled way using harvested energy alone.**
- The implant would not be streaming live data 24/7. Instead, it would collect data quietly and “check in” occasionally.
- This reduces the number of surgeries needed just to replace a dead battery.

---

## 5. Limitations / Next steps

Real challenges we still have to solve:
- Real tissue temperature gradients might be smaller than the ideal 5 °C assumed.
- Mechanical strain / motion might not be consistent for every implant site or every patient.
- Power electronics overhead (rectifier, regulators, storage leakage) will eat part of the harvested µW.
- Biocompatibility, packaging, thermal coupling, and heat flow pathways are non-trivial.

Next steps in this project:
1. Refine the models with more realistic body placement assumptions.
2. Model storage: how quickly a tiny capacitor can charge using the harvested energy.
3. Simulate timing: how often can we afford a transmit burst?
4. Document use cases (heart monitor? pressure sensor? temperature probe?).

---

## 6. Key takeaway

This is NOT sci-fi "infinite free energy."

It's "harvest a tiny trickle of energy forever, store it, and spend it smart."

That’s good enough to keep a sensor alive inside a human body without constant surgical battery swaps.
