import cirq
import numpy as np


def phase_estimation(U, psi, n, Nreps):
    """
    Реализация алгоритма оценки фазы.

    Параметры:
    U (cirq.Gate): Унитарный оператор, для которого проводится оценка фазы.
    psi (numpy.ndarray): Входное состояние.
    n (int): Количество битов для оценки фазы.
    Nreps (int): Количество повторений алгоритма.

    Возвращает:
    None: Выводит оценку фазы для каждого повторения на экран.
    """

    # Инициализация квантовой схемы
    circuit = cirq.Circuit()

    # Инициализация кубитов
    qubits = cirq.LineQubit.range(n + 1)

    # Применение оператора U controlled
    circuit.append(U.on(qubits[n]).controlled_by(*qubits[0:n]))

    # Обратное преобразование Фурье
    circuit.append(cirq.inverse(cirq.qft(*qubits[0:n], without_reverse=True)))

    # Измерение
    circuit.append(cirq.measure(*qubits[0:n], key='result'))

    # Выполнение Nreps повторений
    for _ in range(Nreps):
        # Запуск симулятора
        simulator = cirq.Simulator()
        result = simulator.run(circuit, repetitions=1)

        # Получение оценки фазы из результатов измерений
        binary_str = result.measurements['result'][0]
        theta = np.sum([int(bit) * 2 ** (n - i - 1) for i, bit in enumerate(binary_str)]) / 2 ** n

        print(f"Оценка фазы (в десятичной форме): {theta}")


# Пример использования
# Задайте свой оператор U, состояние psi, количество битов n и количество повторений Nreps
U = cirq.X  # Пример: оператор X (NOT)
psi = np.array([1, 0])  # Пример: состояние |0⟩
n = 7  # Количество битов
Nreps = 13  # Количество повторений

phase_estimation(U, psi, n, Nreps)
