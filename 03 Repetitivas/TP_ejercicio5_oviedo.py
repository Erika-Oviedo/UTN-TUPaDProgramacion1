#Ejercicio 5 — “Escape Room:"La Arena del Gladiador"
#1. Descripción del Escenario
#Vas a desarrollar un simulador de batalla por turnos en Python. El programa enfrentará a un
#usuario (Gladiador) contra un oponente controlado por la computadora (Enemigo). El
#objetivo es reducir los puntos de vida del oponente a cero antes de que él lo haga contigo.
#Este ejercicio evalúa el uso de variables (int, float, string, boolean), estructuras de
#control (if/elif/else), ciclos (while y for) y validación de datos estricta. 
vida_gladiador = 100
vida_enemigo = 100
pocion_vida = 3
daño_ataque_pesado = 15
daño_enemigo = 12
turno_gladiador = True

while True:
    print("--- BIENVENIDO A LA ARENA ---")
    gladiador = input("Ingresar el nombre del gladiador: ").strip()
    
    if gladiador.isalpha():
        print(f"Nombre del Gladiador: {gladiador}")
        break
    else:
        print("Error: Solo se permiten letras")
print(f"""\n=== INICIO DEL COMBATE === 
{gladiador} (HP: {vida_gladiador}) vs Enemigo (HP: {vida_enemigo}) | Pociones:{pocion_vida}
""")
opcion = 0
while vida_gladiador > 0 and vida_enemigo > 0:

    if turno_gladiador:
        print("""--- ELIGE UNA ACCIÓN ---
1.Ataque Pesado
2.Ráfaga Veloz
3.Curar
""")
        while True:
            opcion = input("Opción: ")
            if opcion.isdigit() and opcion in ("1", "2", "3"):
                opcion = int(opcion)
                break
            else:
                print("Número Inválido")
        match opcion:
            case 1:
                daño_critico = daño_ataque_pesado
                if vida_enemigo < 20:
                    daño_critico *= 1.5
                    vida_enemigo -= daño_critico
                    print(f"¡Atacaste al enemigo por {daño_critico} puntos de daño!" )
                else:
                    print("¡No se pudo realizar el ataque!")
            case 2:
                print(">> ¡Inicias una ráfaga de golpes! ")
                for i in range(3):
                    vida_enemigo -= 5
                    print(f"> Golpe conectado por 5 de daño")
            case 3:
                print("Curación por poción")
                if pocion_vida > 0:

                    vida_gladiador = min(100, vida_gladiador + 30)
                    pocion_vida -= 1
                    print(f"Tu vida ahora tiene {vida_gladiador} puntos.")
                elif pocion_vida == 0:
                    print("¡No quedan pociones!")

        if vida_enemigo <= 0:
            break
    else:
        print("\n--- TURNO DEL ENEMIGO ---")
        vida_gladiador -= daño_enemigo
        print(">> ¡El enemigo contraataca por 12 puntos!" )
        print(f"""\n=== NUEVO TURNO === 
{gladiador} (HP: {vida_gladiador}) vs Enemigo (HP: {vida_enemigo}) | Pociones:{pocion_vida}
""")
    turno_gladiador = not turno_gladiador

if vida_gladiador > 0: print(f"¡VICTORIA! {gladiador} ha ganado la batalla.")
if vida_gladiador <= 0: print("DERROTA. Has caído en combate.")
