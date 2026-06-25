Based on your handwritten notes, here's a **GitHub-ready `README.md`** for **Day 03**. I've kept it clean, educational, and like a student's learning journal rather than something AI-generated.

---

# Day 03 – Qubit State Representation & Bloch Sphere

> **30 Days of Quantum Computing Learning Challenge**

## 📚 Topics Covered

* Quantum State Representation
* Quantum States
* Probability Amplitudes
* Normalization Condition
* Important Quantum States
* Quantum Computing Workflow
* Bloch Sphere
* Quantum Bases (X, Y & Z)
* Quantum Gates
* Limitations of the Bloch Sphere

---

# 1. State Representation

A classical bit can only exist in one of two states: **0** or **1**.

A **qubit**, however, is different. It can be in:

* **|0⟩**
* **|1⟩**
* A combination of both (**Superposition**)

The mathematical way of describing the exact condition of a qubit is called **Quantum State Representation**.

---

# 2. Quantum State

A quantum state contains all the information about a qubit before it is measured.

It is represented as:

[
|\psi\rangle = \alpha|0\rangle + \beta|1\rangle
]

Where

* **α** → amplitude of **|0⟩**
* **β** → amplitude of **|1⟩**

These values are called **Probability Amplitudes**.

---

# 3. Normalization Rule

The total probability of measuring a qubit must always equal **1**.

[
|\alpha|^2 + |\beta|^2 = 1
]

After measurement, the qubit always collapses to either:

* **0**
* **1**

There are no other possible outcomes.

---

# 4. Important Quantum States

### State 1

[
|\psi\rangle = |0\rangle
]

Probability

* 0 → **100%**
* 1 → **0%**

---

### State 2

[
|\psi\rangle = |1\rangle
]

Probability

* 0 → **0%**
* 1 → **100%**

---

### State 3 (Equal Superposition)

[
|\psi\rangle = \frac{|0\rangle + |1\rangle}{\sqrt2}
]

Probability

* 0 → **50%**
* 1 → **50%**

This is one of the most important states used in quantum computing.

---

# 5. How Quantum Computers Work

Unlike classical computers that process **bits**, quantum computers process **quantum states**.

Basic workflow:

```
Initial State
      ↓
 Quantum Gate
      ↓
  New State
      ↓
 Measurement
      ↓
    Result
```

Almost every quantum algorithm follows this process.

---

# 6. Bloch Sphere

The equation

[
|\psi\rangle = \alpha|0\rangle + \beta|1\rangle
]

is mathematically correct, but it is difficult to visualize.

To make understanding easier, scientists use the **Bloch Sphere**, which is a **3D representation of a single qubit**.

Think of it as **Google Maps for a qubit**.

Instead of reading equations, we can see the position of the qubit on a sphere.

### Important Positions

* **North Pole → |0⟩**
* **South Pole → |1⟩**
* **Any other point → Superposition**

---

# 7. Quantum Bases

A qubit can be represented using different bases depending on the operation being performed.

### Z Basis

* |0⟩
* |1⟩

Known as the **Computational Basis**.

---

### X Basis

* |+⟩
* |−⟩

Represents equal combinations of |0⟩ and |1⟩.

Commonly used in quantum algorithms.

---

### Y Basis

* |+i⟩
* |-i⟩

Represents quantum states with phase information.

---

# 8. Quantum Gates

In classical computers, logic gates change bits from **0 ↔ 1**.

Quantum gates work differently.

They **do not simply flip a qubit**.

Instead, they **rotate the qubit's state on the Bloch Sphere**, moving it to another quantum state.

Only after measurement does the qubit become either **0** or **1**.

---

# 9. Why the Bloch Sphere is Useful

The Bloch Sphere makes quantum computing easier to understand by visually showing:

* Superposition
* State changes
* Quantum gate operations
* Rotations
* Measurement outcomes

Instead of relying only on mathematical equations.

---

# 10. Limitation of the Bloch Sphere

The Bloch Sphere is designed for **only one qubit**.

When working with **two or more qubits**, especially **entangled qubits**, a single sphere cannot represent the complete quantum system.

In these cases, more advanced mathematical methods are required.

---

# 📝 Key Takeaways

* A qubit can exist in both **|0⟩** and **|1⟩** simultaneously.
* Quantum states are represented using **probability amplitudes**.
* Measurement collapses a qubit into either **0** or **1**.
* The **Bloch Sphere** provides a simple visual representation of a qubit.
* Quantum gates rotate qubits rather than simply flipping them.
* The Bloch Sphere is useful only for **single-qubit systems**.

---

## 🚀 Day 03 Complete

Today I moved beyond the basics of qubits and learned how quantum states are represented mathematically and visually. Understanding the **Bloch Sphere** made concepts like **superposition**, **quantum gates**, and **measurement** much easier to visualize. This was one of the most interesting topics so far in my **30 Days of Quantum Computing Learning Challenge**.

---

This format will look professional on GitHub while still reflecting that these are **your own study notes**, not copied documentation.
