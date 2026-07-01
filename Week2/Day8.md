# Day 08 – Understanding Qiskit Architecture

## Overview

Today I explored the architecture behind Qiskit and learned how a quantum program travels from Python code to a real quantum computer.

Instead of focusing on writing circuits, I studied how Qiskit acts as a bridge between classical programming and quantum hardware, along with the responsibilities of the transpiler and backend.

---

## Learning Objectives

- Understand why Qiskit is required
- Learn what a Quantum SDK is
- Study the Qiskit workflow
- Explore Qiskit's architecture
- Understand the purpose of the transpiler
- Compare simulators with real quantum computers
- Learn IBM Quantum Platform components

---

## Why Do We Need Qiskit?

Just like we write applications in Python instead of machine language, we cannot directly communicate with a quantum processor.

Qiskit converts our Python-based quantum programs into instructions that quantum hardware understands.

Qiskit is IBM's open-source Software Development Kit (SDK) for quantum computing.

---

## What Can Qiskit Do?

Qiskit enables developers to:

- Create quantum circuits
- Apply quantum gates
- Simulate quantum circuits
- Execute circuits on real quantum computers
- Visualize quantum results
- Analyze measurement outcomes

---

## Quantum Computing Workflow

```text
Python Code
      │
      ▼
Quantum Circuit
      │
      ▼
Qiskit SDK
      │
      ▼
Transpiler
      │
      ▼
Backend
      │
      ▼
Measurement
      │
      ▼
Visualization
```

---

## Qiskit Architecture

### Layer 1
Python Code

The quantum program starts as normal Python code.

---

### Layer 2
Qiskit SDK

Provides tools for creating circuits, quantum gates, simulation, visualization, and execution.

---

### Layer 3
Transpiler

Optimizes and converts circuits into a form supported by the selected quantum hardware.

---

### Layer 4
Backend

Can be either:

- Quantum Simulator
- Real Quantum Computer

The backend executes the quantum circuit.

---

### Layer 5
Results

Returns measurement counts and execution statistics for analysis.

---

## Purpose of the Transpiler

The transpiler performs several important tasks:

- Optimizes quantum circuits
- Removes unnecessary gates
- Converts unsupported gates into supported ones
- Matches hardware connectivity
- Improves execution efficiency

Without transpilation, many circuits cannot run efficiently on quantum hardware.

---

## Simulator vs Real Quantum Computer

| Simulator | Real Quantum Computer |
|-----------|-----------------------|
| Runs on classical hardware | Uses physical qubits |
| Fast execution | Slower execution |
| Free to use | Queue time required |
| No quantum noise | Affected by quantum noise |
| Best for learning | Best for real experiments |

---

## IBM Quantum Platform Provides

- Quantum Simulators
- Real Quantum Computers
- Circuit Composer
- Job Management
- Result Visualization
- Learning Resources

---

## Key Takeaways

- Qiskit acts as the bridge between Python and quantum hardware.
- Quantum programs pass through multiple layers before execution.
- The transpiler adapts and optimizes circuits for different quantum devices.
- Simulators are ideal for learning, while real quantum computers introduce hardware limitations and quantum noise.
- Understanding the architecture helps explain what happens behind the scenes during quantum circuit execution.

---

## What I Learned

Today helped me understand that writing a quantum circuit is only one part of quantum programming.

Behind every execution, Qiskit optimizes the circuit, prepares it for compatible hardware, sends it to a backend, and returns measurement results for analysis.

Learning this workflow gave me a much clearer understanding of how modern quantum software interacts with real quantum processors.

---

## Resources

- IBM Quantum Learning
- Qiskit Documentation
- IBM Quantum Platform
- Qiskit SDK Documentation

---

**Day 08 Completed ✅**