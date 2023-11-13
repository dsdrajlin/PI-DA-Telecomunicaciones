

def eda_inicial(df):
    # Obtener información del DataFrame, incluyendo nombre y tipo de columnas,
    # número de filas y valores nulos
    print(df.info(), "\n")

    # Obtener los duplicados considerando todas las columnas.
    print(f"El número de duplicados en el DataFrame es: {df.duplicated().sum()} \n")

    # Describir las columnas
    print(df.describe(include="all"), "\n")