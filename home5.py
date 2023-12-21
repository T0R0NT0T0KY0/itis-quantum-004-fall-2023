import cirq
import numpy as np

def shor_classical(n, Q, a, y):
    # Проверка, является ли yr/Q близким к целому
    if np.isclose(y * r / Q, round(y * r / Q)):
        # Если условие выполняется, начинаем факторизацию
        p = np.gcd(int(np.power(a, r // 2) + 1), n)
        q = np.gcd(int(np.power(a, r // 2) - 1), n)

        # Проверка найденных делителей
        if 1 < p < n and 1 < q < n and p * q == n:
            return p, q
        else:
            return "Перейдите к следующему a"
    else:
        return "Перейдите к следующему a"

# Пример использования
n = 15  # Число, которое требуется факторизовать
Q = 2   # Параметр Q
a = 7   # Выбор случайного a
y = 1   # Начальное значение y
r = 4   # Выбор случайного r

result = shor_classical(n, Q, a, y)
print(result)
