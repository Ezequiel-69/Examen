import random
import csv

def Asignar_sueldos_aleatorios(trabajadores):
    dic_sueldo = {}
    for trabajador in trabajadores:
        sueldo = random.randint(300000,2500000)
        dic_sueldo[trabajador] = sueldo
    
    print(dic_sueldo)

    return dic_sueldo

def Clasificar_sueldos(dic_sueldo):
    sueldo = dic_sueldo.values()
    total = sum(sueldo)

    menor800K = {}
    entre800K2M = {}
    mayor2M = {}

    for trabajador, sueldo in dic_sueldo.items():
        if sueldo < 800000:
            menor800K[trabajador] = sueldo
        elif sueldo <= 2000000:
            entre800K2M[trabajador] = sueldo
        else:
            mayor2M[trabajador] = sueldo
    print("                              ")
    print("Sueldos menores a 800.000",len(menor800K))
    for trabajador, sueldo in menor800K.items():
        print(trabajador,": $",sueldo)
    print("                              ")
    print("Sueldos entre 800.000 y 2.000.000",len(entre800K2M))
    for trabajador, sueldo in entre800K2M.items():
        print(trabajador,": $",sueldo)
    print("                              ")
    print("Sueldos mayores a 2.000.000",len(mayor2M))
    for trabajador, sueldo in mayor2M.items():
        print(trabajador,": $",sueldo)
    print("                              ")
    print("Suma total de sueldos: ",total)
    print("                              ")

def Ver_estadísticas(dic_sueldo):
    sueldo= dic_sueldo.values()

    sueldoMas = max(sueldo)
    sueldoMenos = min(sueldo)
    promsueldos = sum(sueldo) /2

    print("El sueldo mas alto es: ",sueldoMas)
    print("El sueldo mas bajo es: ",sueldoMenos)
    print("El promedio de los sueldo es: ",promsueldos)

def Reporte_de_sueldos(dic_sueldo):

    with open("reporte_de_sueldos","w", newline="") as archivo:
        escritor = csv.writer(archivo, delimiter=",")
        escritor.writerow(["Nobre de Empleado","Sueldo"])
        for trabajador,sueldo in dic_sueldo.items():
            escritor.writerow([trabajador,sueldo])
    print("Reporte generado excitosamente")