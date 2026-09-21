"""Simplified piezoelectric energy-harvesting model for an implant feasibility study.

This is an order-of-magnitude engineering model, not a validated medical-device model.
"""

DEFAULT_FORCE_N = 1.0
DEFAULT_FREQUENCY_HZ = 2.0
DEFAULT_CHARGE_CONSTANT_C_PER_N = 20e-12
DEFAULT_CAPACITANCE_F = 100e-9
DEFAULT_EFFICIENCY = 0.30


def piezoelectric_power(
    force: float = DEFAULT_FORCE_N,
    freq: float = DEFAULT_FREQUENCY_HZ,
    charge_const: float = DEFAULT_CHARGE_CONSTANT_C_PER_N,
    capacitance: float = DEFAULT_CAPACITANCE_F,
    efficiency: float = DEFAULT_EFFICIENCY,
) -> float:
    """Return estimated average harvested power in microwatts."""
    if force < 0 or freq < 0 or capacitance <= 0:
        raise ValueError("Model parameters must be physically valid.")
    if not 0 <= efficiency <= 1:
        raise ValueError("Efficiency must be between 0 and 1.")

    charge = charge_const * force
    ideal_voltage = charge / capacitance
    energy_per_cycle_j = 0.5 * capacitance * (ideal_voltage ** 2) * efficiency
    power_w = energy_per_cycle_j * freq
    return power_w * 1e6


def main() -> None:
    power_uw = piezoelectric_power()
    print("=== Piezoelectric Harvest Model ===")
    print(f"Applied force: {DEFAULT_FORCE_N:.2f} N")
    print(f"Motion frequency: {DEFAULT_FREQUENCY_HZ:.2f} Hz")
    print(f"Estimated average power: {power_uw:.6f} µW")
    print("Note: simplified feasibility estimate; real performance depends on strain,")
    print("material choice, coupling, placement, and rectification losses.")


if __name__ == "__main__":
    main()
