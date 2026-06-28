

```markdown
# Day 06 - Quantum Gates

## Overview

Quantum gates are the fundamental building blocks of quantum computation. Similar to how classical logic gates manipulate bits, quantum gates manipulate qubits by changing their quantum states.

Unlike classical gates, quantum gates are **reversible**, meaning every gate has an inverse operation that preserves quantum information.

---

# Classical Gates vs Quantum Gates

| Classical Gates | Quantum Gates |
|-----------------|---------------|
| Operate on bits | Operate on qubits |
| Perform logical operations | Transform quantum states |
| Inputs are only 0 or 1 | Input can be any valid quantum state |
| Examples: AND, OR, NOT | Examples: X, Y, Z, H |

---

# Important Property

Quantum gates are **reversible**.

- Every gate has an inverse operation.
- Quantum information is preserved.
- Unlike many classical operations, information is never discarded.

---

# X Gate (Quantum NOT Gate)

## Purpose

The X Gate is the quantum equivalent of the classical NOT gate.

### Operation

```

|0⟩ → |1⟩

|1⟩ → |0⟩

```

### Bloch Sphere

- Rotates the qubit **180° around the X-axis**.
- Swaps the North and South poles.

### Key Points

- Flips basis states
- Quantum NOT gate
- Works on any quantum state

---

# Y Gate

## Purpose

The Y Gate performs two operations simultaneously:

- Flips the qubit
- Changes its phase

Example:

```

|0⟩
↓
Y
↓
i|1⟩

```

The imaginary number **i** represents a phase change.

### Bloch Sphere

- Rotates the qubit **180° around the Y-axis**

---

# Z Gate

## Purpose

Unlike the X Gate, the Z Gate does **not** swap basis states.

Instead it changes only the phase.

### Operation

```

|0⟩ → |0⟩

|1⟩ → -|1⟩

```

Only the sign changes.

### Why It Matters

Although measurement probabilities remain unchanged, the phase affects later quantum operations.

This enables **quantum interference**, which is essential for quantum algorithms.

### Bloch Sphere

- Rotates the qubit **180° around the Z-axis**

---

# Hadamard (H) Gate

The Hadamard Gate is one of the most important quantum gates.

Its primary purpose is to create **equal superposition**.

### Operation

Starting with:

```

|0⟩

```

Applying H gives:

```

(|0⟩ + |1⟩)/√2

```

Starting with:

```

|1⟩

```

Applying H gives:

```

(|0⟩ - |1⟩)/√2

```

The second state differs only by its phase.

### Bloch Sphere

The H Gate moves the qubit from the **Z-axis toward the X-axis**, creating an equal superposition.

---

# Why the H Gate is Important

Many quantum algorithms begin by creating superposition using the Hadamard Gate.

Examples include:

- Grover's Algorithm
- Deutsch–Jozsa Algorithm
- Shor's Algorithm
- Quantum Fourier Transform (QFT)

---

# Gate Comparison

| Gate | Main Action | Rotation | Phase Change |
|------|-------------|----------|--------------|
| X | Flips basis states | 180° around X-axis | No |
| Y | Flip + Phase | 180° around Y-axis | Yes |
| Z | Phase Flip | 180° around Z-axis | Yes |
| H | Creates Superposition | Towards X-axis | Yes |

---

# Key Takeaways

- Quantum gates manipulate qubits instead of classical bits.
- All quantum gates are reversible.
- X Gate flips basis states.
- Y Gate flips the state and changes its phase.
- Z Gate changes only the phase.
- Hadamard Gate creates equal superposition.
- Many quantum algorithms begin with the H Gate.
- Bloch Sphere rotations provide an intuitive visualization of how quantum gates transform qubits.

---

## Day 06 Summary

```

Quantum Gates

X → Flip

Y → Flip + Phase

Z → Phase Flip

H → Creates Superposition

All Quantum Gates are Reversible

Quantum Gates = Rotations on the Bloch Sphere

```

