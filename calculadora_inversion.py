def calcular_inversion():
    """
    Programa que calcula el capital obtenido en una inversión año por año.
    Solicita al usuario la cantidad inicial, el interés anual y el número de años.
    """
    print("=== CALCULADORA DE RENDIMIENTO DE INVERSIÓN ===\n")
    
    try:
        # Solicitar datos al usuario
        capital_inicial = float(input("Ingrese la cantidad inicial a invertir ($): "))
        interes_anual = float(input("Ingrese el interés anual (en %): "))
        años = int(input("Ingrese el número de años de la inversión: "))
        
        # Validar que los valores sean positivos
        if capital_inicial <= 0 or interes_anual < 0 or años <= 0:
            print("Error: Todos los valores deben ser positivos.")
            return
        
        print(f"\n=== RESUMEN DE LA INVERSIÓN ===")
        print(f"Capital inicial: ${capital_inicial:,.2f}")
        print(f"Interés anual: {interes_anual}%")
        print(f"Período: {años} años")
        print(f"\n=== EVOLUCIÓN DEL CAPITAL ===")
        
        # Calcular y mostrar el capital año por año
        capital_actual = capital_inicial
        tasa_interes = interes_anual / 100  # Convertir porcentaje a decimal
        
        print(f"Año 0: ${capital_actual:,.2f}")
        
        for año in range(1, años + 1):
            # Aplicar interés compuesto
            capital_actual = capital_actual * (1 + tasa_interes)
            ganancia_año = capital_actual - (capital_inicial * (1 + tasa_interes) ** (año - 1))
            
            print(f"Año {año}: ${capital_actual:,.2f} (Ganancia: ${ganancia_año:,.2f})")
        
        # Mostrar resumen final
        ganancia_total = capital_actual - capital_inicial
        print(f"\n=== RESUMEN FINAL ===")
        print(f"Capital final: ${capital_actual:,.2f}")
        print(f"Ganancia total: ${ganancia_total:,.2f}")
        print(f"Rendimiento total: {(ganancia_total / capital_inicial) * 100:.2f}%")
        
    except ValueError:
        print("Error: Por favor ingrese valores numéricos válidos.")
    except Exception as e:
        print(f"Error inesperado: {e}")

# Ejecutar el programa
if __name__ == "__main__":
    calcular_inversion()
