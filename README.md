
## Frontier Quantum Architecture: Simulating Entanglement & Noise Mitigation
This repository contains proof of concept quantum circuit design using Google's open-source Cirq framework. The project creates a maximally entangled two-qubit state (Bell State) and simulates its execution on both an ideal quantum processor and a noisy quantum environment.
## 🛠️ The Core Architecture
To prove foundational quantum logic capabilities, this project constructs a circuit using two primary quantum operations to entangle two grid-mapped qubits ($q_0$ and $q_1$):

* Hadamard Gate ($H$): Acts on $q_0$ to transition it from a static classical state into a perfect 50/50 superposition of $\vert{}0\rangle$ and $\vert{}1\rangle$.
* Controlled-NOT Gate ($CNOT$): Uses $q_0$ as the control bit to conditionally flip $q_1$, securely entangling their quantum states.

q(0, 0): ───H───@───M('result')───
                │   │
q(0, 1): ───────X───M─────────────

## 🧠 Architectural Focus: Bugs vs. Noise
Unlike classical software engineering, where errors are purely logical bugs, the fundamental barrier in frontier quantum computing is environmental noise.
This repository targets noise mitigation by design:

   1. Gate Depth Optimization: The circuit minimizes the number of operations (gate depth). Shorter execution paths ensure calculations finish before thermal or electromagnetic fluctuations cause phase errors.
   2. Decoherence Prevention: By extracting data immediately after the $CNOT$ operation, the architecture beats the "decoherence clock," protecting fragile logical states from collapsing into scrambled data.

## 💻 Getting Started## Prerequisites
You need a standard python environment. Install Google Cirq via pip:

pip install cirq

## Execution
Run the core simulation script:

python bell_state.py

## 📊 Expected Output
When run on the ideal local simulator, the output yields perfectly correlated results, demonstrating that the qubits are fundamentally linked. You will strictly observe states 00 or 11 across iterations:

Simulation Output (Ideal State):
result=100100110011000011...
Histogram: Counter({0: 51, 3: 49})  # Where 0 represents '00' and 3 represents '11'
