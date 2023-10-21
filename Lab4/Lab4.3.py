import matplotlib.pyplot as plt
import numpy as np

продажи_1 = [100, 200, 300, 400, 500, 600]
продажи_2 = [700, 800, 900, 1000, 1100, 1200]

fig, ax = plt.subplots(1, 2, figsize=(10, 5))

ax[0].plot(продажи_1, label="Предприятие 1")
ax[0].plot(продажи_2, label="Предприятие 2")
ax[0].legend()
ax[0].set_title("Графики объёмов продаж")
ax[0].set_xlabel("Месяц")
ax[0].set_ylabel("Объём продаж")

x = np.arange(len(продажи_1))
width = 0.35

ax[1].bar(x - width/2, продажи_1, width, label="Предприятие 1")
ax[1].bar(x + width/2, продажи_2, width, label="Предприятие 2")
ax[1].set_xticks(x)
ax[1].set_xticklabels(["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь"])
ax[1].set_title("Столбчатые диаграммы объёмов продаж")
ax[1].set_xlabel("Месяц")
ax[1].set_ylabel("Объём продаж")

fig2, ax2 = plt.subplots(1, 2, figsize=(10, 5))

ax2[0].pie(продажи_1, labels=["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь"], autopct="%.1f%%")
ax2[0].set_title("Круговая диаграмма объёмов продаж предприятия 1")

ax2[1].pie(продажи_2, labels=["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь"], autopct="%.1f%%")
ax2[1].set_title("Круговая диаграмма объёмов продаж предприятия 2")

plt.show()