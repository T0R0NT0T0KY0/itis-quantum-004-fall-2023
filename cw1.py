import cirq

qubits = cirq.LineQubit.range(4)

circuit = cirq.Circuit()
circuit.append(cirq.CNOT(qubits[0], qubits[2]))
circuit.append(cirq.CNOT(qubits[1], qubits[3]))
circuit.append(cirq.X(qubits[3]))
circuit.append(cirq.CNOT(qubits[1], qubits[2]))

# Визуализируем схему
print("Result:")
print(circuit)

sim = cirq.Simulator()
r = sim.simulate(circuit)
print(r)