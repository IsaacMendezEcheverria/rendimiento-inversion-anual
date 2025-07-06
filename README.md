# Calculadora de Rendimiento de Inversión Anual

Este programa calcula el capital obtenido en una inversión año por año, mostrando la evolución del capital con interés compuesto.

## Funcionalidades

- Solicita al usuario la cantidad inicial a invertir
- Pide el interés anual (en porcentaje)
- Solicita el número de años de la inversión
- Muestra el capital obtenido año por año
- Calcula y muestra la ganancia total y el rendimiento porcentual

## Uso

### Ejecutar el programa:

```bash
python calculadora_inversion.py
```

### Ejemplo de uso:

```
=== CALCULADORA DE RENDIMIENTO DE INVERSIÓN ===

Ingrese la cantidad inicial a invertir ($): 1000
Ingrese el interés anual (en %): 5
Ingrese el número de años de la inversión: 5

=== RESUMEN DE LA INVERSIÓN ===
Capital inicial: $1,000.00
Interés anual: 5.0%
Período: 5 años

=== EVOLUCIÓN DEL CAPITAL ===
Año 0: $1,000.00
Año 1: $1,050.00 (Ganancia: $50.00)
Año 2: $1,102.50 (Ganancia: $52.50)
Año 3: $1,157.63 (Ganancia: $55.13)
Año 4: $1,215.51 (Ganancia: $57.88)
Año 5: $1,276.28 (Ganancia: $60.77)

=== RESUMEN FINAL ===
Capital final: $1,276.28
Ganancia total: $276.28
Rendimiento total: 27.63%
```

## Características del programa

- **Validación de entrada**: Verifica que los valores ingresados sean positivos y numéricos
- **Formato monetario**: Muestra los valores con formato de moneda para mejor legibilidad
- **Cálculo preciso**: Utiliza la fórmula de interés compuesto para cálculos exactos
- **Manejo de errores**: Captura errores de entrada y muestra mensajes informativos

## Fórmula utilizada

El programa utiliza la fórmula de interés compuesto:

```
Capital_final = Capital_inicial × (1 + tasa_interés)^años
```

Donde:
- `Capital_inicial`: La cantidad inicial invertida
- `tasa_interés`: El interés anual expresado como decimal (ej: 5% = 0.05)
- `años`: El número de años de la inversión
