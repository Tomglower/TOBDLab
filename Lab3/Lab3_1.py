import numpy as np

def input_array_a():
    a = np.array([float(input(f"Введите элемент a[{i}]: ")) for i in range(10)])
    return a

def create_array_b():
    b = np.linspace(0, 9, 10)
    return b

def create_random_array_c():
    c = np.random.uniform(1, 5, 10)
    return c

def print_array_info(arr, name):
    print(f"Массив {name}:")
    print(arr)
    print("Shape:", arr.shape)
    print("Size:", arr.size)
    print("Ndim:", arr.ndim)
    print("Dtype:", arr.dtype)
    print()

def sum_of_minimals(a, b, c):
    return np.min(a) + np.min(b) + np.min(c)

def add_arrays(a, b):
    return a + b

def remove_even_positions(a):
    return a[1::2]

def insert_sequence(b):
    return np.insert(b, 3, [1, 1, 1])

def copy_array_a(a):
    d = np.copy(a)
    return d

def concatenate_arrays(a, b):
    return np.concatenate((a, b))

def split_array(d):
    half = len(d) // 2
    return d[:half], d[half:]

def reshape_array(a):
    return a.reshape(2, 5)

a = input_array_a()

b = create_array_b()
c = create_random_array_c()

print_array_info(a, "a")
print_array_info(b, "b")
print_array_info(c, "c")

result1 = sum_of_minimals(a, b, c)
result2 = add_arrays(a, b)
result3 = remove_even_positions(a)
result4 = insert_sequence(b)
d = copy_array_a(a)
result5 = concatenate_arrays(a, b)
result6, result7 = split_array(d)
result8 = reshape_array(a)

print("\nРезультаты задач:")
print("Сумма минимальных элементов каждого массива:", result1)
print("Сложение массивов a и b:")
print(result2)
print("Массив a после удаления чётных позиций:")
print(result3)
print("Массив b после вставки [1,1,1] между 3 и 4 позициями:")
print(result4)
print("Результат объединения массивов a и b:")
print(result5)
print("Первая половина массива d:")
print(result6)
print("Вторая половина массива d:")
print(result7)
print("Двумерный массив из a:")
print(result8)
