import pandas as pd

# Функция для загрузки данных из файла
def load_titanic_data(file_path):
    return pd.read_csv(file_path)

# Функция для вывода информации о датафрейме
def display_dataframe_info(df):
    df.info()

# Функция для вывода первых N строк датафрейма
def display_first_n_rows(df, n=5):
    return df.head(n)

# Функция для замены значений в столбце Gender
def replace_gender_values(df):
    df['Gender'] = df['Gender'].replace({'male': 'man', 'female': 'woman'})
    return df

# Функция для нахождения максимального возраста пассажира и соответствующей строки(строк)
def find_max_age_passenger(df):
    max_age = df['Age'].max()
    return df[df['Age'] == max_age]

# Функция для вычисления средней стоимости билета
def calculate_average_fare(df):
    return df['Fare'].mean()

# Функция для вывода информации о пассажирах с родственниками
def passengers_with_relatives(df):
    return df[(df['SibSp'] > 0) | (df['Parch'] > 0)]

# Функция для вывода информации о мужчинах до 50 лет и их количестве
def men_under_50(df):
    men_under_50_df = df[(df['Gender'] == 'man') & (df['Age'] < 50)]
    return men_under_50_df, len(men_under_50_df)

# Функция для сортировки по столбцу Pclass
def sort_by_pclass(df):
    return df.sort_values(by='Pclass')

# Функция для вывода информации о количестве мужчин и женщин в каждом классе
def count_gender_in_each_class(df):
    return df.groupby(['Pclass', 'Gender']).size().reset_index(name='Count')

# Функция для анализа влияния класса пассажира на выживаемость
def analyze_survival_by_class(df):
    class_survival = df.groupby(['Pclass', 'Survived'])['PassengerId'].count().unstack()
    class_survival['Survival Rate'] = (class_survival[1] / (class_survival[0] + class_survival[1])) * 100
    return class_survival

# Загрузка данных из файла
titanic_df = load_titanic_data("titanic.csv")

# Вывод информации о датафрейме
print("\nЗадание 2.2: Содержание датафрейма:")
display_dataframe_info(titanic_df)

# Вывод первых 5 строк датафрейма
print("\nЗадание 2.3: Первые 5 строк датафрейма:")
display_first_n_rows(titanic_df)

# Замена значений в столбце Gender
titanic_df = replace_gender_values(titanic_df)

# Поиск пассажиров с максимальным возрастом
max_age_passenger = find_max_age_passenger(titanic_df)
print("\nЗадание 2.4: Пассажиры с максимальным возрастом:")
print(max_age_passenger)

# Вычисление средней стоимости билета
average_fare = calculate_average_fare(titanic_df)
print("\nЗадание 2.5: Средняя стоимость билета:", average_fare)

# Пассажиры с родственниками
passengers_with_relatives_df = passengers_with_relatives(titanic_df)
print("\nЗадание 2.6: Пассажиры с родственниками:")
print(passengers_with_relatives_df)

# Мужчины до 50 лет и их количество
men_under_50_df, men_count = men_under_50(titanic_df)
print("\nЗадание 2.7: Мужчины до 50 лет:")
print(men_under_50_df)
print("Количество мужчин до 50 лет:", men_count)

# Сортировка по столбцу Pclass
sorted_titanic_df = sort_by_pclass(titanic_df)
print("\nЗадание 2.8: Данные, отсортированные по Pclass:")
print(sorted_titanic_df)

# Информация о количестве мужчин и женщин в каждом классе
gender_in_each_class_df = count_gender_in_each_class
