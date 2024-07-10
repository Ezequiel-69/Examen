import funciones as fn

trabajadores = [
    "Juan Pérez", "María García","Carlos López","Ana Martínez","Pedro Rodríguez","Laura Hernández","MiguelSánchez"
    ,"Isabel Gómez","Francisco Díaz","Elena Fernández"]

dic_sueldo = {}

while True:
    
    print("0. Iicializar sueldos")
    print("1. Asignar sueldos aleatorios")
    print("2. Clasificar sueldos")
    print("3. Ver estadísticas")
    print("4. Reporte de sueldos")
    print("5. Salir del programa")

    try:
        opcion = int(input("Eliga una opcion: "))

        if opcion == 0:
            dic_sueldo = {trabajador :0 for trabajador in trabajadores}
            print(dic_sueldo)

        elif opcion == 1:
            if not dic_sueldo:
                print("No has inicializado los sueldos")
            else:
                dic_sueldo = fn.Asignar_sueldos_aleatorios(trabajadores)

        elif opcion == 2:
            if dic_sueldo:
                fn.Clasificar_sueldos(dic_sueldo)
            else:
                print("No has inicializado los sueldos")

        elif opcion == 3:
            if dic_sueldo:
                fn.Ver_estadísticas(dic_sueldo)
            else:
                print("No has inicializado los sueldos")
        elif opcion == 4:
            if dic_sueldo:
                fn.Reporte_de_sueldos(dic_sueldo)
            else:
                print("No has inicializado los sueldos")
        elif opcion == 5:
            print("saliendo del programa...")
            print("Desarrollado por EZequiel Aceituno")
            print("Rut: 21.884.298-4")

            break
        elif opcion > 5:
            print("Debe ingresar una opcion entre 0 y 5")
    except ValueError:
        print("Debe ingresar un numero")