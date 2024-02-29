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
        "Promociones1": list([
            {"codigo" :8, "Pan de centeno": "compre 10 unidades", "valor": 25000},
            {"codigo" :5, "Rosca de maiz": "compre 5 unidades", "valor": 8000},
            ])
    },
    "Pasteles": {
        "Productos" :list([
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
        "Promociones2": list([
            {"codigo" :6, "Empanada de frutas": "compre 3 unidades", "valor": 3500},
            {"codigo" :9, "Milhojas": "compre 5 unidades", "valor": 6500},
        ])
    },
    "Galletas": {
        "Productoss" :list([
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
        "Promociones3": list([
            {"codigo":9, "Galletas de jengibre": "compre 5 unidades", "valor": 4000},
            {"codigo":0, "Galletas de avena": "compre 4 unidades", "valor": 5000},
        ])
    }
})

print("seleccione la categoria")
listaCategoria = list( menu.keys())
for i, val in enumerate(listaCategoria):
    print(f"{i}. {val}")
opcioncategoria = int(input())

if opcioncategoria == 0:
    datosCategoria = (menu.get(listaCategoria)[opcioncategoria])
    valorProducto = (datosCategoria.get("Producto").get("valor"))
    #print(menu.get("Pan").get("Producto"))
    print("seleccione el producto : ")
    for i, val in enumerate(menu.get("Pan").get("Producto")):
        print(f"{i}. {val}")
    opcionProducto = int(input())
    if opcionProducto == 8 :
        print(f"Hay una promocion de {menu.get("Pan").get("Promociones1")[0]}")
        deseaPromocion = int(input("¿Usuario desea la promocion? "))
        for i in enumerate("si", "no") :
            if deseaPromocion == 0 :
                valorPromocion1 = int(25000)
                print(f"seria un total de {valorPromocion1}") 
                dinero = int(input("Ingrese su dinero :"))
            if dinero >= valorUnidades :
                vueltos = dinero - valorUnidades
                print (f"sus vueltos son {vueltos}")
            elif dinero < valorUnidades :
                print ("no tiene dinero suficiente, gracias por su compra")
            elif deseaPromocion == 1 :
                cantUnidades = int(input(f"cuantas unidades desea llevar del producto elegido"))
            valorUnidades = cantUnidades * valorProducto
            print(f"Seria un total de {cantUnidades} por un precio de {valorUnidades}")
            dinero = int(input("Ingrese su dinero :"))
            if dinero >= valorUnidades :
                vueltos = dinero - valorUnidades
                print (f"sus vueltos son {vueltos}")
            elif dinero < valorUnidades :
                print ("no tiene dinero suficiente, gracias por su compra")
    elif opcionProducto == 5 :
        print(f"Hay una promocion de {menu.get("Pan").get("Promociones1")[1]}")
        deseaPromocion = int(input("¿Usuario desea la promocion? "))
        for i in enumerate("si", "no") :
            if deseaPromocion == 0 :
                valorPromocion1 = int(8000)
                print(f"seria un total de {valorPromocion1}") 
                dinero = int(input("Ingrese su dinero :"))
            if dinero >= valorUnidades :
                vueltos = dinero - valorUnidades
                print (f"sus vueltos son {vueltos}")
            elif dinero < valorUnidades :
                print ("no tiene dinero suficiente, gracias por su compra")
            elif deseaPromocion == 1 :
                cantUnidades = int(input(f"cuantas unidades desea llevar del producto elegido"))
            valorUnidades = cantUnidades * valorProducto
            print(f"Seria un total de {cantUnidades} por un precio de {valorUnidades}")
            dinero = int(input("Ingrese su dinero :"))
            if dinero >= valorUnidades :
                vueltos = dinero - valorUnidades
                print (f"sus vueltos son {vueltos}")
            elif dinero < valorUnidades :
                print ("no tiene dinero suficiente, gracias por su compra")




elif opcioncategoria == 1:
    print("seleccione el producto : ")
    for i, val in enumerate(menu.get("Pasteles").get("Productos")):
        print(f"{i}. {val}")
    opcionProducto = int(input())

elif opcioncategoria == 2:
    print("seleccione el producto : ")
    for i, val in enumerate(menu.get("Galletas").get("Productoss")):
        print(f"{i}. {val}")
    opcionProducto = int(input())










    
