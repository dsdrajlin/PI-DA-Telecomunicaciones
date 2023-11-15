import matplotlib.pyplot as plt
import seaborn as sns
import math

def eda_inicial(df):
    """
    Realiza un Análisis Exploratorio de Datos (EDA) inicial en un DataFrame.

    Parameters
    ----------
    df : pandas.DataFrame
        El DataFrame que se analizará.

    Returns
    -------
    None

    Prints
    ------
    None
        Imprime información sobre el DataFrame, incluyendo nombre y tipo de columnas,
        número de filas y valores nulos.
    None
        Imprime el número de duplicados en el DataFrame.
    None
        Imprime estadísticas descriptivas de las columnas.
    """
    # Obtener información del DataFrame, incluyendo nombre y tipo de columnas,
    # número de filas y valores nulos.
    print(df.info(), "\n")

    # Obtener los duplicados considerando todas las columnas.
    print(f"El número de duplicados en el DataFrame es: {df.duplicated().sum()} \n")

    # Describir las columnas.
    print(df.describe(include="all"), "\n")


def get_outliers_df(df, exclude = [], size = (16,8), ylim= None):
    """
    Crea un boxplot para visualizar los valores atípicos en las columnas numéricas 
    de un DataFrame.

    Parameters
    ----------
    df : pandas.DataFrame
        El DataFrame que se utilizará para crear el boxplot.
    exclude : list, optional
        Lista de columnas a excluir del boxplot. Por defecto, es una lista vacía.
    size : tuple, optional
        Tamaño de la figura. Por defecto, es (16, 8).
    ylim : tuple, optional
        Límites del eje y. Por defecto, se ajusta automáticamente.

    Returns
    -------
    None

    Prints
    ------
    None
        Muestra un boxplot de todas las columnas numéricas del DataFrame excluyendo las especificadas en "exclude".
    """
    # Configurar el tamaño de la figura.
    plt.figure(figsize=size)

    # Crear el boxplot con todas las columnas numéricas no incluidas en "exclude".
    sns.boxplot(data=df.drop(exclude, axis=1))

    # Personalizar el título y las etiquetas de los ejes.
    plt.title("Boxplot de las Columnas Numéricas")
    plt.xlabel("Columnas")
    plt.ylabel("Valores")

    # Rotar las etiquetas del eje x para mejorar la legibilidad.
    plt.xticks(rotation=45, ha="right")

    # Ajustar los límites del eje y.
    plt.ylim(ylim)

    # Mostrar el gráfico.
    plt.show()

    
def get_outliers_df_provincia(df, exclude: list, size=(16, 8), cols_per_row=2, rotation=45):
    # Obtener la lista única de provincias.
    provinces = df['Provincia'].unique()

    # Calcular el número total de filas necesario para la grilla.
    total_rows = math.ceil(len(provinces) / cols_per_row)

    # Configurar el tamaño de la figura de la grilla
    fig, axes = plt.subplots(total_rows, cols_per_row, figsize=(size[0], size[1] * total_rows))

    # Asegurarse de que 'axes' sea una matriz bidimensional.
    if total_rows == 1:
        axes = axes.reshape(1, -1)
    else:
        axes = axes.reshape(total_rows, cols_per_row)

    # Iterar sobre las provincias y crear los boxplots
    for i, province in enumerate(provinces):
        # Obtener el subconjunto de datos para la provincia actual
        subset_df = df[df['Provincia'] == province]

        # Seleccionar el eje correcto en la grilla
        row = i // cols_per_row
        col = i % cols_per_row

        # Llamar a la función sns.boxplot con el subconjunto de datos
        sns.boxplot(data=subset_df.drop(exclude, axis=1), ax=axes[row, col])

        # Establecer el título de la provincia
        axes[row, col].set_title(f"Provincia: {province}")

        # Rotar las etiquetas del eje x para mejorar la legibilidad
        axes[row, col].tick_params(axis='x', rotation=rotation)

    # Ajustar el diseño de la grilla y mostrar la figura
    plt.tight_layout()
    plt.show()