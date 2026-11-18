## Dual-Aircraft Flight Telemetry Analysis -  Findings (`usaf-refueling-scenario`)

**Source Datasets:** `nhamby/opentdf-memo-demo`
- `usaf-refueling-scenario/c-17-flight-log-data.csv` (Receiver aircraft, 25 samples across Approach, Pre-Contact, Contact Established, and Fuel Transfer)
- `usaf-refueling-scenario/kc-46-flight-log-data.csv` (Tanker aircraft, 93 samples across full refueling track)

---

### 1. Receiver Aircraft Findings (`c-17-flight-log-data.csv`)

- **Classical Limit Alerts vs. Stabilized Formation State (`t000` – `t024`):** Standard static limit checks immediately flag `AIRSPEED IAS` (268–270 KIAS) and `ALTITUDE SL` (24,950–25,000 ft) as red limit exceedances while leaving the remaining 34 channels nominal green. Cross-channel behavioral analysis confirms a fully stabilized tanker-formation cruise profile (`Roll = 0.0°`, `Pitch = 1.5°`, `AOA = 3.1°`) with zero actual flight-control faults.
- **Approach-to-Contact Coupling Stabilization (`t000` → `t010`):** During the transition from initial tanker approach (`14:08:00`) through pre-contact positioning to receptacle engagement (`Contact Established` at `14:10:20`), global cross-channel stability rises steadily from **33.49%** (14 active subsystem interactions) to **44.42%** (49 active interactions) as altitude and airspeed lock onto the tanker boom envelope.
- **Peak Mass-Transfer Compensation (`t020`):** During active fuel transfer (`Receiving`, fuel mass increasing from `44,750 lbs` past `50,083 lbs` at constant `25,000 ft` and `270 KIAS`), cross-channel dynamic compensation reaches its peak (**0.9463** at `t020`, global stability **47.30%** across **59 active couplings**), reflecting continuous trim and attitude compensation against increasing aircraft gross weight while attitude angles remain held flat.
- **Highest Dynamic Control Channels (C-17):** Roll Rate (`RATE P`, control weight `0.8708`), Longitudinal Load (`G-LOAD X`, `0.4351`), and Pitch Attitude (`PITCH THETA`, `0.3822`).

---

### 2. Tanker Aircraft Findings (`kc-46-flight-log-data.csv`)

- **Sustained Boom-Track Subsystem Coupling (`t000` – `t092`):** Across all 93 samples, cross-channel coupling expands continuously from **14 active interactions** (`t000`, global stability **33.50%**) to **90 active interactions** by `t090` (global stability **36.63%**, peak **47.25%** at `t020`), reflecting tightly coupled station-keeping throughout the refueling track.
- **Early Trajectory Stabilization Peak (`t006`):** Unlike the receiver aircraft (whose peak compensation occurs during late-stage fuel weight gain at `t020`), the tanker reaches its peak cross-channel adjustment earlier at **`t006`** (**0.9341**) while establishing the steady refueling track.
- **Highest Dynamic Control Channels (KC-46):** Outside Air Temperature baseline (`OAT TEMP`, control weight `0.8152`), Fuel Feed (`ENG 1 FUEL`, `0.4699`), Hydraulic System A (`HYD PRESS A`, `0.3670` — supporting boom/refueling actuation), and Yaw Trim (`TRIM YAW`, `0.3097`).
