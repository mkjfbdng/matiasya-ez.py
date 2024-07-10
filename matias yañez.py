import random

# Lista de empleados
trabajadores = ["Juan Pérez", "María García", "Carlos López", "Ana Martínez", 
                "Pedro Rodríguez", "Laura Hernández", "Miguel Sánchez", 
                "Isabel Gómez", "Francisco Díaz", "Elena Fernández"]

sueldos = [0] * len(trabajadores)

def asignar_sueldos_aleatorios():
    global sueldos
    sueldos = [random.randint(300000, 2500000) for _ in range(len(trabajadores))]

def clasificar_sueldos():
    sueldos_ordenados = sorted(sueldos)
    for i, sueldo in enumerate(sueldos_ordenados):
        print(f"{i+1}. {trabajadores[sueldos.index(sueldo)]}: ${sueldo}")

def ver_estadisticas():
    total = sum(sueldos)
    promedio = total / len(trabajadores)
    menor = min(sueldos)
    mayor = max(sueldos)
    
    print(f"Total de sueldos: ${total}")
    print(f"Promedio de sueldos: ${promedio:.2f}")
    print(f"Sueldo más bajo: ${menor}")
    print(f"Sueldo más alto: ${mayor}")

def generar_reporte():
    print("Nombre empleado | Sueldo Base | Descuento Salud | Descuento AFP | Sueldo Líquido")
    print("-" * 80)
    for i in range(len(trabajadores)):
        sueldo_base = sueldos[i]
        descuento_salud = sueldo_base * 0.07
        descuento_afp = sueldo_base * 0.12
        sueldo_liquido = sueldo_base - descuento_salud - descuento_afp
        
        print(f"{trabajadores[i]:15} | ${sueldo_base:11,} | ${descuento_salud:14,.2f} | ${descuento_afp:12,.2f} | ${sueldo_liquido:13,.2f}")
def main():
    while True:
        print("\nMenú:")
        print("1. Asignar sueldos aleatorios")
        print("2. Clasificar sueldos")
        print("3. Ver estadísticas")
        print("4. Reporte de sueldos con descuentos")
        print("5. Salir del programa")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            asignar_sueldos_aleatorios()
            print("Sueldos asignados aleatoriamente.")
        elif opcion == "2":
            clasificar_sueldos()
        elif opcion == "3":
            ver_estadisticas()
        elif opcion == "4":
            generar_reporte()
        elif opcion == "5":
            print("Finalizando el programa...")
            print("Gracias por usar este programa.")
            print("Desarrollado por Matías Yáñez")
            print("RUT: 21.837.722-K")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
