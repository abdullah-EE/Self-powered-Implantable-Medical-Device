"""
piezo_model.py
Estimate harvested electrical power from a small piezoelectric harvester
that converts mechanical motion / pressure into electrical energy.

This models an implant in or near a location that moves repeatedly (muscle, artery wall, joint area).

Author: Abdullah Haydar (2025)
"""

import math

# --------------------------
# Assumptions (tune if you get better data later)
# --------------------------

# Peak force applied on the piezo element each compression (Newtons).
# 1 N ~ 100 grams-force. We're keeping this gentle because this is inside a body, not a shoe insert.
force_newtons = 1.0  # N

# Motion frequency (Hz). 2 Hz = 2 events per second.
# ~1 Hz is like heartbeat. ~2 Hz could be walking/muscle micro-motions.
frequency_hz = 2.0  # cycles per second

# Piezoelectric coupling modeled as an "effective charge constant" (Coulombs per Newton).
# Example: 20 pC/N (picoCoulombs per Newton). This is simplified, but acceptable for feasibility scale.
charge_constant_c_per_n = 20e-12  # 20 pC/N

# Capacitance of the piezo element (Farads). Small piezo films are often tens to hundreds of nF.
capacitance_f = 100e-9  # 100 nF

# Electrical load we're charging / dumping into.
load_resistance_ohms = 1e6  # 1 megaohm. High resistance lets voltage build.

# Estimated capture efficiency. We don't get to keep all the mechanical -> electrical energy.
efficiency = 0.3  # 30%


# --------------------------
# Calculations
# --------------------------

# Charge per compression:
# Q = d * F
charge_coulombs_per_cycle = charge_constant_c_per_n * force_newtons  # Coulombs

# Ideal peak voltage if all that charge went into the piezo capacitance:
# V = Q / C
voltage_peak_volts = charge_coulombs_per_cycle / capacitance_f

# Realistic effective voltage after losses:
effective_voltage_volts = voltage_peak_volts * efficiency

# Energy stored per cycle:
# E = 0.5 * C * V^2
energy_per_cycle_joules = 0.5 * capacitance_f * (effective_voltage_volts ** 2)

# Power output:
# Power (W) = Energy per cycle (J) * cycles per second (Hz)
power_watts = energy_per_cycle_joules * frequency_hz

# Convert to microwatts
power_microwatts = power_watts * 1e6


# --------------------------
# Output
# --------------------------

print("=== Piezoelectric Harvest Model ===")
print(f"Applied force per cycle:             {force_newtons:.3f} N")
print(f"Motion frequency:                    {frequency_hz:.2f} Hz")
print(f"Piezo capacitance:                   {capacitance_f*1e9:.1f} nF")
print(f"Raw peak voltage (ideal):            {voltage_peak_volts:.3f} V")
print(f"Effective voltage after losses:      {effective_voltage_volts:.3f} V")
print()
print(f"Energy per cycle:                    {energy_per_cycle_joules*1e9:.3f} nJ")
print(f"Average harvested power:             {power_microwatts:.3f} µW")

# Interpretation
if power_microwatts >= 10:
    meaning = "Motion harvesting here can realistically power sensing logic."
elif power_microwatts >= 1:
    meaning = "Usable if energy is buffered and transmit is duty-cycled."
else:
    meaning = "Very low harvest. Must accumulate charge over time before sending data."

print()
print("Interpretation:", meaning)
print("Note: Piezo only works if there's repeated motion. Implants in low-motion areas get less.")
