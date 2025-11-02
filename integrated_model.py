"""
Integrated Energy Harvesting Model
----------------------------------
This script combines results from both the thermoelectric and piezoelectric
energy harvesting models to estimate the *total* available power for the
self-powered implantable biosensor.

It imports both models, runs them, and then prints the combined energy budget.
"""

# Import both models
from energy_model import estimate_thermoelectric_power
from piezo_model import estimate_piezo_power

def integrated_power_estimate():
    """
    Run both energy harvesting models and return the total available power.
    """

    # 1. Estimate power from thermoelectric harvesting (body heat)
    power_thermo = estimate_thermoelectric_power(
        area_cm2=4.0,          # surface area of the thermoelectric module
        delta_T=3.0,           # typical human skin temperature difference (°C)
        efficiency=0.06        # assumed thermoelectric efficiency (6%)
    )

    # 2. Estimate power from piezoelectric harvesting (motion)
    power_piezo = estimate_piezo_power(
        frequency_hz=1.2,      # typical body motion frequency (steps/heartbeat)
        strain_level=0.004,    # low-level muscle strain (0.4%)
        material_factor=0.45   # piezoelectric material coefficient
    )

    # 3. Combine both results
    total_power = power_thermo + power_piezo

    print("----- Integrated Energy Harvesting Estimate -----")
    print(f"Thermoelectric power: {power_thermo:.3f} microwatts")
    print(f"Piezoelectric power:  {power_piezo:.3f} microwatts")
    print("-----------------------------------------------")
    print(f"Total estimated power: {total_power:.3f} microwatts")
    print("--------------------------------------------------")

    return total_power


if __name__ == "__main__":
    integrated_power_estimate()
