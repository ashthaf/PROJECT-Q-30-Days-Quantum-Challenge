# Day 05 – Quantum Measurement & State Collapse

## Overview

Quantum measurement is the process of extracting classical information from a qubit. Unlike classical bits, measuring a qubit changes its quantum state. Before measurement, a qubit may exist in a superposition of states. After measurement, it collapses to one definite classical state.

Understanding measurement is essential because every quantum algorithm eventually ends with a measurement that converts quantum information into classical data.

---

# Why Measurement is Special

A classical bit can be read without changing its value.

A quantum bit (qubit) behaves differently.

Before measurement:

* A qubit can exist in a superposition.
* Multiple possibilities coexist.

After measurement:

* Only one classical outcome is observed.
* The original superposition disappears.

---

# What is Quantum Measurement?

Quantum measurement is the process of reading information from a qubit.

For a single qubit measured in the computational (Z) basis, the only possible outcomes are:

```
|0⟩

or

|1⟩
```

No other result is possible.

---

# Before vs After Measurement

Suppose the qubit is

```
|ψ⟩ = α|0⟩ + β|1⟩
```

Before measurement

```
Superposition
        ↓
   Measurement
        ↓
 |0⟩   or   |1⟩
```

After measurement, the superposition no longer exists.

---

# Probability of Measurement

The measurement outcome depends on the probability amplitudes.

Example:

```
(|0⟩ + |1⟩)/√2
```

Measurement probabilities:

```
P(|0⟩) = 50%

P(|1⟩) = 50%
```

Running the experiment multiple times may produce:

```
Run 1 → |0⟩

Run 2 → |1⟩

Run 3 → |0⟩

Run 4 → |1⟩
```

Individual results are random, but many measurements follow the expected probability distribution.

---

# State Collapse

State collapse is the transition from a quantum superposition to a single definite state after measurement.

```
Superposition
      ↓
 Measurement
      ↓
|0⟩ or |1⟩
```

Example:

```
(|0⟩ + |1⟩)/√2
```

If measurement gives

```
|0⟩
```

the qubit immediately becomes

```
|0⟩
```

Likewise, if the outcome is

```
|1⟩
```

the new state becomes

```
|1⟩
```

The superposition is lost.

---

# Measuring Again

Suppose the first measurement gives

```
|0⟩
```

Measuring immediately again gives

```
|0⟩
```

every time.

Why?

Because the state has already collapsed.

There is no remaining superposition.

---

# Measurement is Irreversible

Once a quantum state is measured, its original superposition cannot be recovered from that measurement alone.

```
Quantum State
      ↓
 Measurement
      ↓
Collapsed State
```

The measurement permanently changes the quantum state.

---

# Why Quantum Algorithms Measure at the End

Quantum algorithms first manipulate qubits using quantum gates.

Only after all computations are complete is the qubit measured.

```
Initial State
      ↓
Quantum Gates
      ↓
New Quantum State
      ↓
Measurement
      ↓
Classical Output
```

Measuring too early collapses the state and destroys the quantum computation.

---

# Measurement in IBM Quantum

In IBM Quantum circuits, every execution ends with a **Measurement Gate**.

Without measurement:

* No classical output is produced.
* Results cannot be interpreted by classical computers.

---

# Measurement Statistics (Shots)

Quantum circuits are usually executed many times.

Each execution is called a **Shot**.

Example:

```
1000 Shots

Outcome    Count

0          506

1          494
```

More shots provide a better estimate of the true probability distribution.

---

# Common Beginner Misconceptions

### ❌ Measurement reveals a hidden value.

✅ Measurement produces an outcome based on the probability amplitudes of the quantum state.

---

### ❌ Measurement destroys the qubit.

✅ The qubit still exists.

Only its state changes to the measured basis state.

---

### ❌ Measuring twice gives different answers.

✅ If nothing changes between measurements, repeated measurements produce the same result because the state has already collapsed.

---

# Key Concepts

| Concept           | Meaning                                            |
| ----------------- | -------------------------------------------------- |
| Measurement       | Reading information from a qubit                   |
| Superposition     | Combination of multiple basis states               |
| Probability       | Likelihood of each measurement outcome             |
| State Collapse    | Transition to one definite state after measurement |
| Shots             | Repeated executions of the same circuit            |
| Measurement Basis | Basis used for measurement (commonly Z-basis)      |

---

# Real-World Analogy

Imagine taking a photograph.

Before taking the picture:

```
Person Moving
```

Click the camera

↓

```
One Frozen Frame
```

Similarly, a measurement captures one outcome from the quantum state according to its probability distribution.

---

# Key Takeaways

* Quantum measurement converts a qubit into a classical result.
* A qubit can exist in superposition before measurement.
* Measurement outcomes are probabilistic.
* Measurement causes state collapse.
* Repeated measurements after collapse give the same result.
* Quantum algorithms measure only after computation is complete.
* IBM Quantum circuits end with measurement gates.
* Multiple executions (**shots**) are used to estimate probabilities accurately.

---

# Day 05 Summary

```
Quantum Measurement

↓

Reads a Qubit

↓

Produces |0⟩ or |1⟩

↓

State Collapse

↓

Classical Output

↓

Repeated Executions (Shots)

↓

Probability Distribution
```

**Next Topic:** Quantum Gates – X, Y, Z, and Hadamard (H) Gates, Bloch Sphere Rotations, and State Transformations.
