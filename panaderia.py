menu = dict({
    "Pan": {
        "Producto" :list([
            {"nombre": "Pan de trigo", "valor": 800},
            {"nombre": "Pan de ajo", "valor": 1000},
            {"nombre": "Pan integral", "valor": 1500},
            {"nombre": "Bagette", "valor": 2000},
            {"nombre": "Pan tajado", "valor": 1000},
            {"nombre": "Rosca de maiz", "valor": 800},
            {"nombre": "Bollos suizos", "valor": 2000},
            {"nombre": "Bollitos de leche", "valor": 1500},
            {"nombre": "Pan de centeno", "valor": 3000},
            {"nombre": "Pan de bocadillo", "valor": 800},
        ]),
        "Promociones": list([
            {"codigo" :8, "nombre": "Descuento del 6% en la compra de 6", "unidades" : 6 , "descuento": 0.06},
            {"codigo" :5, "nombre": "Descuento del 15% en la compra de 10", "unidades" : 5 , "descuento": 0.15},
            ])
    },
    "Pasteles": {
        "Producto" :list([
            {"nombre": "Pastel de chocolate", "valor": 2500},
            {"nombre": "Torta de fresa", "valor": 2500},
            {"nombre": "Hojaldre de manzana", "valor": 1500},
            {"nombre": "Rollos de canela", "valor": 2000},
            {"nombre": "Tiramisu", "valor": 2000},
            {"nombre": "Pastel de zanahoria", "valor": 2500},
            {"nombre": "Empanada de frutas'", "valor": 1500},
            {"nombre": "Donas glaseados'", "valor": 1000},
            {"nombre": "Croassants rellenos", "valor": 2500},
            {"nombre": "Milhojas", "valor": 1500},
        ]),
        "Promociones": list([
            {"codigo" :6, "nombre": "Descuento del 7% en la compra de 10", "unidades" : 10 , "descuento": 0.07},
            {"codigo" :9, "nombre": "Descuento del 8% en la compra de 3", "unidades" : 3 , "descuento": 0.08},
        ])
    },
    "Galletas": {
        "Producto" :list([
            {"nombre": "Galletas de avena", "valor": 1000},
            {"nombre": "Galletas de chocolate", "valor": 2000},
            {"nombre": "Alfajores", "valor": 2500},
            {"nombre": "Mantecados", "valor": 2000},
            {"nombre": "Palmeritas", "valor": 2000},
            {"nombre": "Barquillos", "valor": 1500},
            {"nombre": "Galletas con chispas", "valor": 1500},
            {"nombre": "Galettes", "valor": 2000},
            {"nombre": "Biscotti", "valor": 2500},
            {"nombre": "Galletas de jengibre", "valor": 1500},
        ]),
        "Promociones": list([
            {"codigo":9, "nombre": "Descuento del 5% en la compra de 5", "unidades" : 5 , "descuento": 0.05},
            {"codigo":0, "nombre": "Descuento del 10% en la compra de 4", "unidades" : 4, "descuento": 0.1},
        ])
    }
})

#Esto es para mostrar todas las categorias de la lista de productos
print("seleccione la categoria")
listaCategoria = list( menu.keys())
for i, val in enumerate(listaCategoria):
    print(f"{i}. {val}")
opcioncategoria = int(input())
datosCategoria = menu.get(listaCategoria[opcioncategoria])
productosCategoria = datosCategoria.get("Producto")
#Este es para seleccionar el producto segun la categoria selecionada
print(f"Seleccione el producto de la categoria{listaCategoria[opcioncategoria]}")
for i, val in enumerate(productosCategoria):
    print(f"{i}. {val}")
opcionProducto = int(input())
#Este busca si el producto tiene promociones
datosCategoria = menu.get(listaCategoria[opcioncategoria])
promocionesProducto = datosCategoria.get("Promociones")
promocionProductos = list()
for val in promocionesProducto:
    if (val.get("codigo") == opcionProducto) :
        promocionProductos.append(val)
#esto es para saber si la lista de promociones tiene un producto seleccionado segun la categoria
if (len(promocionProductos)==0):
    producto = datosCategoria.get('Producto')[opcionProducto]
    nombreProducto = producto.get("nombre")
    productoValor = producto.get("valor")
    cantidad = int(input(f"Usuario cuantos {producto} desea?: "))
    valorApagar = cantidad * productoValor
    print(f"Usuario su producto{nombreProducto}tiene un valor de ${productoValor} la cantidad solicitada es de {cantidad} que da un total de ${round(valorApagar)} ")
    dinero = int(input("ingrese su dinero : "))
    if (dinero >= valorApagar):
        vueltos = dinero - valorApagar
        print(f"Sus vueltos son {vueltos} muchas gracias por su compra")
    else:
        print(f"Su dinero es insuficiente")
