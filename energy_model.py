"""
energy_model.py
Estimate harvested electrical power from a small thermoelectric generator (TEG)
using a human body temperature gradient.

This is part of a feasibility study for a self-powered implantable biosensor.

Author: Abdullah Haydar (2025)
"""

# --------------------------
# Assumptions (you can tune these later)
# --------------------------

# Temperature difference between inside body and outer surface (in °C).
# Example: ~37°C core vs ~32°C near surface. A small ΔT like 5°C is realistic in an implant context.
delta_T_celsius = 5.0

# Seebeck coefficient (Volts per Kelvin) for a bismuth telluride (Bi2Te3)-type thermoelectric material.
# ~200 microvolts per Kelvin per junction is a common ballpark.
seebeck_per_junction = 200e-6  # 200 µV/K

# Number of thermocouples in series in a tiny module.
# We keep this small, because implants have serious space limits.
num_junctions = 100

# Internal electrical resistance of the TEG in ohms.
# Higher resistance means less current delivery.
teg_internal_resistance = 50.0  # ohms (rough guess for a tiny harvester)

# Load resistance in ohms.
# Matching load ~ internal resistance gives near max power transfer.
load_resistance = 50.0  # ohms


# --------------------------
# Calculations
# --------------------------

# ΔT (Kelvin) is numerically the same as ΔT (Celsius), so we just reuse it here.
delta_T_kelvin = delta_T_celsius

# Open-circuit voltage (no load attached):
# Voc = Seebeck * ΔT * N
open_circuit_voltage = seebeck_per_junction * delta_T_kelvin * num_junctions  # Volts

# Current delivered to a resistive load using voltage divider:
# I = Voc / (R_internal + R_load)
current_amperes = open_circuit_voltage / (teg_internal_resistance + load_resistance)

# Voltage delivered across the load:
voltage_load = current_amperes * load_resistance  # Volts

# Power delivered to the load:
# P = V^2 / R  (equivalent to I^2 * R)
power_watts = (voltage_load ** 2) / load_resistance

# Convert to microwatts (µW), which is the scale implants actually care about.
power_microwatts = power_watts * 1e6


# --------------------------
# Output
# --------------------------

print("=== Thermoelectric Harvest Model ===")
print(f"Temperature difference (ΔT):         {delta_T_celsius:.2f} °C")
print(f"Seebeck per junction:                {seebeck_per_junction*1e6:.1f} µV/K")
print(f"Number of junctions:                 {num_junctions}")
print(f"Open-circuit voltage (no load):      {open_circuit_voltage*1000:.3f} mV")
print()
print(f"Load resistance:                     {load_resistance:.1f} Ω")
print(f"Internal resistance:                 {teg_internal_resistance:.1f} Ω")
print(f"Current delivered:                   {current_amperes*1e6:.3f} µA")
print(f"Voltage across load:                 {voltage_load*1000:.3f} mV")
print(f"Power into load:                     {power_microwatts:.3f} µW")

# High-level interpretation for humans / admission reviewers
if power_microwatts >= 10:
    meaning = "This could run ultra-low-power sensing plus short wireless bursts."
elif power_microwatts >= 1:
    meaning = "Borderline usable. Needs energy storage and duty cycling."
else:
    meaning = "Very low harvest. You'd have to store energy over time before doing anything."

print()
print("Interpretation:", meaning)
print("Note: Implant strategy is NOT constant radio. It's log quietly, then transmit in bursts.")
"""
energy_model.py
----------------
Simulates thermoelectric energy harvesting from body heat.

This model estimates the power output (in microwatts) from a small thermoelectric
generator (TEG) implanted in the body. It uses basic physical parameters such as
temperature difference, surface area, material efficiency, and internal resistance
to estimate whether a biosensor can be powered continuously or intermittently.

Author: Abdullah Haydar (2025)
"""

# --- Imports ---
import math

# --- Constants ---
SEEBECK_COEFF = 0.0002     # Volts per Kelvin (V/K)
BODY_TEMP = 37.0           # Celsius (inside)
SKIN_TEMP = 32.0           # Celsius (surface)
DELTA_T = BODY_TEMP - SKIN_TEMP  # Temperature difference (K)
INTERNAL_RESISTANCE = 50.0 # Ohms
LOAD_RESISTANCE = 50.0     # Ohms
SURFACE_AREA = 0.0001      # m² (1 cm²)
TEG_EFFICIENCY = 0.03      # 3% conversion efficiency

# --- Core calculation ---
def thermoelectric_power(delta_t=DELTA_T, area=SURFACE_AREA, seebeck=SEEBECK_COEFF,
                         r_internal=INTERNAL_RESISTANCE, r_load=LOAD_RESISTANCE,
                         efficiency=TEG_EFFICIENCY):
    """
    Calculate thermoelectric power output (μW).
    """
    voltage = seebeck * delta_t
    total_r = r_internal + r_load
    current = voltage / total_r
    power = (current ** 2) * r_load * efficiency
    return power * 1e6  # convert to microwatts

# --- Run example ---
if __name__ == "__main__":
    p = thermoelectric_power()
    print(f"Estimated thermoelectric power: {p:.3f} μW")
