"""Combine the simplified thermoelectric and piezoelectric feasibility models."""

from energy_model import thermoelectric_power
from piezo_model import piezoelectric_power


def integrated_power_estimate() -> float:
    """Return the combined first-pass harvested-power estimate in microwatts."""
    power_thermo_uw = thermoelectric_power(delta_t=3.0, efficiency=0.03)
    power_piezo_uw = piezoelectric_power(freq=1.2, efficiency=0.30)
    total_power_uw = power_thermo_uw + power_piezo_uw

    print("=== Integrated Energy Harvesting Estimate ===")
    print(f"Thermoelectric: {power_thermo_uw:.6f} µW")
    print(f"Piezoelectric:  {power_piezo_uw:.6f} µW")
    print(f"Combined:       {total_power_uw:.6f} µW")
    print("This is a simplified feasibility estimate, not a validated implant power budget.")

    return total_power_uw


if __name__ == "__main__":
    integrated_power_estimate()
