import pandas as pd


def load_data(file_path):
    print("1.1 Загрузка данных из CSV файла.")
    df = pd.read_csv(file_path, delimiter=";")
    return df

def describe_dataframe(description, df):
    print(description)
    print(df)

# Функция для вывода первых 5 строк датафрейма
def display_first_rows(df):
    print("1.3 Вывод первых 5 строк датафрейма:")
    print(df.head(5))

# Функция для вывода информации о датафрейме
def display_dataframe_info(df):
    print("1.4 Вывод информации о датафрейме:")
    df.info()

# Функция для вывода количества строк и столбцов
def display_shape(df):
    print("1.5 Количество строк и столбцов:", df.shape)

# Функция для вывода названий столбцов
def display_columns(df):
    print("1.6 Названия столбцов:", df.columns)

# Функция для вывода индексов строк
def display_indexes(df):
    print("1.7 Индексы строк:", df.index)

# Функция для вывода содержимого датафрейма как массив
def display_data_as_array(df):
    print("1.8 Содержимое датафрейма как массив:")
    data_array = df.values
    print(data_array)

# Функция для вывода типов данных в каждом столбце
def display_data_types(df):
    print("1.9 Типы данных в каждом столбце:")
    print(df.dtypes)

# Функция для вывода массива уникальных значений в произвольном столбце
def display_unique_values(df, column_name):
    unique_values = df[column_name].unique()
    print("1.10 Уникальные значения в столбце '{}':".format(column_name))
    print(unique_values)

# Функция для вывода количества уникальных значений в каждом столбце
def display_unique_value_counts(df):
    unique_counts = df.nunique()
    print("1.11 Количество уникальных значений в каждом столбце:")
    print(unique_counts)

# Функция для вывода количества пропущенных значений в каждом столбце
def display_missing_values(df):
    missing_values = df.isnull().sum()
    print("1.12 Количество пропущенных значений в каждом столбце:")
    print(missing_values)

# Функция для удаления строк с пропущенными значениями
def drop_rows_with_missing_values(df):
    print("1.13 Удаление строк с пропущенными значениями.")
    df = df.dropna()
    print(df)
    return df

# Функция для удаления дубликатов строк
def drop_duplicate_rows(df):
    print("1.14 Удаление дубликатов строк.")
    df = df.drop_duplicates()
    print(df)
    return df

# Функция для переименования двух произвольных столбцов
def rename_columns(df, old_names, new_names):
    print("1.15 Переименование столбцов.")
    df.rename(columns=dict(zip(old_names, new_names)), inplace=True)
    print(df)
    return df


# Функция для удаления последнего столбца и вставки его в начало датафрейма
def move_last_column_to_beginning(df):
    print("1.16 Удаление последнего столбца и вставка его в начало датафрейма.")
    last_column = df.pop(df.columns[-1])
    df.insert(0, last_column.name, last_column)
    print(df)
    return df

# Функция для удаления последних 20 строк датафрейма
def drop_last_n_rows(df, n):
    print("1.16 Удаление последних {} строк датафрейма.".format(n))
    df = df.iloc[:-n]
    print(df)
    return df

# Функция для создания нового датафрейма из первых 10 строк и 3 столбцов
def create_new_dataframe(df, rows, columns):
    print("1.17 Создание нового датафрейма из первых {} строк и {} столбцов.".format(rows, columns))
    new_df = df.iloc[:rows, :columns]
    print(new_df)
    return new_df

# Функция для записи датафрейма в файл Excel
def write_to_excel(df, file_name):
    print("1.18 Запись датафрейма в файл Excel: '{}'.".format(file_name))
    df.to_excel(file_name, index=False)

# Загрузка данных
dataframe = load_data("https://raw.githubusercontent.com/dm-fedorov/pandas_basic/master/data/bank.csv")

# Вывод описания и информации о датафрейме
describe_dataframe("Описание датасета:", dataframe)
display_first_rows(dataframe)
display_dataframe_info(dataframe)
display_shape(dataframe)
display_columns(dataframe)
display_indexes(dataframe)
display_data_as_array(dataframe)
display_data_types(dataframe)

# Вывод уникальных и пропущенных значений
display_unique_values(dataframe, "month")
display_unique_value_counts(dataframe)
display_missing_values(dataframe)

# Удаление строк и дубликатов
dataframe = drop_rows_with_missing_values(dataframe)
dataframe = drop_duplicate_rows(dataframe)

# Переименование столбцов
dataframe = rename_columns(dataframe, ["balance", "day"], ["money", "days"])

# Удаление последнего столбца и вставка его в начало датафрейма
dataframe = move_last_column_to_beginning(dataframe)

# Удаление последних 20 строк
dataframe = drop_last_n_rows(dataframe, 20)

# Создание нового датафрейма
new_dataframe = create_new_dataframe(dataframe, 10, 3)

# Запись в файл Excel
write_to_excel(new_dataframe, "5-6.1.xlsx")
