# Algoritmos Computacionales
# Actividad: Flujo de Control (parte 1) - Tarea 2
# Nombre: [Coloca aqui tu nombre]
# Programa que calcula el Impuesto Sobre la Renta (ISR) que debe pagar un
# empleado segun la escala salarial vigente de la DGII (Republica Dominicana).
#
# Escala ISR vigente (Resolucion DGII No. DDG-AR1-2026-00001), montos anuales:
#   Hasta RD$416,220.00                -> Exento (0%)
#   RD$416,220.01 - RD$624,329.00      -> 15% del excedente de RD$416,220.00
#   RD$624,329.01 - RD$867,123.00      -> RD$31,216.00 + 20% del excedente de RD$624,329.00
#   Mas de RD$867,123.00               -> RD$79,776.00 + 25% del excedente de RD$867,123.00

# --- Entrada de datos ---
sueldo_mensual = float(input("Ingrese el sueldo mensual del empleado (RD$): "))

# --- Procesamiento ---
sueldo_anual = sueldo_mensual * 12

if sueldo_anual <= 416220.00:
    isr_anual = 0
elif sueldo_anual <= 624329.00:
    isr_anual = (sueldo_anual - 416220.00) * 0.15
elif sueldo_anual <= 867123.00:
    isr_anual = 31216.00 + (sueldo_anual - 624329.00) * 0.20
else:
    isr_anual = 79776.00 + (sueldo_anual - 867123.00) * 0.25

isr_mensual = isr_anual / 12

# --- Salida de resultados ---
print(f"\nSueldo: RD${sueldo_mensual:,.2f}")
if isr_mensual == 0:
    print("ISR: N/A")
else:
    print(f"ISR: RD${isr_mensual:,.2f}")
