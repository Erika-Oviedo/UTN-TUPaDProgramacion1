##Ejercicio 1— “Caja del Kiosco” OVIEDO ERIKA
##Objetivo: Simular una compra con validaciones y cálculo de total.
#Requisitos
#1. Pedir nombre del cliente (solo letras, validar con .isalpha() en while).
#2. Pedir cantidad de productos a comprar (número entero positivo, validar con
#.isdigit() en while).
#3. Por cada producto (usar for):
#o Pedir precio (entero, validar .isdigit()).
#o Pedir si tiene descuento S/N (validar con while, aceptar s o n en
#cualquier mayuscula/minuscula).
#o Si tiene descuento: aplicar 10% al precio de ese producto.
#4. Al final mostrar:
#o Total sin descuentos
#o Total con descuentos
#o Ahorro total
#o Promedio por producto (usar float y formatear con :.2f, ejem:
#x = 3.14159
#print(f"{x:.2f}"))
total_con_desc = 0
total_sin_desc = 0
total_ahorrado= 0

while True:
    nombre_cliente = input("Ingrese su nombre: ").strip()
    if(nombre_cliente.isalpha() and nombre_cliente != ""):
        print(f"Cliente: {nombre_cliente}")
        break
    else:
        print("¡Por favor ingrese su nombre solo con letras!")

while True:
    cant_productos_str = input("¿Cuántos productos desea comprar?: ")
    if (cant_productos_str.isdigit() and cant_productos_str != "" and int(cant_productos_str) > 0):
        cant_productos = int(cant_productos_str)
        print(f"Cantidad de productos: {cant_productos}")
        break
    else:
        print("Por favor ingrese la cantidad de productos a comprar solo con numeros.")

for i in range(cant_productos):
    while True:
        precio_prod_str = input(f"Producto {i + 1}-precio : ") 
        if(precio_prod_str.replace(".","").isdigit() and precio_prod_str != "" and float(precio_prod_str) > 0):
            precio_prod = float(precio_prod_str)
            print("Ingresado")
            break
        else:
            print("Error en el ingreso del precio del producto.")
    while True:
        tipo_prod = input("El producto tiene descuento (si/no): ").upper()
    
        if tipo_prod == "SI":
            print("Aplica %10 de descuento")
            descuento = precio_prod * 0.10
            break
        elif tipo_prod == "NO":
            print("No aplica descuentos")
            descuento = 0
            break
        else:
            print("Error, solo se permiten respuestas de (si/no).")

    total_sin_desc += precio_prod        
    total_con_desc += precio_prod - descuento
    total_ahorrado += descuento
    promedio = total_con_desc / cant_productos

print(f"El total sin descuento: ${total_sin_desc}.")
print(f"El total con descuentos: ${total_con_desc}")
print(f"Ahorro: ${total_ahorrado}.") 
print(f"Promedio por producto: ${promedio:.2f}")