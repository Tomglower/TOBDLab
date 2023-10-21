import numpy as np

def input_array_a():
    a = np.empty((4, 4))
    for i in range(4):
        for j in range(4):
            a[i, j] = float(input(f"Введите элемент a[{i}][{j}]: "))
    return a


def create_array_b():
    b = np.random.uniform(-10, 10, (4, 4))
    return b

def print_array_info(arr, name):
    print(f"Массив {name}:")
    print(arr)
    print("Shape:", arr.shape)
    print("Size:", arr.size)
    print("Ndim:", arr.ndim)
    print("Dtype:", arr.dtype)
    print()


def swap_min_max_elements(a):
    for i in range(4):
        min_idx = np.argmin(a[i])
        max_idx = np.argmax(a[i])
        a[i][min_idx], a[i][max_idx] = a[i][max_idx], a[i][min_idx]
    return a

def average_of_even_elements(b):
    third_column = b[:, 2]
    even_elements = third_column[third_column % 2 == 0]
    return np.mean(even_elements)

def negative_elements_of_a(a):
    return a[a < 0]

def square_second_row(a):
    a[1, :] = np.square(a[1, :])
    return a


def extract_and_flatten_columns(a):
    new_array = a[:, [0, -1]]
    flattened_array = new_array.flatten()
    print("Новый массив из первого и последнего столбцов a:")
    print(new_array)
    print("Преобразованный в одномерный:")
    print(flattened_array)
    return flattened_array

def print_part_of_b(b):
    part_b = b[1:4, 3]
    print("Часть массива b от элемента b[1,3] до элемента b[3,3]:")
    print(part_b)

def insert_new_row(a):
    new_row = np.array([[10, 10, 10, 10]])
    a = np.insert(a, 2, new_row, axis=0)
    return a

def transpose_b(b):
    transposed_b = np.transpose(b)
    return transposed_b

a = input_array_a()

b = create_array_b()

print_array_info(a, "a")
print_array_info(b, "b")

a = swap_min_max_elements(a)
average = average_of_even_elements(b)
negatives = negative_elements_of_a(a)
a = square_second_row(a)
flattened_a = extract_and_flatten_columns(a)
print_part_of_b(b)
a = insert_new_row(a)
transposed_b = transpose_b(b)

print("Массив a после замены минимальных и максимальных элементов:")
print(a)
print("Среднее арифметическое чётных элементов третьего столбца b:", average)
print("Одномерный массив из отрицательных элементов a:", negatives)
print("Массив a после возведения второй строки в квадрат:")
print(a)
print("Преобразованный массив из первого и последнего столбцов a:")
print(flattened_a)
print("Массив b после транспонирования:")
print(transposed_b)
