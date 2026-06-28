# Algoritmos Computacionales
# Actividad: Flujo de Control (parte 1) - Tarea 1
# Nombre: [Coloca aqui tu nombre]
# Programa que calcula la cuota mensual de un prestamo (sistema de amortizacion
# de cuota fija / sistema frances), a partir del monto, la tasa de interes
# anual y el tiempo a pagar en meses.

# --- Entrada de datos ---
monto = float(input("Ingrese el monto del prestamo (RD$): "))
tasa_anual = float(input("Ingrese la tasa de interes anual (%): "))
meses = int(input("Ingrese el tiempo a pagar (en meses): "))

# --- Procesamiento ---
# Se convierte la tasa anual a tasa mensual en formato decimal
tasa_mensual = (tasa_anual / 100) / 12

if tasa_mensual == 0:
    # Si la tasa es 0%, la cuota es simplemente el monto dividido entre los meses
    cuota = monto / meses
else:
    # Formula de la cuota fija (sistema frances de amortizacion):
    # Cuota = Monto * i / (1 - (1 + i)^-n)
    cuota = monto * tasa_mensual / (1 - (1 + tasa_mensual) ** (-meses))

# --- Salida de resultados ---
print("\n--- Resultado del calculo de prestamo ---")
print(f"Monto del prestamo: RD${monto:,.2f}")
print(f"Tasa de interes anual: {tasa_anual:.2f}%")
print(f"Tiempo a pagar: {meses} meses")
print(f"Cuota mensual a pagar: RD${cuota:,.2f}")
