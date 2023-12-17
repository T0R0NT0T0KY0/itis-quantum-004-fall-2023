import cirq
from cirq import sim

def xor_oracle(qubits):
    circuit = cirq.Circuit()

    circuit.append(cirq.X(qubits[0]))
    circuit.append(cirq.X(qubits[1]))
    circuit.append(cirq.X(qubits[2]))

    circuit.append(cirq.CCX(qubits[0], qubits[1], qubits[3]))
    circuit.append(cirq.CX(qubits[2], qubits[3]))

    # Отменяем X-гейты на первых трёх кубитах
    circuit.append(cirq.X(qubits[0]))
    circuit.append(cirq.X(qubits[1]))
    circuit.append(cirq.X(qubits[2]))

    return circuit

# Создаем четыре кубита
qubits = cirq.LineQubit.range(4)

# Создаем схему и добавляем оракул
main_circuit = cirq.Circuit()
main_circuit.append(xor_oracle(qubits))

# Визуализируем схему
print("Circuit:")
print(main_circuit)

# Выводим легенду
print("\nЛегенда:")
print(f"{qubits[0]} - Входной кубит 1 (x1)")
print(f"{qubits[1]} - Входной кубит 2 (x2)")
print(f"{qubits[2]} - Входной кубит 3 (x3)")
print(f"{qubits[3]} - Выходной кубит (Результат f(x1, x2, x3))")