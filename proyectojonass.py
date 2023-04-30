from os import system
system("cls")

peliculas = [["SpiderMan",10000],
             ["Matrix",10000],
             ["Scream",10000]]

Combos = [["Personal", 12000], 
          ["Para Dos", 20000], 
          ["Familiar", 30000]]

agregados = [["Gaseosa", 2500], 
             ["Palomitas", 5000], 
             ["Hot-Dog", 4500]]

lista_compras = []

def combos_disp():
    num = 0
    print(" _____________________________")
    print("|------Combos disponibles-----|")
    print("+-----------------------------+")
    for combo, precio in Combos:
        num = num + 1
        print(f"|{num}) {combo}:\t\t${precio:.0f}|")
        print("+-----------------------------+")

def peliculas_disp():
    num = 0
    print(" _____________________________")
    print("|----Películas disponibles----|")
    print("+-----------------------------+")
    for pelicula, precio in peliculas:
        num = num + 1
        print(f"|{num}) {pelicula}:\t\t${precio:.0f}|")
        print("+-----------------------------+")

def agregadoss():
    num = 0
    print(" _____________________________")
    print("|----Agregados disponibles----|")
    print("+-----------------------------+")
    for comida, precio in agregados:
        num = num + 1
        print(f"|{num}) {comida}:\t\t${precio:.0f}|")
        print("+-----------------------------+")

def menu():
    print(" ______________________")
    print("|--Bienvenido al cine--|")
    print("+----------------------+")
    print("+     (1) - Cajero     +")
    print("+----------------------+")
    print("+     (2) - Cliente    +")
    print("+----------------------+")
    print("+     (3) - Salir      +")
    print("+----------------------+")

def cajero():
    while True:
        system("cls")
        print(" ______________________________")
        print("|------Menú de Cajero----------|")
        print("+------------------------------+")
        print("+  (1) - Agregar película      +")
        print("+------------------------------+")
        print("+  (2) - Editar película       +")
        print("+------------------------------+")
        print("+  (3) - Eliminar película     +")
        print("+------------------------------+")
        print("+  (4) - historial de compras  +")
        print("+------------------------------+")
        print("+  (5) - Salir                 +")
        print("+------------------------------+")
        try:
            opcion = int(input("\nIngrese una opción: "))
            if opcion == 1:
                system("cls")
                nombre = input("Ingrese el nombre de la película: ")
                try:
                    precio_pelicula = float(input("Ingrese el precio de la película: "))
                    if precio_pelicula < 10000 or precio_pelicula >= 100000:
                        print("Error: El precio debe ser mayor o igual a 10000 y menor a 100000.")
                        input("precione Enter")
                    else:
                        anadir = [[nombre,precio_pelicula]]
                        peliculas.extend(anadir)
                        print(f"La película {nombre} ha sido agregada con éxito.")
                        input("precione Enter")
                except ValueError:
                    print("Error: El precio debe ser un número.")
                    input("precione Enter")

            elif opcion == 2:
                system("cls")
                peliculas_disp()
                try:
                    nombre = int(input("Ingrese el numero de la película a editar: "))
                    if nombre > 0 or nombre <= len(peliculas):
                        nombrerel = nombre - 1
                        print(f"Precio actual de {peliculas[nombrerel][0]}: {peliculas[nombrerel][1]}")
                        try:
                            precio_pelicula = float(input("Ingrese el precio de la película: "))
                            if precio_pelicula < 10000 or precio_pelicula >= 100000:
                                print("Error: El precio debe ser mayor o igual a 10000 y menor a 100000.")
                                input("precione Enter")
                            else:
                                peliculas[nombrerel][1] = precio_pelicula
                                print(f"La película {nombre} ha sido agregada con éxito.")
                                input("precione Enter")
                        except ValueError:
                            print("Error: El precio debe ser un número.")
                            input("precione Enter")
                    else:
                        print("Error: La película no existe en el sistema.")
                        input("precione Enter")
                except ValueError:
                    print("el valor deve ser numérico")
                    input("Presione Enter")

            elif opcion == 3:
                system("cls")
                peliculas_disp()
                try:
                    nombre = int(input("Ingrese el numero de la película a eliminar: "))
                    nombrerel = nombre - 1
                    if nombre > 0 or nombre <= len(peliculas):
                        del peliculas[nombrerel]
                        print("La película se eliminó exitosamente.")
                        input("precione Enter")
                    else:
                        print("Error: La película no existe en el sistema.")
                        input("precione Enter")
                except ValueError:
                    print("el valor deve ser numérico")
                    input("Presione Enter")

            elif opcion == 4:
                system("cls")
                print("-----Historial de compras-----\n")
                for compra in lista_compras:
                    print(f"-Pelicula: {compra[0]}, cantidad: {compra[1]}\nCliente: {compra[2]}, Documento de identidad: {compra[3]}\n-Cobo Elegido: {compra[5]}, Agregados: {compra[4]}")
                    print(f"-Precio total: ${compra[6]}\n")
                input("precione Enter")
            elif opcion == 5:
                system("cls")
                break
            else:
                print("Opción inválida. Intente de nuevo.")
                input("precione Enter")
        except ValueError:
            print("Error: La opción debe ser un número.")
            input("precione Enter")

