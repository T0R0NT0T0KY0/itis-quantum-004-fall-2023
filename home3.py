import cirq


def addOneModFour():
    qubits = cirq.LineQubit.range(2)
    circuit = cirq.Circuit()
    circuit.append(cirq.CNOT(qubits[1], qubits[0]))
    circuit.append(cirq.X(qubits[1]))

    print("Result (+1, // 4):")
    print(circuit)

    sim = cirq.Simulator()
    r = sim.simulate(circuit)
    print(r)


def isEqualsTwo():
    qubits = cirq.LineQubit.range(3)
    circuit = cirq.Circuit()
    circuit.append(cirq.CNOT(qubits[0], qubits[1]))
    circuit.append(cirq.CCX(qubits[0], qubits[1], qubits[2]))

    print("Result (=== 2):")
    print(circuit)

    sim = cirq.Simulator()
    r = sim.simulate(circuit)
    print(r)


def grover_search(oracle, grover_circuit, num_iterations, qubits):
    for _ in range(num_iterations):
        grover_circuit.append(oracle)
        grover_circuit.append(cirq.H.on_each(qubits))
        grover_circuit.append(cirq.X.on_each(qubits))
        grover_circuit.append(cirq.H.on(qubits[1]))
        grover_circuit.append(cirq.CNOT(qubits[0], qubits[1]))
        grover_circuit.append(cirq.H.on(qubits[1]))
        grover_circuit.append(cirq.X.on_each(qubits))
        grover_circuit.append(cirq.H.on_each(qubits))
        grover_circuit.append(oracle)
        grover_circuit.append(cirq.H.on(qubits[1]))
        grover_circuit.append(cirq.CNOT(qubits[0], qubits[1]))
        grover_circuit.append(cirq.H.on(qubits[1]))
        grover_circuit.append(cirq.X.on_each(qubits))
        grover_circuit.append(cirq.H.on_each(qubits))

    return grover_circuit

# Определение оракула для уравнения x + 1 = 3
def oracle(circuit, qubits):
    # Инвертируем состояние, если x + 1 не равно 3
    circuit.append(cirq.X(qubits[0]))
    circuit.append(cirq.CCX(qubits[0], qubits[1], cirq.LineQubit(2)))
    circuit.append(cirq.X(qubits[0]))

def isEqualsTwoByGrover():
    qubits = [cirq.LineQubit(i) for i in range(2)]

    circuit = cirq.Circuit()

    circuit = grover_search(oracle=cirq.Circuit(), grover_circuit=circuit, num_iterations=1, qubits=qubits)

    circuit.append(cirq.measure(qubits[0], key='result'))

    simulator = cirq.Simulator()
    result = simulator.run(circuit, repetitions=1000)

    print("Результаты:", result.histogram(key='result'))


# оракул, который добавляет единицу к двухбитовому числу (по модулю 4);
addOneModFour()
print('------------')

# оракул, который по заданному двухбитовому x проверяет, что x+1 = 3;
isEqualsTwo()
print('------------')

# алгоритм Гровера для нахождения решения уравнения x+1 = 3, где x - двухбитовое число.
isEqualsTwoByGrover()