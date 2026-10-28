# Trophic Cascade — Numerical Simulation

Numerical simulation of a five-compartment trophic cascade (vegetation, elk/moose, deer, wolves, and bears), modeled using a system of nonlinear, non-autonomous ordinary differential equations (ODEs).

## Project Structure

- `constante.py` — Model parameters
- `f.py` — System of differential equations
- `euler_explicite.py`, `euler_implicite.py`, `runge_kutta.py` — Different numerical methods for solving differential equations
- `main.py` — Simulation and visualization of results

## Implemented Numerical Methods

- **Explicit Euler** — First-order method; simple but conditionally stable.
- **Implicit Euler** — Stable method, solved at each time step using Newton's method.
- **Runge–Kutta 4 (RK4)** — Fourth-order method.

## Requirements

- Python
- NumPy
- Matplotlib

Install the required libraries using pip:

```bash
pip install numpy matplotlib
```

## Authors

Thaddée · Rémi · Hafssa · Malek

