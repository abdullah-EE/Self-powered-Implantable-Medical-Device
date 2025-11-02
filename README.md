# Self-Powered Implantable Medical Device (Energy-Harvesting Biosensor Concept)

This project explores a self-powered biomedical implant that uses the body's own energy instead of a traditional battery. The main long-term goal is to design an implantable sensor that can monitor health data without requiring surgical battery replacement.

This is early-stage feasibility work:
1. Estimate how much electrical power we can realistically harvest from the body (heat and motion).
2. Compare that harvested power to what a low-power biosensor needs.
3. Design a usage pattern (duty cycle) that makes the device realistic: log data continuously at ultra-low power, then transmit data in bursts only when enough energy is stored.

## Why this matters

Most implantable devices depend on a battery. Replacing that battery means surgery. Surgery means cost, infection risk, and pain.

If an implant can partially recharge itself from energy it harvests inside the body, we get:
- Longer implant lifetime
- Fewer surgeries per patient
- Safer continuous health monitoring
- Better access in places where frequent clinical maintenance is not realistic

The device here is not just “infinite Bluetooth.” The realistic goal is: always-on sensing and logging, plus short data uploads when there is enough stored energy.

## System concept

High level block diagram of the proposed device:

1. Energy harvester  
   - Option A: Thermoelectric (uses body heat / temperature gradient)  
   - Option B: Piezoelectric (uses mechanical motion / pressure / vibration)

2. Power management  
   - Rectifier / regulator to turn raw harvested energy into something usable

3. Energy storage  
   - Thin-film rechargeable cell or capacitor

4. Sensor + microcontroller  
   - Ultra-low-power sensing loop runs continuously
   - Microcontroller sleeps most of the time to save power

5. Data transmit burst  
   - Send data wirelessly in short bursts instead of streaming 24/7

This architecture is how you make an actually possible self-powered implant. The point is not to be “always on radio.” The point is to avoid repeated surgery.

## Repository structure

```text
Self-powered-Implantable-Medical-Device/
│
├── README.md                <- project overview (this file)
├── LICENSE                  <- license terms (MIT for now)
├── .gitignore               <- ignore Python/OS clutter
│
├── code/
│   ├── energy_model.py      <- thermoelectric model (body heat harvesting)
│   └── piezo_model.py       <- piezoelectric model (motion / pressure harvesting)
│
└── docs/
    └── power_budget.md      <- can harvested energy actually run an implant?
---

## ⚡ Current Progress

- ✅ Thermoelectric model implemented (`energy_model.py`)
- ✅ Piezoelectric model implemented (`piezo_model.py`)
- ✅ Power budget feasibility documented (`docs/power_budget.md`)
- ⏳ Next: integrate both harvesters and simulate combined output (`integrated_model.py` coming soon)

---

## 🧠 Author

**Abdullah Haydar (2025)**  
Biomedical Engineering / Electrical Systems  
[GitHub: abdullah-EE](https://github.com/abdullah-EE)

---

## 📜 License

This project is open source under the MIT License.  
Feel free to reference or build upon it with credit.