else: 
    print (f"Seleccione una Promocion del producto {datosCategoria.get('Producto')[opcionProducto]}")
    for i , val in enumerate(promocionProductos):
        print(f"{i}. {val}")
    print(f"{len(promocionProductos)}.Salir")
    opcionPromocion = int(input())
    if (opcionPromocion != len(promocionProductos)):
        producto = datosCategoria.get('Producto')[opcionProducto]
        nombreProducto = producto.get("nombre")
        productoValor = producto.get("valor")
        nombrePromocion = promocionProductos[opcionPromocion].get("nombre")
        descuentoPromocion = promocionProductos[opcionPromocion].get ("descuento")
        unidadesPromocion = promocionProductos[opcionPromocion].get ("unidades")
        valorApagar = (unidadesPromocion * productoValor) - ((unidadesPromocion * productoValor) * descuentoPromocion)
        print(f"{nombrePromocion} del producto {datosCategoria.get('producto')[opcionProducto]} total a pagar ${round(valorApagar)}")
        dinero = int(input("ingrese su dinero : "))
        if (dinero >= valorApagar):
            vueltos = dinero - valorApagar
            print(f"el valor a pagar es de {valorApagar} de la promocion {promocionProductos[opcionPromocion]}")
            print(f"Sus vueltos son {vueltos} muchas gracias por su compra")
        else:
            print(f"Su dinero es insuficiente")
    else :
        producto = datosCategoria.get('Producto')[opcionProducto]
    nombreProducto = producto.get("nombre")
    productoValor = producto.get("valor")
    cantidad = int(input(f"Usuario cuantos{producto} desea?: "))
    valorApagar = cantidad * productoValor
    print(f"Usuario su producto{nombreProducto}tiene un valor de ${productoValor} la cantidad solicitada es de {cantidad} que da un total de ${round(valorApagar)} ")
    dinero = int(input("ingrese su dinero : "))
    if (dinero >= valorApagar):
        vueltos = dinero - valorApagar
        print(f"Sus vueltos son {vueltos} muchas gracias por su compra")
    else:
        print(f"Su dinero es insuficiente")


        
#if opcioncategoria == 0:
#    valorProducto = (menu.get("pan").get("Producto")["valor"])
    #print(menu.get("Pan").get("Producto"))
#    print("seleccione el producto : ")
#    for i, val in enumerate(menu.get("Pan").get("Producto")):
#        print(f"{i}. {val}")
#    opcionProducto = int(input())
#    if opcionProducto == 8 :
#        print(f"Hay una promocion de {menu.get('Pan').get('Promociones1')[0]}")
#        deseaPromocion = int(input("¿Usuario desea la promocion? "))
#        for i in enumerate("si", "no") :
#            if deseaPromocion == 0 :
#                valorPromocion1 = int(25000)
#                print(f"seria un total de {valorPromocion1}") 
#                dinero = int(input("Ingrese su dinero :"))
#            if dinero >= valorUnidades :
#                vueltos = dinero - valorUnidades
#                print (f"sus vueltos son {vueltos}")
#            elif dinero < valorUnidades :
#                print ("no tiene dinero suficiente, gracias por su compra")
#            elif deseaPromocion == 1 :
#                cantUnidades = int(input(f"cuantas unidades desea llevar del producto elegido"))
#            valorUnidades = cantUnidades * valorProducto
#            print(f"Seria un total de {cantUnidades} por un precio de {valorUnidades}")
#            dinero = int(input("Ingrese su dinero :"))
#            if dinero >= valorUnidades :
#                vueltos = dinero - valorUnidades
#                print (f"sus vueltos son {vueltos}")
#            elif dinero < valorUnidades :
#                print ("no tiene dinero suficiente, gracias por su compra")
#    elif opcionProducto == 5 :
#        print(f"Hay una promocion de {menu.get('Pan').get('Promociones1')[1]}")
#        deseaPromocion = int(input("¿Usuario desea la promocion? "))
#        for i in enumerate("si", "no") :
#            if deseaPromocion == 0 :
#                valorPromocion1 = int(8000)
#                print(f"seria un total de {valorPromocion1}") 
#                dinero = int(input("Ingrese su dinero :"))
#            if dinero >= valorUnidades :
#                vueltos = dinero - valorUnidades
#                print (f"sus vueltos son {vueltos}")
#            elif dinero < valorUnidades :
#                print ("no tiene dinero suficiente, gracias por su compra")
#            elif deseaPromocion == 1 :
#                cantUnidades = int(input(f"cuantas unidades desea llevar del producto elegido"))
#            valorUnidades = cantUnidades * valorProducto
#            print(f"Seria un total de {cantUnidades} por un precio de {valorUnidades}")
#            dinero = int(input("Ingrese su dinero :"))
#            if dinero >= valorUnidades :
#                vueltos = dinero - valorUnidades
#                print (f"sus vueltos son {vueltos}")
#            elif dinero < valorUnidades :
#                print ("no tiene dinero suficiente, gracias por su compra")
#elif opcioncategoria == 1:
#    print("seleccione el producto : ")
#    for i, val in enumerate(menu.get("Pasteles").get("Productos")):
#        print(f"{i}. {val}")
#    opcionProducto = int(input())

#elif opcioncategoria == 2:
#    print("seleccione el producto : ")
#    for i, val in enumerate(menu.get("Galletas").get("Productoss")):
#        print(f"{i}. {val}")
#    opcionProducto = int(input())










    
