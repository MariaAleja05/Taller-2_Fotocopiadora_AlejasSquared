def Digitos(numero): #Aquí utilicé separo los dígitos del número
  digitos = []
  while numero > 0:
      digito = numero % 10
      digitos.insert(0, digito)  # se van introduciendo los dígitos a una lista
      numero = numero // 10
  return digitos

def reverse_list(n): #Hago lo que no fui capaz de hacer en el examen porque no soy buena trabajando bajo presión
  nueva_lista=[]
  cardinal= len(n)
  j=0
  while j<= cardinal: #voy iterando la posición de los elementos de la lista de digitos oringinal hasta que sea igual a n-1
    for i in n:
      nueva_lista.insert(j, i)
    j+=1
    return nueva_lista
if __name__ =="__main__":
  #Defino todas las variables que necesito
  numero_1 = int(input("Por favor, ingrese un número entero: "))
  numero_2= int(input("Por favor ingrese otro número entero: "))
  # Las listas de los dígitos de cada número
  digitos_1 = Digitos(numero_1)
  digitos_2= Digitos(numero_2)
  # Las listas invertidas de los digitos de cada número
  digitos_1_r=reverse_list(digitos_1)
  digitos_2_r=reverse_list(digitos_2)
  # Literalmente el objetivo final, comprobar si son espejo o no teniendo en cuenta la lista original de los digitros y la que está en reversa
  if numero_2 == digitos_1_r:
    print("Los números que ingresó son numeros espejo")
    print(f"{numero_1} {numero_2}")
  else:
    print("Los números que ingreó no son números espejo")


