# Day 04 – Quantum Entanglement

## Overview

Quantum entanglement is one of the most fascinating concepts in quantum computing. It describes a situation where two or more qubits become correlated in such a way that the state of one qubit is directly related to the state of the other, regardless of the distance between them.

Unlike classical systems, entangled qubits cannot always be described independently. Instead, they share a single quantum state.

---

# What is Quantum Entanglement?

Quantum entanglement is a quantum phenomenon in which multiple qubits become linked together.

When qubits are entangled:

* The state of one qubit depends on the state of another.
* Measuring one qubit immediately determines the correlated state of the other.
* The qubits behave as a single quantum system.

---

# Why is Entanglement Important?

Entanglement provides computational capabilities that are impossible with classical computers.

It is a fundamental resource for:

* Quantum algorithms
* Quantum teleportation
* Quantum cryptography
* Quantum error correction
* Quantum communication

Without entanglement, many quantum advantages would not exist.

---

# Creating Entanglement

Entanglement is commonly created using two quantum gates:

1. **Hadamard (H) Gate**

   * Creates a superposition.

2. **Controlled-NOT (CNOT) Gate**

   * Correlates two qubits to produce an entangled state.

Example circuit:

```text
|0⟩ ── H ──●──
           │
|0⟩ ───────X──
```

This produces one of the Bell States.

---

# Bell State Example

Starting state:

```text
|00⟩
```

Apply Hadamard to the first qubit:

```text
(|00⟩ + |10⟩)/√2
```

Apply CNOT:

```text
(|00⟩ + |11⟩)/√2
```

This is an entangled state.

---

# What Happens During Measurement?

Suppose the entangled state is:

```text
(|00⟩ + |11⟩)/√2
```

Possible measurement outcomes:

* 00 (50%)
* 11 (50%)

Impossible outcomes:

* 01
* 10

The measurement of one qubit determines the correlated outcome of the other.

---

# Correlation vs Classical Correlation

## Classical Correlation

Two objects may be related because they were prepared that way.

Example:

* Two identical gloves
* Seeing the left glove tells you the other is the right glove.

## Quantum Entanglement

The relationship exists as part of the shared quantum state until measurement.

The qubits behave as one quantum system rather than two independent objects.

---

# Real-World Analogy

Imagine two perfectly synchronized magic coins.

Whenever you flip them:

* If one shows Heads, the other also shows Heads.
* If one shows Tails, the other also shows Tails.

Although this is only an analogy, it helps visualize quantum correlation.

---

# Applications of Entanglement

* Quantum Teleportation
* Quantum Key Distribution (QKD)
* Quantum Error Correction
* Grover's Search Algorithm
* Shor's Factoring Algorithm
* Distributed Quantum Computing

---

# Key Concepts

| Concept      | Description                         |
| ------------ | ----------------------------------- |
| Entanglement | Correlation between multiple qubits |
| Bell State   | Simplest entangled quantum state    |
| H Gate       | Creates superposition               |
| CNOT Gate    | Creates entanglement                |
| Measurement  | Produces correlated outcomes        |

---

# Common Beginner Misconceptions

### ❌ Entangled qubits communicate faster than light.

✅ They do not send information instantly. They only exhibit quantum correlations.

---

### ❌ Entangled qubits always have opposite values.

✅ They can have the same or opposite correlations depending on the entangled state.

---

### ❌ Entanglement means two qubits become physically connected.

✅ Entanglement is a relationship between quantum states, not a physical connection.

---

# Key Takeaways

* Quantum entanglement links two or more qubits into a shared quantum state.
* Measuring one entangled qubit affects the overall quantum state and determines correlated outcomes.
* Entanglement is created using gates such as Hadamard (H) and CNOT.
* Bell States are the simplest examples of entangled states.
* Entanglement is essential for quantum communication, cryptography, teleportation, and many quantum algorithms.

---

# Day 04 Summary

```text
Two Qubits
      ↓
Apply H Gate
      ↓
Create Superposition
      ↓
Apply CNOT Gate
      ↓
Entangled State
      ↓
Measure
      ↓
Correlated Classical Results
```

**Next Topic:** Quantum Gates (X, Y, Z, and Hadamard Gates) – understanding how quantum states are manipulated.
