# Day 02 – Bits, Qubits and Quantum States

## Importance of Bits

* Every computer works using information
* Classical computers use **bits**
* Quantum computers use **qubits**

---

## What is a Bit?

* A bit is the **smallest unit of information** in a classical computer
* It can have only **one value at a time**
* Values: **0 or 1**

### Example:

Light Switch Model

```
OFF  -------->  0
ON   -------->  1

State = Only ONE at a time
```

---

## How Bits Work

```
Number of Bits    Possible Values
--------------------------------
1 bit             2 (0,1)
2 bits            4 (00,01,10,11)
3 bits            8
8 bits            256
```

* More bits → more combinations
* Everything in a computer is built using bits

---

## What is a Qubit?

* A qubit is the **basic unit of quantum computing**
* It can exist in:

  * 0
  * 1
  * **Both at the same time**

---

## Superposition (Core Idea)

### Bit:

```
[ 0 ]  OR  [ 1 ]
```

### Qubit:

```
[ 0 ] + [ 1 ]  (at same time)
```

---

## Spinning Coin Example

```
Before Measurement:

   (Spinning Coin)
      ↻
   Heads + Tails

After Measurement:

   Heads   OR   Tails
```

* Before → multiple possibilities
* After → one fixed result

---

## Power of Qubits

```
Qubits        Possible States
-----------------------------
1             2
2             4
3             8
10            1024
```

➡ Growth is exponential → this is why quantum is powerful

---

## Real Qubits (Hardware)

Qubits are physically created using:

* Superconducting circuits
* Trapped ions
* Photons
* Atoms

```
Real System → Qubit → Computation
```

* IBM uses **superconducting qubits**

---

## Quantum State

* A quantum state describes the **full condition of a qubit**
* It stores **probabilities**

### Instead of:

```
0 or 1
```

### We use:

```
P(0) = probability of 0
P(1) = probability of 1
```

---

## Representation (Ket Notation)

```
|0⟩  → State 0
|1⟩  → State 1
```

---

## Measurement Process

```
Before Measurement:
   |ψ⟩ = a|0⟩ + b|1⟩
   (multiple possibilities)

        ↓ Measure

After Measurement:
   |0⟩  OR  |1⟩
   (single result)
```

➡ This is called **State Collapse**

---

## Bits vs Qubits

```
Feature        Bit              Qubit
-----------------------------------------
Values         0 or 1           0,1 or both
Type           Fixed            Probabilistic
Power          Limited          Very Powerful
Measurement    No change        State changes
```

---

## Visual Understanding

Compass Analogy:

```
Bit:
   ↑ (Only one direction)

Qubit:
   ↗ ↑ ↖ → ↘ ↓ ↙
   (Many possible directions)
```

---

## Summary

* Bits store **fixed information**
* Qubits store **probabilities**
* Quantum computing grows **exponentially**
* Measurement collapses quantum state to a single value

---

✔ Day 02 Completed – Understanding Quantum Information Basics
