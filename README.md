# attitude-gnc

Attitude determination and control for a small satellite, written in Python and built step by step.

> **Status: early development, step 1 of 7.** The repository currently contains a tested scalar Kalman filter. Everything else is listed in the [Roadmap](#roadmap) and does not exist yet.

## What is in this repository

| File | Content |
|---|---|
| `src/attitude_gnc/kalman_scalar.py` | `predict` and `update` for a Kalman filter with one state and one measurement |
| `tests/test_kalman_scalar.py` | Tests of the variance recursion against closed-form results |

## What the tests verify

- **Constant state** (`a = 1`, `q = 0`): after `n` updates, the variance matches `1/P_n = 1/P_0 + n/r`.
- **Random-walk state** (`a = 1`, `q = 0.01`, `r = 0.25`): after 10,000 cycles from `P_0 = 1000`, the prior variance matches the positive root of `P^2 - q P - q r = 0`.

## Reproduce

Requires [uv](https://docs.astral.sh/uv/). Python 3.14 or later is required.

```
git clone https://github.com/thomaslemoinecode/attitude-gnc.git
cd attitude-gnc
uv sync
uv run pytest -v
uv run ruff check
```

## Limitations

- The filter handles a single scalar state. There is no attitude representation in the code yet.
- The tests cover the variance recursion only. The state estimate is not tested yet: a Monte Carlo consistency test is the next step.
- No sensor data is used yet, and the repository contains no dataset.

## Roadmap

1. **Inertial estimation (in progress).** Monte Carlo consistency test. Allan variance on static IMU data (TUM VI). A 3-state tilt Kalman filter, validated against optical ground truth (BROAD) and compared with a complementary filter. Figures and a technical note.
2. **Kinematics and dynamics.** Quaternion kinematics, rigid-body dynamics, justified numerical integration, 3D attitude animation.
3. **Sensor models on real references.** Orbit from CelesTrak TLEs propagated with SGP4, Sun direction, IGRF magnetic field, star tracker based on the Hipparcos catalogue.
4. **Static attitude determination.** TRIAD, then QUEST.
5. **Multiplicative extended Kalman filter (MEKF)**, with the gyro bias in the state.
6. **Attitude control.** Lyapunov-based control law on the quaternion error, reaction wheels with saturation, Monte Carlo campaign, pointing error budget.
7. **Cross-validation** against Basilisk.

## References

- R. E. Kalman. A New Approach to Linear Filtering and Prediction Problems. *Journal of Basic Engineering*, 82(1), 35–45, 1960.

Planned for later steps:

- D. Schubert et al. The TUM VI Benchmark for Evaluating Visual-Inertial Odometry. *IROS*, 1680–1687, 2018. Dataset under CC BY 4.0.
- D. Laidig, M. Caruso, A. Cereatti, T. Seel. BROAD – A Benchmark for Robust Inertial Orientation Estimation. *Data*, 6(7), 72, 2021. Dataset under CC BY 4.0.
- E. J. Lefferts, F. L. Markley, M. D. Shuster. Kalman Filtering for Spacecraft Attitude Estimation. *Journal of Guidance, Control, and Dynamics*, 5(5), 417–429, 1982.