#Ejercicio 4 — “Escape Room: La Bóveda”
#Historia
#Sos un agente que intenta abrir una bóveda con 3 cerraduras. Tenés energía y tiempo
#limitados.
#Si abrís las 3 cerraduras antes de quedarte sin energía o sin tiempo, ganás.

energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
intento = 0

while True:
    agente = input("Ingresar el nombre del agente: ").strip().lower()
    if agente.isalpha():
        print(f"Agente: {agente}")
        break
    else:
        print("¡Por favor ingrese el nombre del agente solo con letras!")

opcion = 0
while opcion != "4":
    print("""\n--- MENÚ DE TURNOS ---
1.Forzar cerradura
2.Hackear panel
3.Descansar
4.Adios!
""")
    opcion = input("Ingrese una opción: ")
    match opcion:
        case "1":
            print("FORZAR CERRADURA")

            energia -= 20
            tiempo -= 2
            energia = max(0, energia)
            tiempo = max(0, tiempo)

            intento += 1

            if intento == 3:
                alarma = True
                print("Se activó la ALARMA!!")
                print("CERRADURA BLOQUEADA")
                print(f"\nEnergía: {energia} | Tiempo: {tiempo} | Cerraduras: {cerraduras_abiertas}")
                continue

            if energia < 40:
                print("Riesgo de Alarma!!")
                while True:
                    riesgo = input("Ingrese un número (1-3): ")
                    if riesgo.isdigit() and riesgo in ("1", "2", "3"):
                        riesgo = int(riesgo)
                        break
                    else:
                        print("Número Inválido")

                if riesgo in ("1", "2"):
                    cerraduras_abiertas += 1
                    print("¡Cerradura Abierta!") 
                    continue
                elif riesgo == 3:
                    alarma = True
                    print("¡¡Alarma activada!!")
                    print("¡¡CERRADURA BLOQUEADA!!")
                    print(f"\nEnergía: {energia} | Tiempo: {tiempo} | Cerraduras: {cerraduras_abiertas}")
                    continue
            if not alarma:
                    cerraduras_abiertas += 1
                    print("¡Cerradura Abierta!") 
            print(f"\nEnergía: {energia} | Tiempo: {tiempo} | Cerraduras: {cerraduras_abiertas}")

        case "2":
            print("HACKEAR PANEL")
            intento = 0
            energia -= 10
            tiempo -= 3
            energia = max(0, energia)
            tiempo = max(0, tiempo)
            print(f"Código de la cerradura:{codigo_parcial}")
            for i in range(4):
                while True:
                    letra = input(f"Paso {i+1}/4 Ingresar una letra al código: ").strip()

                    if letra.isalpha():
                        break
                    else:
                        print("Error: Ingresá solo letras (sin números ni espacios)")

                codigo_parcial += letra
                print(f"Código de la cerradura: {codigo_parcial}")

                if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
                    cerraduras_abiertas += 1
                    print("¡Código completo! Se abrió una cerradura automáticamente 🔓")
                    break

            print(f"\nEnergía: {energia} | Tiempo: {tiempo} | Cerraduras: {cerraduras_abiertas}")

        case "3":
            print("DESCANSO")
            intento = 0
            energia += 15
            tiempo -= 1

            if alarma:
                energia -= 10
                print("La alarma consume energía extra")
            energia = min(100, energia)
            energia = max(0, energia)               

            print(f"\nEnergía: {energia} | Tiempo: {tiempo} | Cerraduras: {cerraduras_abiertas}")

        case "4":
            print("Adios Agente!!")
        case _:
            print("¡Opción Incorrecta!")

    if cerraduras_abiertas == 3:
        print("\nVICTORIA: Abriste la bóveda!")
        break

    if energia <= 0 or tiempo <= 0:
        print("\nDERROTA: Te quedaste sin recursos")
        break

    if alarma and tiempo <= 3 and cerraduras_abiertas < 3:
        print("\nDERROTA: La alarma bloqueó el sistema")
        break