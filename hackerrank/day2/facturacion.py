def facturacion():
    print("=" * 50)
    print("      SISTEMA DE FACTURACIÓN")
    print("=" * 50)

    cantidad = 1
    productos = []

    subtotal = 0

    for i in range(cantidad):
        print(f"\nProducto #{i+1}")

        nombre = input("Nombre del producto: ")
        precio = float(input("Precio del producto: RD$ "))
        cantidad_producto = int(input("Cantidad: "))

        total_producto = precio * cantidad_producto
        subtotal += total_producto

        productos.append({
            "nombre": nombre,
            "precio": precio,
            "cantidad": cantidad_producto,
            "total": total_producto
        })

    tip_percent = int(input("\nDigite el porcentaje de propina: "))
    tax_percent = int(input("Digite el porcentaje de ITBIS: "))

    propina = subtotal * (tip_percent / 100)
    impuesto = subtotal * (tax_percent / 100)
    total = subtotal + propina + impuesto

    print("\n")
    print("=" * 60)
    print("                 FACTURA")
    print("=" * 60)
    print(f'{"Producto":20} {"Cant.":>5} {"Precio":>10} {"Total":>12}')
    print("-" * 60)

    for p in productos:
        print(f'{p["nombre"]:20} {p["cantidad"]:>5} {p["precio"]:>10.2f} {p["total"]:>12.2f}')

    print("-" * 60)
    print(f'Subtotal:{"":30} RD$ {subtotal:.2f}')
    print(f'Propina ({tip_percent}%):{"":22} RD$ {propina:.2f}')
    print(f'ITBIS ({tax_percent}%):{"":24} RD$ {impuesto:.2f}')
    print("=" * 60)
    print(f'TOTAL A PAGAR:{"":24} RD$ {round(total)}')
    print("=" * 60)


facturacion()