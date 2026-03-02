from datetime import datetime, timedelta

fecha = input("Ingrese una fecha (YYYY-MM-DD): ")
fecha_obj = datetime.strptime(fecha, "%Y-%m-%d")

nueva_fecha = fecha_obj + timedelta(days=1)

print("Nueva fecha:", nueva_fecha.strftime("%Y-%m-%d"))
print("Cálculo completado")
print("Modificación hecha en local")
print("Modificación hecha en remoto")
