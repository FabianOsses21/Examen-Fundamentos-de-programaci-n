
import random
import csv

trabajadores = ["Juan Pérez", 
                "María García",
                  "Carlos López",
                    "Ana Martínez",
                      "Pedro Rodríguez",
                        "Laura Hernández",
                          "Miguel Sánchez", 
                          "Isabel Gómez", 
                          "Francisco Díaz",
                            "Elena Fernández"]
sueldos = {}

def asignar_sueldos_aleatorios(trabajadores):
    sueldos = {trabajador: random.randint(300000, 2500000) for trabajador in trabajadores}
    print("Sueldos aleatorios asignados:")
    for trabajador, sueldo in sueldos.items():
        print("Nombre empleado Sueldo")
        print(f"{trabajador}: ${sueldo}")
        print(" ")
    return sueldos

def clasificar_sueldos(sueldos):
    clasificacion = {"Menores a $800.000": [], "Entre $800.000 y $2.000.000": [], "Superiores a $2.000.000": []}

    for trabajador, sueldo in sueldos.items():
        if sueldo < 800000:
            clasificacion["Menores a $800.000"].append((trabajador, sueldo))
        elif sueldo < 2000000:
            clasificacion["Entre $800.000 y $2.000.000"].append((trabajador, sueldo))
        else:
            clasificacion["Superiores a $2.000.000"].append((trabajador, sueldo))
    print(" ")
    print("Clasificación de sueldos:")
    for categoria, empleados in clasificacion.items():
        print(f"{categoria} - Total: {len(empleados)}")
        for trabajador, sueldo in empleados:
            print(f"{trabajador}: {sueldo}")
        print()

    print(f"Total sueldos: {sum(sueldos.values())}")

def ver_estadisticas(sueldos):
    # Sueldo más alto
    sueldo_mas_alto = max(sueldos.values())
    print(" ")
    print(f"Sueldo más alto: {sueldo_mas_alto}")
    print(" ")
    # Sueldo más bajo
    sueldo_mas_bajo = min(sueldos.values())
    print(f"Sueldo más bajo: {sueldo_mas_bajo}")
    print(" ")
    # Promedio de sueldos
    promedio_sueldos = round(sum(sueldos.values()) / len(sueldos), 2)
    print(f"Promedio de sueldos: {promedio_sueldos}")
    print(" ")
    # Media geométrica
    producto_sueldos = 1
    for sueldo in sueldos.values():
        producto_sueldos *= sueldo
    media_geometrica = round(producto_sueldos ** (1.0 / len(sueldos)), 2)
    print(f"Media geométrica: {media_geometrica}")

def reporte_sueldos(sueldos):
    with open('sueldos.csv', 'w', encoding='utf-8') as archivo_csv:
        escritor_csv = csv.writer(archivo_csv, delimiter=",")
        escritor_csv.writerow(['Nombre empleado', 'Sueldo base', 'Descuento salud', 'Descuento AFP', 'Sueldo líquido'])
        
        for trabajador, sueldo in sueldos.items():
            descuento_salud = round(sueldo * 0.07)
            descuento_afp = round(sueldo * 0.12)
            sueldo_liquido = round(sueldo - descuento_salud - descuento_afp)
            
            escritor_csv.writerow([trabajador, round(sueldo, 2), descuento_salud, descuento_afp, sueldo_liquido])

def menu():
    exit = False
    sueldos = {}

    while not exit:
        print(" ")
        print("Menú:")
        print("1. Asignar sueldos aleatorios")
        print("2. Clasificar sueldos")
        print("3. Ver estadísticas")
        print("4. Reporte de sueldos")
        print("5. Salir del programa")

        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            sueldos = asignar_sueldos_aleatorios(trabajadores)
        elif opcion == "2":
            if sueldos:  # Ver si sueldos no está vacío
                clasificar_sueldos(sueldos)
            else:
                print("Debe asignar sueldos aleatorios primero.")
        elif opcion == "3":
            if sueldos:  
                ver_estadisticas(sueldos)
            else:
                print("Debe asignar sueldos aleatorios primero.")
        elif opcion == "4":
            if sueldos:  
                reporte_sueldos(sueldos)
            else:
                print("Debe asignar sueldos aleatorios primero.")
        elif opcion == "5":
            exit = True
            print("Saliendo del programa")
            print("Desarrollado por Fabián Osses")
            print("Rut 20.147.555-4")
           
        else:
            print("Opción inválida. Intente nuevamente.")
menu()
