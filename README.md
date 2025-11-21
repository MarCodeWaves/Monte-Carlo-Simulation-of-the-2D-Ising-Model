**Monte-Carlo Simulation of the 2D Ising Model**


This repository contains the implementation and analysis of the 2D Ising Model using the Monte Carlo (MC) Metropolis Algorithm. The primary goal of the project was to simulate the magnetic phase transition in a 2D lattice, accurately determining key thermodynamic properties—specifically the magnetization ($M$)—as a function of temperature ($T$), focusing on the behavior near the critical temperature $T^*$.

**Methodology**

Model Parameters:

- Lattice Size: Simulations were performed primarily on $L \times L = 10 \times 10$ and $L \times L = 80 \times 80$ lattices.

- Algorithm: Metropolis Algorithm was utilized to evolve the system state (spin configurations).

- Critical Temperature: The known critical temperature for the 2D Ising model (in the thermodynamic limit) is $T^* \approx 2.269$.

- Boundary Conditions: Periodic boundary conditions were used to minimize finite-size effects.

**Analysis Focus**
The analysis concentrated on:

- Spin Configurations: Visualization of the lattice state for temperatures below, at, and above $T^*$.

- Thermalization Time: Determining the minimum number of Monte Carlo Steps (MCS) required for the system to reach equilibrium.

- Critical Behavior: Detailed examination of the system's properties in the vicinity of the critical point.

**Key Results and Findings**

The simulation successfully replicated the behavior of the Ising model, validating the implementation of the Metropolis algorithm.

Phase Transition: The sharp drop in magnetization confirmed the existence of a phase transition from the ferromagnetic ordered state ($M \approx 1$) to the paramagnetic disordered state ($M \approx 0$).

Thermodynamic Quantities: Calculation of magnetization ($M$) as a function of temperature $T$, with results presented as averages over time and averages over the ensemble.

Trajectory Analysis: Individual Monte Carlo trajectories were analyzed for different temperatures to confirm the transition behavior:

For $T < T^*$: Rapid relaxation to the ordered state.

For $T \approx T^*$: Significant increase in fluctuations and thermalization time (critical slowing down).

For $T > T^*$: Rapid relaxation to the disordered state.

Documentation

Detailed theoretical background, code implementation, and full results analysis (including figures showing magnetization curves and spin configurations) are available in the project report:

IsingMC_report.pdf
