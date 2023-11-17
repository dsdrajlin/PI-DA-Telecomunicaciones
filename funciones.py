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

    # Ajustar las etiquetas del eje x para mejorar la legibilidad.
    plt.xticks(rotation=45, ha="right")

    # Ajustar los límites del eje y.
    plt.ylim(ylim)

    # Mostrar el gráfico.
    plt.show()

    
def get_outliers_df_provincia(df, exclude: list, size=(16, 8), cols_por_fila=2, rotacion=45):
    """
    Crea un conjunto de boxplots para visualizar los valores atípicos en las 
    columnas numéricas de un DataFrame, separados por provincia.

    Parameters
    ----------
    df : pandas.DataFrame
        El DataFrame que se utilizará para crear los boxplots.
    exclude : list
        Lista de columnas a excluir del boxplot.
    size : tuple, optional
        Tamaño de la figura. Por defecto, es (16, 8).
    cols_por_fila : int, optional
        Número de columnas por fila en la grilla de boxplots. Por defecto, es 2.
    rotacion : int, optional
        Grados de rotación de las etiquetas del eje x. Por defecto, es 45.

    Returns
    -------
    None

    Prints
    ------
    None
        Muestra una grilla de boxplots, cada uno correspondiente a una provincia, 
        para visualizar valores atípicos.
    """
    # Obtener la lista única de provincias.
    provincias = df['Provincia'].unique()

    # Calcular el número total de filas necesario para la grilla.
    total_filas = math.ceil(len(provincias) / cols_por_fila)

    # Configurar el tamaño de la figura de la grilla.
    fig, axes = plt.subplots(total_filas, cols_por_fila, 
                             figsize=(size[0], size[1] * total_filas))

    # Asegurarse de que "axes" sea una matriz bidimensional.
    if total_filas == 1:
        axes = axes.reshape(1, -1)
    else:
        axes = axes.reshape(total_filas, cols_por_fila)

    # Iterar sobre las provincias y crear los boxplots.
    for i, provincia in enumerate(provincias):
        # Obtener el subconjunto de datos para la provincia actual.
        subset_df = df[df['Provincia'] == provincia]

        # Seleccionar el eje correcto en la grilla.
        row = i // cols_por_fila
        col = i % cols_por_fila

        # Llamar a la función sns.boxplot con el subconjunto de datos.
        sns.boxplot(data=subset_df.drop(exclude, axis=1), ax=axes[row, col])

        # Establecer el título de la provincia.
        axes[row, col].set_title(f"Provincia: {provincia}")

        # Rotar las etiquetas del eje x para mejorar la legibilidad.
        axes[row, col].tick_params(axis='x', rotation=rotacion)

    # Ajustar el diseño de la grilla y mostrar la figura.
    plt.tight_layout()
    plt.show()