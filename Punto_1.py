
numero = int(input("Por favor, ingrese un número entero: "))
digitos = []
while numero > 0:
    digito = numero % 10  # Obtiene el último dígito del número
    digitos.insert(0, digito)  # Inserta el dígito en la priemra posición de la lista
    numero = numero // 10  # Elimina el último dígito del número
print("Los dígitos separados son:", digitos)