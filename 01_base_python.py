def calcular_factura_final(precios):
    total_acumulado = 0
    cantidad_items = 0

    for monto in precios:
        total_acumulado += monto
        cantidad_items += 1

    if cantidad_items == 0:
        print("Error: El carrito está vacío")
        return 0, 0
    
    promedio = total_acumulado / cantidad_items

    print(f"El cobro final es de : ${total_acumulado:.2f}")
    print(f"El promedio por producto: ${promedio:.2f}")

    return total_acumulado, promedio

Carrito_compras = [59.99, 35.49, 43.50, 112.00]
total, promedio = calcular_factura_final(Carrito_compras)
print("valores retornados ->", "total", total, "promedio", promedio)