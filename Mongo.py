# Ruta del archivos JSON
ruta_json1 = r'C:\Users\Lonso\Desktop\Examen\BD1.json'
ruta_json2 = r'C:\Users\Lonso\Desktop\Examen\BD2.json'

import pandas as pd

try:
    # Lectura de JSON
    df1 = pd.read_json(ruta_json1)
    df2 = pd.read_json(ruta_json2)

    # Unir DF
    df=pd.concat([df1, df2], axis=0)

    # Limpieza de datos
    df = df.drop_duplicates()
    df.dropna()

    df=df.drop(['isbn', 'autor_fecha_nacimiento'],axis=1)
    df = df.set_index('id')

except Exception as e:
    print("Error en la ejecución:", e)

# Cargar base de datos en MONGO DB

from pymongo import MongoClient
import json
import pandas as pd

#Conexion
cliente = MongoClient("mongodb://localhost:27017/")

#Crear base de datos y coleccion

db=cliente['Libreria']
coleccion = db['Libros']

#Insertar datos a la coleción
def insertar(coleccion, registro):
    rows = None
    try:
        rows = coleccion.insert_many(registro)
        print(f"{len(rows.inserted_ids)} Agregado a Mongo!")
    except Exception as e:
        print(e)
    return rows



#Agrega DataFrame inicial
records = json.loads(df.T.to_json()).values()
insertar(coleccion, records)

cliente.close()