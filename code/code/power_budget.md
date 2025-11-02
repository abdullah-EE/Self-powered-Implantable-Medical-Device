# Power Budget and Feasibility

Question:
Can an implantable biosensor run off harvested energy from the human body instead of a replaceable battery?

Short answer:
Yes for logging and monitoring, maybe for burst transmissions, no for 24/7 live radio.

## How the device should behave

The point is not "always transmit data nonstop." That's fantasy at microwatt levels.

The realistic strategy is:
1. Sense data continuously at ultra-low power (heart rate, temperature, etc.).
2. Store data locally.
3. Wait until enough energy is harvested and stored.
4. Transmit in a short burst, then go quiet again.

So instead of constant Bluetooth, it's more like smart check-ins.

## Typical power needs (order of magnitude)

- Low-power biosensor sampling: ~1–10 µW
- Microcontroller in deep sleep: <1 µW
- Microcontroller awake doing processing: ~50–200 µW (but only for milliseconds)
- Radio transmit burst: milliwatts (mW), but only for a fraction of a second

What matters is AVERAGE power over time, not the peak.

## Thermoelectric model (energy_model.py)

Assumptions:
- Temperature difference ΔT ~ 5 °C inside the body vs surface
- ~100 thermocouple junctions in series
- Matched load and internal resistance ~50 Ω

Results:
- Output power is in the range of a few microwatts (µW)

Interpretation:
- This looks borderline but viable for always-on sensing + logging
- You would NOT try to run constant wireless transmit with only this

## Piezoelectric model (piezo_model.py)

Assumptions:
- ~1 N compression force per cycle
- ~2 Hz motion frequency (like walking-level movement)
- Piezo capacitance ~100 nF
- ~30% capture efficiency

Results:
- Average harvested power also lands in the µW range, if there's repeated motion

Interpretation:
- Good for high-motion placements (near muscle, arterial wall, joint surfaces)
- Weak in static locations

## So is it feasible?

Yes, if:
- You design for ultra-low-power sensing
- You use local storage
- You transmit data only sometimes, not constantly
- You include even a tiny energy buffer (thin-film battery / capacitor)

In other words:
This is not "unlimited wireless power forever."  
This IS "battery-less continuous monitoring, with smart burst communication."

## Next steps

- Add a diagram showing:
  Energy harvester → rectifier → storage → microcontroller → radio burst
- Add duty cycle math:
  How long does it take to collect enough energy for one data upload?
- Prepare a short PDF/slide summary for professors / labs / admissions
