import cirq

# https://quantum.gltronred.info/quirk/quirk.html#circuit={%22cols%22:[[%22X%22,1,%22X%22,%22X%22],[%22%E2%80%A2%22,%22%E2%80%A2%22,1,1,%22X%22],[1,1,%22%E2%80%A2%22,%22%E2%80%A2%22,1,%22X%22],[1,1,1,1,%22%E2%80%A2%22,%22%E2%80%A2%22,%22X%22]],%22init%22:[0,1]}
def oracle():
    qubits = cirq.LineQubit.range(7)
    circuit = cirq.Circuit()
    circuit.append(cirq.X(qubits[0]))
    circuit.append(cirq.X(qubits[2]))
    circuit.append(cirq.X(qubits[3]))

    circuit.append(cirq.CCX(qubits[0], qubits[1], qubits[4]))
    circuit.append(cirq.CCX(qubits[2], qubits[3], qubits[5]))
    circuit.append(cirq.CCX(qubits[4], qubits[5], qubits[6]))

    print(circuit)

    return circuit

import cirq

def grover_algorithm(oracle):
    qubits = cirq.LineQubit.range(7)
    circuit = cirq.Circuit()

    # Инициализация суперпозиции
    circuit.append(cirq.H.on_each(qubits))

    num_iterations = 1

    for _ in range(num_iterations):
        # Применение оракула
        circuit.append(oracle)

        # Амплификация
        circuit.append(cirq.H(qubits[4]))
        circuit.append(cirq.X(qubits[4]))
        circuit.append(cirq.H(qubits[5]))
        circuit.append(cirq.X(qubits[5]))
        circuit.append(cirq.H(qubits[6]))
        circuit.append(cirq.X(qubits[6]))
        circuit.append(cirq.CCX(qubits[4], qubits[5], qubits[6]))
        circuit.append(cirq.H(qubits[6]))
        circuit.append(cirq.X(qubits[6]))
        circuit.append(cirq.H(qubits[5]))
        circuit.append(cirq.X(qubits[5]))
        circuit.append(cirq.H(qubits[4]))
        circuit.append(cirq.X(qubits[4]))

        # Обратное применение оракула
        circuit.append(oracle**-1)

        # Амплификация
        circuit.append(cirq.H.on_each(qubits[4:7]))
        circuit.append(cirq.X.on_each(qubits[4:7]))
        circuit.append(cirq.H(qubits[6]))
        circuit.append(cirq.CCX(qubits[4], qubits[5], qubits[6]))
        circuit.append(cirq.H(qubits[6]))
        circuit.append(cirq.X.on_each(qubits[4:7]))
        circuit.append(cirq.H.on_each(qubits[4:7]))

    # Измерение
    circuit.append(cirq.measure(*qubits[4:7], key='result'))

    return circuit


circuit = oracle()

sim = cirq.Simulator()
r = sim.simulate(circuit)
print(r)

# 2

# Создание оракула
oracle_circuit = oracle()

# Создание и запуск алгоритма Гровера
grover_circuit = grover_algorithm(oracle_circuit)

# Симуляция
simulator = cirq.Simulator()
result = simulator.run(grover_circuit, repetitions=1)

# Вывод результатов
print("Measurement outcome:", result.measurements['result'])