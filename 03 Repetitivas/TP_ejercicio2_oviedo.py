##Ejercicio 2 — “Acceso al Campus y Menú Seguro” OVIEDO ERIKA
#Objetivo: Login con intentos + menú de acciones con validación estricta.
#Requisitos
#1. Definir credenciales fijas en el código:
#o usuario correcto: "alumno"
#o clave correcta: "python123"
#2. Permitir máximo 3 intentos para ingresar usuario y clave.
#3. Si falla 3 veces: mostrar “Cuenta bloqueada” y terminar.
#4. Si ingresa bien: mostrar un menú repetitivo (usar while) hasta elegir salir:
#1. Ver estado de inscripción (mostrar “Inscripto”)
#2. Cambiar clave (pedir nueva clave y confirmación; deben
#coincidir)
#3. Mostrar mensaje motivacional (1 frase)
#4. Salir
#5. Validación del menú:
#o Debe ser número (.isdigit())
#o Debe estar entre 1 y 4
usuario = "alumno"
clave = "python123" 
saldo_inicial = 10000

intentos = 3

opcion = "0"

while (intentos >= 1):
    usuario_alumno = input("Ingrese su usuario: ").strip()
    clave_alumno = input("Ingrese su clave: ")

    if( usuario_alumno == usuario and clave_alumno == clave):
        print("Ingreso correcto")
        break
    else:
        intentos -= 1
        print("Error: credenciales inválidas.")
        if(intentos == 0):
            print("Cuenta bloqueada")
        else:
            print(f"Te quedan {intentos} intentos")

while opcion != "4" and intentos != 0:
    print("""\n--- MENÚ DE ESTUDIANTE ---
1.Estado
2.Cambiar clave
3.Mensaje
4.Salir""")
    opcion = input("Ingrese una opción: ")
    match opcion:
        case "1":
            print("""\n--- ESTADO --- 
Inscripto""")
        case "2":
            while True:
                print("\n--- CAMBIO DE CLAVE ---")
                clave_nueva = input("Ingrese la nueva clave (minimo 6 caracteres): ")
                if len(clave_nueva) < 6:
                    print("La clave debe tener mínimo 6 caracteres.")
                    continue
                confirmar_clave = input("Confirme la nueva clave: ")
                if clave_nueva == confirmar_clave:
                    clave = clave_nueva
                    print("¡Clave cambiada correctamente!")
                    break
                else:
                    print("Las claves no coinciden. Intente nuevamente.")   
        case "3":
            print("""\n--- FRASE MOTIVACIONAL --- 
¡¡Cada error que aparece en pantalla es una oportunidad para entender algo nuevo. Ánimo!!""")
        case "4":
            print("¡Hasta luego!")
        case _:
            print("ERROR! Ingrese correctamente la opción elegida (1-4).")
