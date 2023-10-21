import math


def f(x):
    return pow(math.e, -x) - math.cos(x)


def dichotomy_method(a, b, epsilon):
    n = 0

    # Пока половина длины интервала (b - a) / 2 больше заданной точности epsilon
    while (b - a) / 2 > epsilon:
        # Вычисление двух промежуточных точек x1 и x2
        x1 = (a + b - epsilon) / 2
        x2 = (a + b + epsilon) / 2

        # Сравнение значений функции f(x1) и f(x2) и выбор нового интервала [a, b]
        if f(x1) < f(x2):
            b = x2
        else:
            a = x1

        # Увеличение счетчика итераций
        n += 1

    # Вычисление оптимального значения x, значения функции f(x) и числа итераций
    x_optimal = (a + b) / 2
    f_optimal = f(x_optimal)


    return x_optimal, f_optimal, n

a = float(input("Введите левую границу интервала: "))
b = float(input("Введите правую границу интервала: "))
epsilon = float(input("Введите точность: "))


x_opt, f_opt, num_iterations = dichotomy_method(a, b, epsilon)


print(f"Оптимальное значение x: {x_opt}")
print(f"Значение f(x): {f_opt}")
print(f"Число итераций: {num_iterations}")
