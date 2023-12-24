import cirq
import numpy as np

def inverse_fourier_transform(qubits):
    n = len(qubits)
    circuit = cirq.Circuit()

    # Apply Hadamard gates
    for i in range(n):
        circuit.append(cirq.H(qubits[i]))

    # Apply controlled-phase gates
    for control_qubit in range(n):
        for target_qubit in range(control_qubit + 1, n):
            angle = 2.0 * np.pi / (2 ** (target_qubit - control_qubit + 1))
            circuit.append(cirq.CZ(qubits[control_qubit], qubits[target_qubit]) ** angle)

    # Swap qubits
    for i in range(n // 2):
        circuit.append(cirq.SWAP(qubits[i], qubits[n - i - 1]))

    return circuit

# Шаг 1: Создание входного состояния
input_state = np.array([1, 0, 0, 0])  # Пример: состояние |0000⟩
qubits = cirq.LineQubit.range(len(input_state))

# Подготовка входного состояния
circuit_input = cirq.Circuit()
for i, bit in enumerate(input_state):
    if bit:
        circuit_input.append(cirq.X(qubits[i]))

# Шаг 2: Применение обратного преобразования Фурье
circuit_transform = inverse_fourier_transform(qubits)

# Шаг 3: Измерение результатов
simulator = cirq.Simulator()
result = simulator.simulate(circuit_input + circuit_transform)

# Шаг 4: Анализ результатов
output_state = result.final_state_vector
print("Входное состояние:", input_state)
print("Выходное состояние после обратного преобразования Фурье:", output_state)
