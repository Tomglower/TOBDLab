import math

def first():
    a = int(input("Введите число a: "))
    b = int(input("Введите число b: "))
    result = ((math.tan(2 * (a / b)) - math.sin(b * (math.pow(a, 2) / 2))) /
              (a * math.pow(b, 2) + b * math.pow(a, 2))) * (math.pow(math.e, math.sqrt(a * b) + math.sqrt(b)))
    return round(result, 2)

def delete_commas(input_string):
    output_string = input_string.replace(",", "")
    deleted_characters_count = len(input_string) - len(output_string)
    print("Исходная строка:", input_string)
    print("Строка без запятых:", output_string)
    print("Количество удаленных символов:", deleted_characters_count)

def manipulate_array(N):
    arr = []
    for i in range(N):
        num = int(input(f"Введите элемент {i + 1}: "))
        arr.append(num)

    odd_count = 0
    for i in range(N):
        if arr[i] % 2 != 0:
            arr[i] = 0
            odd_count += 1

    print("Измененный массив:", arr)
    print("Количество нечётных элементов:", odd_count)

def manipulate_2d_array():
    print("Задание 6")
    n = int(input("Введите количество строк: "))
    m = int(input("Введите количество столбцов: "))

    array = []
    for i in range(n):
        row = []
        for j in range(m):
            element = int(input(f"Введите элемент [{i + 1}][{j + 1}]: "))
            row.append(element)
        array.append(row)

    for i in range(n):
        min_element = min(array[i])
        max_element = max(array[i])

        min_index = array[i].index(min_element)
        max_index = array[i].index(max_element)

        array[i][min_index], array[i][max_index] = array[i][max_index], array[i][min_index]

    print("Измененный массив:")
    for i in range(n):
        print(array[i])

if __name__ == '__main__':
    print("Задание 2:", first())

    x = float(input("Задание 3. Введите число: "))
    if x < -1:
        print(math.sin(pow(x + 1, 2)))
    elif -1 <= x < 1:
        print(-(1 + math.cos(math.pi * x)))
    elif x >= 1:
        print(math.sin(pow(x - 1, 2)))

    string = input("Задание 4. Введите строку:")
    delete_commas(string)

    N = int(input("Задание 5. Введите размерность массива:"))
    manipulate_array(N)
    manipulate_2d_array()