def cliente():
    system("cls")
    peliculas_disp()
    while True:
        try:
            pelicula_elegida = int(input("\nIngrese el numero de la película que desea ver: "))
            break
        except ValueError:
            print("Error: Ingrese un valor numérico para la pelicula.")

    while pelicula_elegida> len(peliculas):
        system("cls")
        peliculas_disp()
        try:
            pelicula_elegida = int(input("\nLa película ingresada no está en cartelera, Intente Nuevamente: "))
        except ValueError:
            print("Error: Ingrese un valor numérico para la pelicula.")
        
    while True:
        try:
            cantidad = int(input("\nIngrese la cantidad de boletos que desea comprar: "))
            break
        except ValueError:
            print("Error: Ingrese un valor numérico para la cantidad de boletos.")
    
    while True:
        system("cls")
        try:
            print("Desea comprar un combo? (1)si, (2)no")
            sionocmbo = int(input("---> "))

            if sionocmbo == 1:
                system("cls")
                combos_disp()
                while True:
                    try:
                        combo_elegido = int(input("\nIngrese el numero del combo que desea comprar: "))
                        combober = combo_elegido - 1
                        combonom = Combos[combober][0]
                        prescomb = Combos[combober][1]

                        break
                    except ValueError:
                        print("Error: Ingrese un valor numérico para el combo.")

                while combo_elegido> len(Combos):
                    system("cls")
                    combos_disp()
                    try:
                        combo_elegido = int(input("El combo ingresada no está disponible, Intente Nuevamente: "))
                    except ValueError:
                        print("Error: Ingrese un valor numérico para el combo.")

                input("Combo agregado, Presione Enter: ")

                cosascom = []
                preciocom = []

                while True:
                    system("cls")
                    print("Desea comprar un agregado? (1)si, (2)no")
                    while True:
                        try:
                            sionoafg = int(input("---> "))
                            break
                        except ValueError:
                                print("Error: Ingrese un valor numérico para los agregados.")
                                input("Presione Enter: ")
                    system("cls")
                    if sionoafg == 1:
                        while True:
                            system("cls")
                            agregadoss()
                            try:
                                agre_elegido = int(input("\nIngrese el numero del agregado que desea comprar: "))

                                if agre_elegido> len(agregados):
                                    print("Ingrese un numero valido")
                                    input("Presione Enter: ")
                                else:
                                    agreber = agre_elegido - 1
                                    agrenom = agregados[agreber][0]
                                    agreomb = agregados[agreber][1]
                                    cosascom.append(agrenom)
                                    preciocom.append(agreomb)
                                    break

                            except ValueError:
                                print("Error: Ingrese un valor numérico para el combo.")
                                input("Presione Enter: ")

                        try:
                            seguiresto = int(input("\nDesea seguir comprando? (1)si, (2)no\n---> "))

                            if seguiresto == 1:
                                print("okey")
                                input("Presione Enter: ")
                            elif seguiresto == 2:
                                sumlist = sum(preciocom)
                                print(*cosascom,sumlist)
                                print("\nokey")
                                input("Presione Enter: ")
                                break
                            else:
                                print("Ingrese un numero valido")
                                input("Presione Enter: ")

                        except ValueError:
                            print("Error: Ingrese un valor numérico para el combo.")
                            input("Presione Enter: ")

                    elif sionoafg == 2:
                        print("okey")
                        input("Presione Enter: ")
                        break
                    else:
                        print("El numero no es valido")
                        input("Presione Enter: ")

                break
                        
            elif sionocmbo == 2:
                prescomb = 0

                print("okey")
                input("Presione Enter: ")
                break
            else:
                print("El numero no es valido")
                input("Presione Enter: ")
        except ValueError:
            print("Error: La opción debe ser un número.")
            input("precione Enter")

    system("cls")
    nombre = input("Ingrese su nombre y apellido: ")
    while True:
        system("cls")
        try:
            while True:
                identidad = int(input("Ingrese su documento de identidad: "))
                if identidad < 10000000 or identidad >= 10000000000:
                    input("La cantidad de dígitos en el documento es invalida\nPresione Enter: ")
                else:
                    input("El documento esta guardado\nPresione Enter: ")
                    break
            break
        except ValueError:
            print("Error: Ingrese un valor numérico para el documento de identidad.")
            input("precione Enter")
    
    pelinomber = pelicula_elegida - 1
    pelinom = peliculas[pelinomber][0]

    system("cls")

    if sionocmbo == 1:
        
        if sionoafg ==1:

            precio_total = (prescomb + (peliculas[pelinomber][1] * cantidad)) + sumlist

            compra = (pelinom, cantidad, nombre, identidad, cosascom, combonom, precio_total)
            lista_compras.append(compra)

            print("Recibo de pago:\n")
            print(f"-Total a pagar por: {cantidad} boletos de {pelinom} y el combo {combonom}")
            print("-Añadidos: ",*cosascom, sep = ',')
            print(f"\n-Total: ${precio_total:.0f}\n")
            print(f"-Cliente: {nombre}\n-Documento de identidad: {identidad}")
            input("\nGracias por su compra")

        elif sionoafg ==2:

            precio_total = prescomb + (peliculas[pelinomber][1] * cantidad)

            compra = (pelinom, cantidad, nombre, identidad, "Sin agregados", combonom, precio_total)
            lista_compras.append(compra)

            print("Recibo de pago:\n")
            print(f"-Total a pagar por: {cantidad} boletos de {pelinom} y el combo {combonom}")
            print(f"\n-Total: ${precio_total:.0f}\n")
            print(f"-Cliente: {nombre}\n-Documento de identidad: {identidad}")
            input("\nGracias por su compra")

    elif sionocmbo == 2:

        precio_total = peliculas[pelinomber][1] * cantidad

        compra = (pelinom, cantidad, nombre, identidad, "Sin agregados", "Sin combo registrado", precio_total)
        lista_compras.append(compra)

        print("Recibo de pago:\n")
        print(f"-Total a pagar por: {cantidad} boletos de {pelinom}, sin combo")
        print(f"\n-Total: ${precio_total:.0f}\n")
        print(f"-Cliente: {nombre}\n-Documento de identidad: {identidad}")
        input("\nGracias por su compra")

while True:
    try:
        while True:
            system("cls")
            menu()
            opcion = int(input("\nIngrese una opción: "))
            if opcion == 1:
                cajero()
            elif opcion == 2:
                cliente()
            elif opcion == 3:
                system("cls")
                print("\nOkey")
                break
            else:
                print("Opción inválida. Intente de nuevo.")
                input("precione Enter")
        break
    except ValueError:
        system("cls")
        print("Error: La opción debe ser un número.")
        input("precione Enter")