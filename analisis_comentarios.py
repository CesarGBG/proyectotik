import pandas as pd
import re
import matplotlib.pyplot as plt

# 1. Cargar el archivo CSV
df = pd.read_csv("comentarios_video1.csv")  # Cambia el nombre si es diferente

# 2. Mostrar las primeras filas y columnas disponibles
print("Primeras filas del archivo:")
print(df.head())
print("\nColumnas disponibles:")
print(df.columns)

# 3. Limpiar el texto: minúsculas, quitar símbolos, etc.
df["texto_limpio"] = df["text"].apply(lambda x: re.sub(r"[^a-zA-ZáéíóúÁÉÍÓÚñÑ\s]", "", str(x).lower()))

# 4. Lista de palabras ofensivas (puedes editarla o ampliarla)
palabras_ofensivas = [
    "feo", "peru"
]

# 5. Función para detectar si el comentario contiene alguna palabra ofensiva
def es_discriminatorio(texto):
    return any(p in texto for p in palabras_ofensivas)

# 6. Aplicar la función a los comentarios limpios
df["discriminatorio"] = df["texto_limpio"].apply(es_discriminatorio)

# 7. Mostrar conteo de comentarios discriminatorios vs no discriminatorios
conteo = df["discriminatorio"].value_counts()
print("\nConteo de comentarios discriminatorios vs no discriminatorios:")
print(conteo)

# 8. Visualización básica (gráfico de barras)
conteo.plot(kind="bar", color=["green", "red"])
plt.xticks([0, 1], ["No Discriminatorio", "Discriminatorio"], rotation=0)
plt.title("Distribución de comentarios discriminatorios")
plt.ylabel("Cantidad de comentarios")
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.tight_layout()
plt.show()
