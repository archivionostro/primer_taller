from datetime import date, timedelta

hoy = date.today()
manana = hoy + timedelta(days=1)
print(f"Hoy: {hoy}, Mañana: {manana}")
print("Este archivo fue modificado en local")
print("Este archivo fue modificado DIRECTAMENTE EN GITHUB")
print("Ambos cambios combinados después del conflicto")
