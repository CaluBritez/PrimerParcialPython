import pandas as pd
import matplotlib.pyplot as plt

ventas_mensuales = [
{"mes": "Enero", "total_ventas": 15000, "año": 2023},
{"mes": "Febrero", "total_ventas": 18000, "año": 2023},
{"mes": "Marzo", "total_ventas": 22000, "año": 2023},
{"mes": "Abril", "total_ventas": 19000, "año": 2023},
{"mes": "Mayo", "total_ventas": 25000, "año": 2023},
{"mes": "Junio", "total_ventas": 28000, "año": 2023},
{"mes": "Julio", "total_ventas": 32000, "año": 2023},
{"mes": "Agosto", "total_ventas": 30000, "año": 2023},
{"mes": "Septiembre", "total_ventas": 28000, "año": 2023},
{"mes": "Octubre", "total_ventas": 31000, "año": 2023},
{"mes": "Noviembre", "total_ventas": 33000, "año": 2023},
{"mes": "Diciembre", "total_ventas": 36000, "año": 2023},
{"mes": "Enero 2", "total_ventas": 37000, "año": 2024},
{"mes": "Febrero 2", "total_ventas": 38000, "año": 2024},
{"mes": "Marzo 2", "total_ventas": 42000, "año": 2024},
{"mes": "Abril 2", "total_ventas": 39000, "año": 2024},
{"mes": "Mayo 2", "total_ventas": 45000, "año": 2024},
{"mes": "Junio 2", "total_ventas": 48000, "año": 2024},
{"mes": "Julio 2", "total_ventas": 52000, "año": 2024},
{"mes": "Agosto 2", "total_ventas": 50000, "año": 2024},
{"mes": "Septiembre 2", "total_ventas": 48000, "año": 2024},
{"mes": "Octubre 2", "total_ventas": 51000, "año": 2024},
{"mes": "Noviembre 2", "total_ventas": 55000, "año": 2024},
{"mes": "Diciembre 2", "total_ventas": 58000, "año": 2024}
]
df = pd.DataFrame(ventas_mensuales)

#Respuesta
#No pude agrupar los datos por trimestre 

#Respuesta
print("Los meses donde las ventas superan los 20000 son los siguientes:")
print(df[df["total_ventas"] > 20000])

#Respuesta
mayor_valor = df["total_ventas"].max()
print(f"El monto de mayor volumen de venta fue de {mayor_valor} correspondiente al siguiente mes:")
print(df[df["total_ventas"] == mayor_valor])

#Respuesta
promedio = round(df["total_ventas"].mean(),2)
print(f"El promedio de ventas mensuales es de {promedio}")

#Respuesta
meses = df["mes"].tolist()
ventas = df["total_ventas"].tolist()
new_df = pd.DataFrame()
new_df["mes"] = meses
new_df["total_ventas"] = ventas
print(new_df)


#poligono de frecuencias
fig, ax = plt.subplots()
ax.plot(new_df["mes"], new_df["total_ventas"])
plt.title("Ventas totales por mes")
plt.xlabel('Mes')
plt.ylabel('Monto de ventas')
plt.show()
