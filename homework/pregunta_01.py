"""
Escriba el codigo que ejecute la accion solicitada en la pregunta.
"""


def pregunta_01():
    """
    Realice la limpieza del archivo "files/input/solicitudes_de_credito.csv".
    El archivo tiene problemas como registros duplicados y datos faltantes.
    Tenga en cuenta todas las verificaciones discutidas en clase para
    realizar la limpieza de los datos.

    El archivo limpio debe escribirse en "files/output/solicitudes_de_credito.csv"

    """
    import os
    import pandas as pd

    df = pd.read_csv("files/input/solicitudes_de_credito.csv", sep=";", index_col=0)
    
    df["sexo"] = df["sexo"].str.lower().str.strip()
    df["tipo_de_emprendimiento"] = df["tipo_de_emprendimiento"].str.lower().str.strip()

    df["idea_negocio"] = df["idea_negocio"].str.lower().str.replace("_", " ").str.replace("-", " ").str.strip()
    df["barrio"] = df["barrio"].str.lower().str.replace("_", " ").str.replace("-", " ")
    
    df["estrato"] = [int(x) for x in df["estrato"]]
    df["comuna_ciudadano"] = [int(x) for x in df["comuna_ciudadano"]]
    
    fecha_formato_1 = pd.to_datetime(df["fecha_de_beneficio"], format="%d/%m/%Y", errors="coerce")
    fecha_formato_2 = pd.to_datetime(df["fecha_de_beneficio"], format="%Y/%m/%d", errors="coerce")
    df["fecha_de_beneficio"] = fecha_formato_1.combine_first(fecha_formato_2)

    df["monto_del_credito"] = df["monto_del_credito"].str.replace("$", "", regex=False).str.replace(",", "", regex=False).str.replace(".00", "", regex=False).str.strip()

    df["línea_credito"] = df["línea_credito"].str.lower().str.strip().str.replace("_", " ").str.replace("-", " ").str.strip()

    df = df.drop_duplicates()
    df = df.dropna()

    os.makedirs("files/output", exist_ok=True)
    df.to_csv("files/output/solicitudes_de_credito.csv", sep=";", index=False)
