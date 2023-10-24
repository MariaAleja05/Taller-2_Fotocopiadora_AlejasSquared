# Taller #2
### Fecha:  18-20-2023
### **Nombre del equipo:** Fotocopiadora AlejasSquared
  **Integrantes del equipo:** María Alejandra Niño Peña y María Alejandra Varela
  
### **Logo**:
FALTA

### 1. Desarrollar un programa que ingrese un número entero n y separe todos los digitos que componen el número. Pista: Utilice los operadores módulo (%) y división entera (//).
* EXPLICACIÓN
* Mirar archivo Punto1.py
```pseudocode

```
### 2. Desarrollar un programa que ingrese un número flotante n y separe su parte entera de la parte decimal, y luego entregue los dígitos tanto de la parte entera como de la decimal.
* EXPLICACIÓN
* Mirar archivo Punto2.ipynb
```pseudocode

```
### 3. Desarrollar un programa que permita ingresar dos números enteros y determinar si se tratan de números espejos, definiendo números espejos como dos números a y b tales que a se lee de izquierda a derecha igual que se lee b de derecha a izquierda, y viceversa.
* EXPLICACIÓN
* Mirar archivo Punto3.py
```pseudocode

```
### 4. Diseñar una función que permita calcular una aproximación de la función coseno alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Taylor. nota: use math para traer la función coseno y mostrar la diferencia entre el valor real y la aproximación. Calcule con cuántos términos de la serie (i.e: cuáles valores de n), se tienen errores del 10%, 1%, 0.1% y 0.001%.
* EXPLICACIÓN
* Mirar archivo Punto4.ipynb
```pseudocode

```
### 5. Desarrollar un programa que permita determinar el Minimo Comun Multiplo de dos numeros enteros. Abordar el problema desde una perpectiva tanto iterativa como recursiva. Pista: Puede ser de utilidad chequear el Algoritmo de Euclides para el cálculo del Máximo Común Divisor, y revisar cómo se relaciona este último con el Mínimo Común Múltiplo.
* EXPLICACIÓN
* Mirar archivo Punto5.py
```pseudocode

```
### 6. Desarrollar un programa que determine si en una lista existen o no elementos repetidos. Pista: Maneje valores booleanos y utilice el operador in.
* EXPLICACIÓN
* Mirar archivo Punto6.ipynb
```pseudocode
def ElementosRepetidos(lista):                # Función para encontrar elementos repetidos
  lista2=[]                                   # Lista para colocar los valores que ya se miraron
  for j in lista:                             # Evalua cada elemento de la lista original
    if j in lista2:                           # Evalua si el elemento esta en la lista 2
      return True                             # Significa que está repetido
    lista2.append(j)                          # Añade el elemento a la lista 2 para ver si se repite
  return False                                # No hay ningún elemento repetido

if __name__ == "__main__":
  lista=[]                                    # Lista vacía que crea el usuario
  n = int(input("Ingrese la cantidad de elementos de la lista: "))  # La cantidad de elementos

  for i in range(n):                          # Repite según la cantidad de elementos que tendrá la lista
    a = float(input("Ingrese un elemento de la lista: "))
    lista.append(a)                           # Añade el elemento a la lista
  rta=ElementosRepetidos(lista)               # Llama la función
  print("--------------------------------------------------")
  print(lista)
  if rta:                                     # Si el resultado de la función es True
    print("La lista SI tiene elementos repetidos")
  else:                                       # Si el resultado de la función es False
    print("La lista NO tiene elementos repetidos")
```
### 7. Desarrollar un programa que determine si en una lista se encuentra una cadena de caracteres con dos o más vocales. Si la cadena existe debe imprimirla y si no existe debe imprimir 'No existe'.
* EXPLICACIÓN
* Mirar archivo Punto7.py
```pseudocode

```
### 8. Desarrollar un programa que dadas dos listas determine que elementos tiene la primer lista que no tenga la segunda lista.
* EXPLICACIÓN
* Mirar archivo Punto8.ipynb
```pseudocode
def ElementosRepetidos(lista, lista2):
  for i in range(n):      # Se repite por cada elemento de la lista
    for j in lista:       # Toma cada elemento de la primera lista
      if j in lista2:     # Se mira si ese elemento está en la lista 2
        lista.remove(j)   # Si está se elimina de la primera lista
  return lista

if __name__ == "__main__":
  lista=[]
  lista2=[]
  n = int(input("Ingrese la cantidad de elementos de la primera lista: "))    # Ingresar # de elementos
  for i in range(n):                                                          # Ingresar elementos
    a = float(input("Ingrese un elemento de la primera lista: "))
    lista.append(a)
  m = int(input("Ingrese la cantidad de elementos de la segunda lista: "))    # Ingresar # de elementos
  for i in range(m):                                                          # Ingresar elementos
    b = float(input("Ingrese un elemento de la segunda lista: "))
    lista2.append(b)
  rta=ElementosRepetidos(lista, lista2)                                       # Se llama la función
  print("--------------------------------------------------")
  print("La primera lista tiene los siguientes elementos que no están en la segunda lista: " + str(rta))
```
### 9. Resolver el punto 7 del taller 1 usando operaciones con vectores.
* EXPLICACIÓN
* Mirar archivo Punto9.py
```pseudocode

```
### 10. Suponga que se tiene una lista A con ciertos números enteros. Desarrolle una función que, independientemente de los números que se encuentran en la lista A, tome aquellos números que son múltiplos de 3 y los guarde en una lista nueva, la cual debe ser retornada por la función. Implemente la perspectiva de un patrón de acumulación y también de comprensión de listas. Desafío: Si ya lo logró, inténtelo ahora sin utilizar el módulo (%). Pista: Un número es multiplo de 3 si la suma de sus dígitos también lo es, ¿verdad?
* EXPLICACIÓN
* Mirar archivo Punto10.ipynb
```pseudocode

```
### 11. BONO: Desarrollar un algoritmo que determine si una matriz es mágica. Se dice que una matriz cuadrada es mágica si la suma de cada una de sus filas, de cada una de sus columnas y de cada diagonal es igual.
* EXPLICACIÓN
* Mirar archivo Punto11.py
```pseudocode

```
