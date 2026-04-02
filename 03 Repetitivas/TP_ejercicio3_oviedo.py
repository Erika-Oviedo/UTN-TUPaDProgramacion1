#Ejercicio 3 (Alta) — “Agenda de Turnos con Nombres (sin listas)”
#Contexto
#Hay 2 días de atención: Lunes y Martes.
#Cada día tiene cupos fijos:
#• Lunes: 4 turnos
#• Martes: 3 turnos
#Reglas
#1. Pedir nombre del operador (solo letras).
#2. Menú repetitivo hasta salir:
#1. Reservar turno
#2. Cancelar turno (por nombre)
#3. Ver agenda del día
#4. Ver resumen general
#5. Cerrar sistema
lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""

martes1 = ""
martes2 = ""
martes3 = ""


while True:
    nombre_operador = input("Ingrese el nombre del operador: ").strip().lower()
    if(nombre_operador.isalpha() and nombre_operador != ""):
        print(f"Operador: {nombre_operador}")
        break
    else:
        print("¡Por favor ingrese su nombre solo con letras!")

opcion = 0

while opcion != "5":
    print("""\n--- MENÚ DE TURNOS ---
1.Reservar turno
2.Cancelar turno (por nombre)
3.Ver agenda del día
4.Ver resumen general
5.Cerrar sistema """)
    opcion = input("Ingrese una opción: ")
    match opcion:
        case "1":
            while True:
                print("""\n--- DÍAS DE ATENCIÓN ---
1) Lunes
2) Martes""")
                dia = input("Seleccione el día: ")
                if dia in ("1", "2"):
                    break
                else:
                    print("Ingrese el DÍA solo con el número 1 o 2 según corresponda.")
            if dia == "1":
                while True:
                    paciente = input("Ingrese el nombre del paciente: ").strip().lower()
                    if(paciente.isalpha() and paciente != ""):
                        print(f"Paciente: {paciente}")
                        break
                    else:
                        print("¡Por favor ingrese el nombre solo con letras!")

                if paciente == lunes1 or paciente == lunes2 or paciente == lunes3 or paciente == lunes4:
                    print("Nombre repetido")
                else:
                    guardado = False

                    if lunes1 == "":   
                        lunes1 = paciente
                        guardado = True
                    elif lunes2 == "":
                        lunes2 = paciente
                        guardado = True
                    elif lunes3 == "":
                        lunes3 = paciente
                        guardado = True
                    elif lunes4 == "":
                        lunes4 = paciente
                        guardado = True

                    if guardado:
                        print("Nombre guardado correctamente")
                    else:
                        print("No hay espacio disponible")

            elif dia == "2":
                while True:
                    paciente = input("Ingrese el nombre del paciente: ").strip().lower()
                    if(paciente.isalpha() and paciente != ""):
                        print(f"Paciente: {paciente}")
                        break
                    else:
                        print("¡Por favor ingrese el nombre solo con letras!")
                if paciente == martes1 or paciente == martes2 or paciente == martes3:
                    print("Nombre repetido")
                else:
                    guardado = False

                    if martes1 == "":
                        martes1 = paciente
                        guardado = True
                    elif martes2 == "":
                        martes2 = paciente
                        guardado = True
                    elif martes3 == "":
                        martes3 = paciente
                        guardado = True
                                
                    if guardado:
                        print("Nombre guardado correctamente")
                    else:
                        print("No hay espacio disponible")
        case "2":
            print("Opción para cancelar turno:")
            while True:
                print("""\n--- DÍAS DE ATENCIÓN ---
1) Lunes
2) Martes""")
                dia = input("Seleccione el día: ")
                if dia in ("1", "2"):
                    break
                else:
                    print("Ingrese el DÍA solo con el número 1 o 2 según corresponda.")
            if dia == "1":
                while True:
                    cancelar = input("Ingrese el nombre del paciente: ").strip().lower()
                    if(cancelar.isalpha() and cancelar != ""):
                        print(f"Paciente: {cancelar}")
                        break
                    else:
                        print("¡Por favor ingrese el nombre solo con letras!")
                if cancelar == lunes1:
                    lunes1 = ""
                    print("Cancelar turno 1")
                elif cancelar == lunes2:
                    lunes2 = ""
                    print("Cancelar turno 2")
                elif cancelar == lunes3:
                    lunes3 = ""
                    print("Cancelar turno 3")
                elif cancelar == lunes4:
                    lunes4 = ""
                    print("Cancelar turno 4")               
                else:
                    print("Nombre no encontrado")
            elif dia == "2":
                while True:
                    cancelar = input("Ingrese el nombre del paciente: ").strip().lower()
                    if(cancelar.isalpha() and cancelar != ""):
                        print(f"Paciente: {cancelar}")
                        break
                    else:
                        print("¡Por favor ingrese el nombre solo con letras!")
                if cancelar == martes1:
                    martes1 = ""
                    print("Cancelar turno 1")
                elif cancelar == martes2:
                    martes2 = ""
                    print("Cancelar turno 2")
                elif cancelar == martes3:
                    martes3 = ""
                    print("Cancelar turno 3")
                else:
                    print("Nombre no encontrado")

        case "3":
            while True:
                print("""\n--- DÍAS DE ATENCIÓN ---
1) Lunes
2) Martes""")
                dia = input("Seleccione el día: ")
                if dia in ("1", "2"):
                    break
                else:
                    print("Ingrese el DÍA solo con el número 1 o 2 según corresponda.")
            if dia == "1":
                print("\n--- AGENDA LUNES ---")
                print(f"1. {lunes1 if lunes1 != '' else 'Libre'}")
                print(f"2. {lunes2 if lunes2 != '' else 'Libre'}")
                print(f"3. {lunes3 if lunes3 != '' else 'Libre'}")
                print(f"4. {lunes4 if lunes4 != '' else 'Libre'}")

            elif dia == "2":
                print("\n--- AGENDA MARTES ---")
                print(f"1. {martes1 if martes1 != '' else 'Libre'}")
                print(f"2. {martes2 if martes2 != '' else 'Libre'}")
                print(f"3. {martes3 if martes3 != '' else 'Libre'}")
        case "4":
            total = 0
            ocupados_lunes = 0
            if lunes1 != "": ocupados_lunes += 1
            if lunes2 != "": ocupados_lunes += 1
            if lunes3 != "": ocupados_lunes += 1
            if lunes4 != "": ocupados_lunes += 1

            libres_lunes = 4 - ocupados_lunes

            ocupados_martes = 0
            if martes1 != "": ocupados_martes += 1
            if martes2 != "": ocupados_martes += 1
            if martes3 != "": ocupados_martes += 1

            libres_martes = 3 - ocupados_martes

            print("\n--- RESUMEN GENERAL ---")
            print(f"Lunes → Ocupados: {ocupados_lunes} | Libres: {libres_lunes}")
            print(f"Martes → Ocupados: {ocupados_martes} | Libres: {libres_martes}")

            if ocupados_lunes > ocupados_martes:
                print("Día con más turnos: Lunes")
            elif ocupados_martes > ocupados_lunes:
                print("Día con más turnos: Martes")
            else:
                print("Día con más turnos: Empate")
            total = ocupados_lunes + ocupados_martes
            print(f"Total de turnos reservados: {total}")
        case "5":
            print("Cerrando sistema...")
        case _:
            print("¡Opción Incorrecta!")