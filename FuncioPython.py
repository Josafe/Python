def mostrarPrecioFinal(producto, precio, descuento):
    precioFinal = precio - descuento * precio / 100
    print("El precio del " + producto + " es: $ " + str(precioFinal))

mostrarPrecioFinal("Pantalon", 40, 20)
mostrarPrecioFinal("Camiseta", 30, 50)