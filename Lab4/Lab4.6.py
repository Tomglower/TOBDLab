import numpy as np
import matplotlib.pyplot as plt

# Создаем случайный массив 10x10 из чисел на отрезке [0, 1]
random_array = np.random.rand(10, 10)

# Вырезаем части изображения
part = random_array[:4, 6:]
# Шаг 3: Инвертируем цвета
inverted_array = 1 - random_array

# Производим размытие
blurred_array = np.copy(random_array)
for i in range(1, 9):
    for j in range(1, 9):
        blurred_array[i, j] = (random_array[i, j-1] + random_array[i, j] + random_array[i, j+1]) / 3

# Создаем изображение с 4 графиками
fig, axs = plt.subplots(2, 2, figsize=(8, 8))

# Отображаем исходный массив
axs[0, 0].imshow(random_array, cmap='gray')
axs[0, 0].set_title('Исходное изображение')

# Отображаем инвертированный массив
axs[0, 1].imshow(inverted_array, cmap='gray')
axs[0, 1].set_title('Инвертированное изображение')

# Отображаем размытое изображение
axs[1, 0].imshow(blurred_array, cmap='gray')
axs[1, 0].set_title('Размытое изображение')

# Отображаем вырезанные части
axs[1, 1].imshow(part, cmap='gray')
axs[1, 1].set_title('Правый верхний угол 4x4')

# Удаляем оси координат
for ax in axs.flat:
    ax.axis('off')

# Сохраняем изображение
plt.savefig('lab6_result.png')
plt.show()
