# Quantum Dev Portfolio

Small Python projects for learning and demonstrating core quantum-computing concepts through executable examples and visualisations.

## Projects

### Bloch sphere simulator

`bloch-sphere-simulator/`

Explores single-qubit state representation on the Bloch sphere using NumPy and Matplotlib.

Included examples:

- `bloch_one_qubit.py` — plots a qubit with `P(0)=0.75`, `P(1)=0.25` and configurable phase.
- `bloch_qubit_plot.py` — interactive Bloch-sphere visualisation with probability and phase controls.
- `z_gate_bloch.py` — compares a state before and after applying the Pauli-Z gate.

Setup:

```powershell
cd bloch-sphere-simulator
python -m venv venv-bloch
venv-bloch\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python bloch_one_qubit.py
```

### Bell states and teleportation

`bell-states/`

Contains a step-by-step Qiskit example that builds a Bell pair, prepares a source qubit, performs the teleportation measurements, and applies the conditional X/Z corrections.

Setup:

```powershell
cd bell-states
python -m venv venv-teleport
venv-teleport\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python teleportation.py
```

## Quantum concepts demonstrated

- qubit amplitudes and measurement probabilities;
- relative phase;
- Bloch-sphere coordinates;
- Pauli-Z rotation behaviour;
- Bell-pair entanglement;
- quantum teleportation with classical feed-forward corrections.

## Repository hygiene

Virtual environments and editor swap files are local-only and are not committed. Dependency files contain only the direct packages required by each project.

## Status

This is a learning portfolio rather than a production library. The scripts are intentionally small and explicit so the quantum operations remain easy to inspect.
