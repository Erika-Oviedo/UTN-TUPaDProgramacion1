#1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.
print("Hola Mundo!!")

#2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
# el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
# por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
# realizar la impresión por pantalla.
nombre = input ("Ingrese su nombre: ")
print(f"Su nombre es ", nombre)

#3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
# imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
# “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
# años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
# la impresión por pantalla.
nombre = input("Ingrese su nombre: ")
apellido = input ("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
lugar_de_residencia = input("Ingrese su lugar de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugar_de_residencia}.")

#4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
# su perímetro.
import math

radio = float(input("Ingresá el radio del círculo: "))

area = math.pi * radio ** 2
perimetro = 2 * math.pi * radio

print("Área del círculo:", area)
print("Perímetro del círculo:", perimetro)

#5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
# cuántas horas equivale.
segundos = int(input("Ingresá una cantidad de segundos: "))

horas = segundos / 3600

print("Equivale a", horas, "horas.")

# 6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
# multiplicar de dicho número.
numero = int(input("Ingresá un número: "))

print("Tabla de multiplicar del", numero)
for i in range(1, 11):
    print(numero, "x", i, "=", numero * i)


# 7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
# pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.
num1 = int(input("Ingresá el primer número (distinto de 0): "))
num2 = int(input("Ingresá el segundo número (distinto de 0): "))

suma = num1 + num2
division = num1 / num2
multiplicacion = num1 * num2
resta = num1 - num2

print("Suma:", suma)
print("División:", division)
print("Multiplicación:", multiplicacion)
print("Resta:", resta)

# 8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
# de masa corporal.
peso = float(input("Ingresá tu peso en kg: "))
altura = float(input("Ingresá tu altura en metros: "))

imc = peso / (altura ** 2)

print("Tu índice de masa corporal es: ", imc)


#9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
#pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:
celsius = float(input("Ingresá la temperatura en grados Celsius: "))

fahrenheit = (9/5) * celsius + 32

print("Equivalente en Fahrenheit:", fahrenheit)

#10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
#dichos números.
num1 = float(input("Ingresá el primer número: "))
num2 = float(input("Ingresá el segundo número: "))
num3 = float(input("Ingresá el tercer número: "))

promedio = (num1 + num2 + num3) / 3

print("El promedio es:", promedio)
