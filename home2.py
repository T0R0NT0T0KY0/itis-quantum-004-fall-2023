import cirq

def balanced_oracle(qubits):
    circuit = cirq.Circuit()

    # Применяем X-гейты к первым трём кубитам
    circuit.append(cirq.X(qubits[0]))
    circuit.append(cirq.X(qubits[1]))
    circuit.append(cirq.X(qubits[2]))

    # Создаем контролируемый NOT (CX) гейт, где первые три кубита являются контролирующими,
    # а четвёртый – целевым
    circuit.append(cirq.CCX(qubits[0], qubits[1], qubits[3]))
    circuit.append(cirq.CX(qubits[2], qubits[3]))

    # Отменяем X-гейты на первых трёх кубитах
    circuit.append(cirq.X(qubits[0]))
    circuit.append(cirq.X(qubits[1]))
    circuit.append(cirq.X(qubits[2]))

    return circuit

def const_oracle(qubits):
    # Создаем схему, которая всегда применяет NOT к четвёртому кубиту
    circuit = cirq.Circuit(cirq.X(qubits[3]))
    return circuit

def run_deutsch_jozsa_algorithm(oracle):
    # Создаем четыре кубита
    qubits = cirq.LineQubit.range(4)

    # Создаем схему для алгоритма Дойча-Йожи
    dj_circuit = cirq.Circuit()

    # Применяем оператор Адамара к первым трём кубитам
    dj_circuit.append(cirq.H(q) for q in qubits[:-1])

    # Применяем оператор X к последнему кубиту
    dj_circuit.append(cirq.X(qubits[-1]))

    # Применяем оператор Адамара к последнему кубиту
    dj_circuit.append(cirq.H(qubits[-1]))

    # Применяем оракул
    dj_circuit.append(oracle(qubits))

    # Применяем оператор Адамара к первым трём кубитам
    dj_circuit.append(cirq.H(q) for q in qubits[:-1])

    # Измеряем первые три кубита
    dj_circuit.append(cirq.measure(*qubits[:-1], key='result'))

    # Запускаем симуляцию
    simulator = cirq.Simulator()
    result = simulator.run(dj_circuit)

    return result

# Создаем четыре кубита
qubits = cirq.LineQubit.range(4)

# Создаем схему для алгоритма Дойча-Йожи
dj_circuit = cirq.Circuit()

# Добавляем алгоритм Дойча-Йожи с балансированным оракулом
dj_circuit.append(balanced_oracle(qubits))

# Добавляем оракул с постоянной функцией
dj_circuit.append(const_oracle(qubits))

# Выводим схему
print(dj_circuit)

# Запускаем алгоритм с балансированным оракулом
balanced_result = run_deutsch_jozsa_algorithm(balanced_oracle)
print("Balanced Oracle Result:", balanced_result.measurements['result'])

# Запускаем алгоритм с оракулом постоянной функции
const_result = run_deutsch_jozsa_algorithm(const_oracle)
print("Constant Oracle Result:", const_result.measurements['result'])

