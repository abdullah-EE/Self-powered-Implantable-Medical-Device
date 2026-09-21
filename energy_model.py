"""Simplified thermoelectric energy-harvesting model for an implant feasibility study.

This is an order-of-magnitude engineering model, not a validated medical-device model.
"""

DEFAULT_DELTA_T_K = 5.0
SEEBECK_PER_JUNCTION_V_PER_K = 200e-6
DEFAULT_JUNCTIONS = 100
DEFAULT_INTERNAL_RESISTANCE_OHM = 50.0
DEFAULT_LOAD_RESISTANCE_OHM = 50.0
DEFAULT_CONVERSION_EFFICIENCY = 0.03


def thermoelectric_power(
    delta_t: float = DEFAULT_DELTA_T_K,
    seebeck_per_junction: float = SEEBECK_PER_JUNCTION_V_PER_K,
    junctions: int = DEFAULT_JUNCTIONS,
    r_internal: float = DEFAULT_INTERNAL_RESISTANCE_OHM,
    r_load: float = DEFAULT_LOAD_RESISTANCE_OHM,
    efficiency: float = DEFAULT_CONVERSION_EFFICIENCY,
) -> float:
    """Return estimated electrical power delivered to the load in microwatts."""
    if delta_t < 0 or junctions <= 0 or r_internal <= 0 or r_load <= 0:
        raise ValueError("Model parameters must be physically valid.")
    if not 0 <= efficiency <= 1:
        raise ValueError("Efficiency must be between 0 and 1.")

    open_circuit_voltage = seebeck_per_junction * delta_t * junctions
    current = open_circuit_voltage / (r_internal + r_load)
    load_power_w = (current ** 2) * r_load * efficiency
    return load_power_w * 1e6


def main() -> None:
    power_uw = thermoelectric_power()
    print("=== Thermoelectric Harvest Model ===")
    print(f"Temperature difference: {DEFAULT_DELTA_T_K:.2f} K")
    print(f"Thermocouple junctions: {DEFAULT_JUNCTIONS}")
    print(f"Estimated delivered power: {power_uw:.4f} µW")
    print("Note: simplified feasibility estimate; real performance depends on geometry,")
    print("thermal coupling, material properties, packaging, and power electronics.")


if __name__ == "__main__":
    main()
