import cirq

# 1. Define two physical qubits on a grid
q0, q1 = cirq.GridQubit(0, 0), cirq.GridQubit(0, 1)

# 2. Create a quantum circuit container
circuit = cirq.Circuit()

# 3. Apply the logic gates to create entanglement
circuit.append(cirq.H(q0))      # Puts qubit 0 into a 0 and 1 split (Superposition)
circuit.append(cirq.CNOT(q0, q1)) # Entangles qubit 1 to qubit 0

# 4. Measure both qubits to get the final data
circuit.append(cirq.measure(q0, q1, key='result'))

# 5. Simulate the circuit locally on your machine 100 times
simulator = cirq.Simulator()
output = simulator.run(circuit, repetitions=100)

print("Your Quantum Circuit Architecture:")
print(circuit)
print("\nSimulation Output (Should strictly show 00 or 11 combinations):")
print(output.histogram(key='result'))
