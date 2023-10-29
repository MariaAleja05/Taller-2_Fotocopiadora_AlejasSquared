# Taller #2
### Fecha:  18-20-2023
### **Nombre del equipo:** Fotocopiadora AlejasSquared
  **Integrantes del equipo:** María Alejandra Niño Peña y María Alejandra Varela
  
### **Logo**:
FALTA

### 1. Desarrollar un programa que ingrese un número entero n y separe todos los digitos que componen el número. Pista: Utilice los operadores módulo (%) y división entera (//).
* Para este punto lo primero es inicializar una lista donde se van almacenar los dígitos, posteriormente en un ciclo while con caso base que el número sea mayor que cero, el número se divide entre 10 y de eso se toma el residuo, el número que resultó es el último dígito de el número inicial. Ese dígito se agrega a una lista y por último el número inicial se divide entre 10 y se toma su parte entera para eliminar el dígito que ya descubrimos.                                                                                                                                                                                                                                   
* Ver documento:[Punto_1.py](Punto_1.py)
```python

numero = int(input("Por favor, ingrese un número entero: "))
digitos = []
while numero > 0:
    digito = numero % 10  # Obtiene el último dígito del número
    digitos.insert(0, digito)  # Inserta el dígito en la priemra posición de la lista
    numero = numero // 10  # Elimina el último dígito del número
print("Los dígitos separados son:", digitos)
```
### 2. Desarrollar un programa que ingrese un número flotante n y separe su parte entera de la parte decimal, y luego entregue los dígitos tanto de la parte entera como de la decimal.
* EXPLICACION
* Mirar archivo Punto2.ipynb
```python
def Digitos(n):                                                 # La función
  digitos=[]                                                    # Lista para introducir los dígitos
  entero=[]                                                     # Lista para ingresar la parte entera
  decimal=[]                                                    # Lista para ingresar la parte decimal
  str_n=str(n)                                                  # Convertir el número a str
  for i in str_n:                                               # Un for que va con cada elemento del str
    decimal.append(i)                                           # Se añaden todos los elementos    
  decimal_aux=decimal[:]                                        # Se usará más adelante 
  for i in decimal_aux:                                         # Con cada elemento de la lista se busca donde hay un punto y así se divide la parte entera de la decimal
    if i==".":
      decimal.remove(i)
      break
    else:
      decimal.remove(i)                                         # Lo que se elemina del decima se añade a la entera
      entero.append(i)
  print("La parte entera es: " + str(entero))                   # Se muestra el resultado
  print("La parte decimal es: " + str(decimal))

if __name__ == "__main__":
  n = float(input("Ingrese el número:"))                        # El usuario ingresa el número flotante
  Digitos(n)
```
### 3. Desarrollar un programa que permita ingresar dos números enteros y determinar si se tratan de números espejos, definiendo números espejos como dos números a y b tales que a se lee de izquierda a derecha igual que se lee b de derecha a izquierda, y viceversa.
* En este punto definimos dos funciones, la primera para almacenar los dígitos de los números en una lista y segunda (y necesariamente larga porque podríamos usar ```Lista[::-1]```) que permite swapear la lista de números. Por último pedimos al usuario que ingrese los dos números y se hace una comparación entre la lista swapeada del primero y la lista original del segundo. Si son ifuales entonces los números son espejo, de resto no.
* Ver documento:[Punto_3.py](Punto_3.py)
```python
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

```
### 4. Diseñar una función que permita calcular una aproximación de la función coseno alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Taylor. nota: use math para traer la función coseno y mostrar la diferencia entre el valor real y la aproximación. Calcule con cuántos términos de la serie (i.e: cuáles valores de n), se tienen errores del 10%, 1%, 0.1% y 0.001%.
* Para este problema primero importe math y las funciones cos y factorial para desarrollar las operaciones.
Creé una función con un for de rango desde 0 hasta n+1 (para incluir n) donde va a realizar la operación y el resultado de esta operación se le irá sumando a la variable "suma" para calcularla. La función retornará la aproximación de esta operación en la variable suma.

En la función main, se le solicita al usuario ingresar el número real, definimos que n(número de iteraciones) comience a evaluar desde 1, llamamos la función de la aprox del seno para mostrar el resultado de la aproximación, luego para mostrar el valor real lo calculamos usando la función de math: cos. Hay un while para calcular el número de veces n que se puede realizar la operación mientras que el error entre la aprox y el valor real no se pase del 10%, 1%, 0.1$, 0.001% en este se llama la función para que n se vaya actualizando en esta mientras se cumpla la condición.
* Mirar archivo Punto4.ipynb
```python
import math                                           # Se importa la biblioteca math
from math import cos, factorial                       # Se importan las funciones cos y factorial

def AproxFuncionCoseno(x: float, n:int) -> float:     # Se crea una función para hallar la operación
  suma: float = 0                                     # La suma inicia en cero
  for i in range(0, n+1):                             # Para repetir la operación con cada elemento
    y = ((-1)**i)*((x**(2*i))/factorial(2*i))         # Operación de la formula
    suma += y
  return suma                                         # Resultado final

if __name__ == "__main__":
  x = float(input("Ingrese un número real: "))        # Ingresar el número x
  n: int = 1                                          # La sumatoria inicia desde 1
  aprox: float = AproxFuncionCoseno(x, n)             # Se llama la función
  valorReal: float = cos(x)                           # Se calcula el valor real
  diferencia: float = valorReal-aprox                 # Se halla la diferencia

  print("------------------------------------------------------------------------------")

  while ((abs(valorReal - aprox)/valorReal * 100)>0.1):     #Para el 10%
    aprox: float = AproxFuncionCoseno(x, n)
    n += 1
  print("El valor de n para tener un error menor a 0.1: " + str(n))

  while ((abs(valorReal - aprox)/valorReal * 100)>0.01):    #Para el 1%
    aprox: float = AproxFuncionCoseno(x, n)
    n += 1
  print("El valor de n para tener un error menor a 0.01: " + str(n))

  while ((abs(valorReal - aprox)/valorReal * 100)>0.001):   # Para el 0.1%
    aprox: float = AproxFuncionCoseno(x, n)
    n += 1
  print("El valor de n para tener un error menor a 0.001: " + str(n))

  while ((abs(valorReal - aprox)/valorReal * 100)>0.00001): #Para el 0.001%
    aprox: float = AproxFuncionCoseno(x, n)
    n += 1
  print("El valor de n para tener un error menor a 0.00001: " + str(n))

  print("------------------------------------------------------------------------------")

  print("La aproximación es: " + str(aprox))                # Resultado de la aprox
  print("El valor real es: " + str(valorReal))              # Resultado del valor real
  print("La diferencia entre estos dos valores es de: " + str(diferencia))  #Resultado diferencia
```
### 5. Desarrollar un programa que permita determinar el Minimo Comun Multiplo de dos numeros enteros. Abordar el problema desde una perpectiva tanto iterativa como recursiva. Pista: Puede ser de utilidad chequear el Algoritmo de Euclides para el cálculo del Máximo Común Divisor, y revisar cómo se relaciona este último con el Mínimo Común Múltiplo.
* El algoritmo de Euclides funciona la siguiente manera: el número mayor se divide por el número menor, después el número menor pasa a ser el dividendo y el recibo de la primera división va a ser el divisor así se hace consecutivamente hasta que el residuo cero, el residuo inter inmediatamente anteriorsería el máximo común divisor, pero el ejercicio nos pide el mínimo común múltiplo así que buscamos la relación: *m_c_m=(A*B)/m_c_d*. Teniendo en cuenta la anterior hicimos una función en la que se determina primero cuál número es el mayor, con ese resultado se obtiene la primera división y a su vez el primer residuo, después con un ciclo while con caso base que el residuo sea mayor que cero se actualizan las variables teniendo en cuenta el algoritmo de Euclides. Por último se pide al usuario que ingrese los números y definimos dos variables, el máximo común divisor como la función de esos dos números El mínimo común múltiplo con la relación que ya habíamos explicado.
*Ver documento:[Punto_5.py](Punto_5.py) y [Punto_5_recursivo.py](Punto_5_recursivo.py)

```python
#Iterativo
def m_c_d(x,n) ->int:
  if x>=n: #descubrir cual es el número mayor y que empiece la iteración en órden
    dividendo=x
    divisor=n
  else:
    dividendo= n
    divisor=x
  residuo = dividendo % divisor
  while residuo > 0:
    dividendo=divisor
    divisor=residuo
    residuo = dividendo % divisor
  return divisor #Si funcionó, que emoción

if __name__ =="__main__":
  print("Ingrese dos números para conocer su mínimo común multiplo")
  a=int(input("Ingrese el primer número: "))
  b=int(input("Ingrese el segundo número: "))
  m_c_d=m_c_d(a,b)
  m_c_m= (a*b)//m_c_d #Esta es la relación entre maximo compun divisor y mínimo común multiplo
  print(f"El mínimo común múltiplo entre {a} y {b} es: {m_c_m}. Y el máximo comun divisor es: {m_c_d}")
```
## Función recursiva
La función recursiva en un principio pareció más difícil de lo que era. Pero en realidad sólo debíamos como en el anterior, identificar el número mayor, tomar como caso hace que el residuo fuera cero para lo cual la función retornaría el divisor de esa última iteración  que sería el residuo anterior. Y para la parte de la iteración se define la función recursiva pero en este caso con las variables del divisor y el residuo.
```python
# Recursivo
def m_c_dRecursiva(x,n):
  if x>=n: #descubrir cual es el número mayor y que empiece la iteración en órden
    dividendo=x
    divisor=n
  else:
    dividendo= n
    divisor=x
  residuo = dividendo % divisor
  #Caso base
  if residuo == 0:
    return divisor
  #Aca se define la variable
  else:
    return  m_c_dRecursiva(divisor, residuo)

if __name__ =="__main__":
  print("Ingrese dos números para conocer su mínimo común multiplo")
  a=int(input("Ingrese el primer número: "))
  b=int(input("Ingrese el segundo número: "))
  m_c_d=m_c_dRecursiva(a, b)
  m_c_m= (a*b)//m_c_d #Esta es la relación entre maximo compun divisor y mínimo común multiplo
  print(f"El mínimo común múltiplo entre {a} y {b} es: {m_c_m}. Y el máximo comun divisor es: {m_c_d}")
```
![image](https://github.com/MariaAleja05/Taller-2_Fotocopiadora_AlejasSquared/assets/141885396/2d4a40ad-fe89-4853-91db-5019be1156b4)
" Codificar no es solo hacer código"
                                 -Un profe particular-
### 6. Desarrollar un programa que determine si en una lista existen o no elementos repetidos. Pista: Maneje valores booleanos y utilice el operador in.
* Primero creé una función donde hay un for que evaluará cada elemento de la lista que creó el usuario. Luego hay un if que mira si el elemento se encuentra en la lista 2 alterna que se creá donde se irán añadiendo los valores que ya se evaluaron, si en algún momento se encuentra un valor que este en la lista original y en la alterna significa que ya se había mirado ese número en la original, y por lo tanto, si habrán elementos repetidos y la función retornará True.

En la función main, se le solicita al usuario ingresar la cantidad de elementos que tendrá su lista, hay un for para que el usuario ingrese cada elemento de la lista, proceso que se repitirá según la longitud de la lista. Se llama la función y en un condicional se expresa que si la función retorna True, significa que sí hay valores repetidos, de lo contrario, no habrá.
* Mirar archivo Punto6.ipynb
```python
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
* En una función definimos una variable como una lista vacía, posteriormente recorremos la lista con un ciclo for, y en un condicional hacemos que el código utilice la función ```isintance``` para que pueda evaluar el tipo de variable que está en la lista, y además verifique que ese string tiene dos o más letras si no cumple alguna de las dos entonces se imprimirá un no existe.
* Ver documento:[Punto_7.py](Punto_7.py)
```python
def cadenita(Lista):
  nueva_l=[]
  for i in Lista:
    if isinstance(i,str) and len(i)>=2:
      nueva_l.append(i)
  if len(nueva_l) == 0:
    print("No existe")
  return nueva_l

if __name__ =="__main__":
  lista =["a",1,2,"No",45,"Hola"]
  ev = cadenita(lista)
  print(ev)
```
### 8. Desarrollar un programa que dadas dos listas determine que elementos tiene la primer lista que no tenga la segunda lista.
* Primero creé una función donde hay un for que evaluará cada elemento de la lista que creó el usuario. Hay otro for anidado que mirará si el elemento se seleccionada se encuentra en la lista 2, en caso de ser así el elemento se eliminará de la lista (ya que se buscan todos los elementos que no están en la segunda lista), si no está no se borrara de la primera lista.

En la función main, se crearon las 2 listas. Se le solicita al usuario ingresar la cantidad de elementos que tendrá su lista, hay un for para que el usuario ingrese cada elemento de la lista, proceso que se repitirá según la longitud de la lista. Se repite el anterior proceso para la creación de la segunda lista. Se llama la función y se imprimirá la primera lista sin los elementos que se encuentran en la segunda lista.
* Mirar archivo Punto8.ipynb
```python
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
En este punto nos emocionamos y decidimos definir cinco funciones que no eran necesarias pero igual estuvo divertido. Cada una de las funciones encuentra cada una de las operaciones pedidas en el punto siete:
* El promedio
* La mediana
* El promedio multiplicativo (multilplica todos y luego calcula la raíz de la cantidad de operandos)
* Ordenar los números de forma ascendente
*La potencia del mayor número elevado al menor número
*La raíz cúbica del menor número
Los promedios fueron fáciles simplemente se inicializa una variable en donde se va almacenar la suma o la multiplicación dado el caso de los números de la lista. Para el orden ascendente simplemente utilizamos la función Sort, por otro lado el orden se hizo en la definición de las variables. Para elevar el número mayor al número menor se define en una variable la función ascendente de la lista para posteriormente definir dos variables que estén en la posición primera y en la posición última de esa lista, por último el que está en la última posición se le va al que esté en la primera posición. Ya para ejecutar las funciones se pide an usuario que ingrese cinco números reales, se inicializa una variable que será una lista vacía en la que se van a agregar todos esos números y por último se definen diferentes variables con su respectiva función y se imprime cada una de las operaciones
* Ver documento:[Punto_9.py](Punto_9.py)
```python
def promedio(Lista):
  a=0 #una variable para que se guarde la suma
  for i in Lista:
    a+=i
    promedio= a/5
  return promedio

def ascendente(Lista):
  orden_A=sorted(Lista) #La vida era tan facil y no lo sobiamos
  return orden_A

def mediana(Lista):
  orden=ascendente(Lista)
  mediana= orden[2] #Aqui se escoge el número que esté en la posición 3, la mitad.
  return mediana

def promedio_multiplicativo(Lista):
  a=1
  for i in Lista:
    a*=i
    promedio= a/5 #Funciona como el promedio normal pero con multiplicación
  return promedio

def mayor_al_menor(Lista):
  orden=ascendente(Lista)
  mayor= orden[4]
  menor=orden[0]
  potencia= mayor**menor
  return potencia

def cubica(Lista):
  orden=ascendente(Lista)
  menor=orden[0]
  cubica= menor**(1/3)
  return cubica

if __name__ =="__main__":
  Lista=[]
  print("Ingrese 5 números reales") #Definición de todas las variables
  a=float(input("a: "))
  b=float(input("b: "))
  c=float(input("c: "))
  d=float(input("d: "))
  e=float(input("e: "))
  Lista.append(a)
  Lista.append(b)
  Lista.append(c)
  Lista.append(d)
  Lista.append(e)
  El_promedio=promedio(Lista)
  La_mediana=mediana(Lista)
  El_multiplicativo=promedio_multiplicativo(Lista)
  Forma_Ascendente=ascendente(Lista)
  Forma_Descendente = Lista
  Lista.sort(reverse = True)
  Potencia=mayor_al_menor(Lista)
  Cubica=cubica(Lista)
  print(f"Promedio={El_promedio} \n\nMediana={La_mediana} \n\nPromedio multiplicativo={El_multiplicativo} \n\nForma ascendente={Forma_Ascendente} \n\nForma descendente={Forma_Descendente} \n\nPotencia del mayor al menor={Potencia} \n\nCubica del menor={cubica} ")
```
### 10. Suponga que se tiene una lista A con ciertos números enteros. Desarrolle una función que, independientemente de los números que se encuentran en la lista A, tome aquellos números que son múltiplos de 3 y los guarde en una lista nueva, la cual debe ser retornada por la función. Implemente la perspectiva de un patrón de acumulación y también de comprensión de listas. Desafío: Si ya lo logró, inténtelo ahora sin utilizar el módulo (%). Pista: Un número es multiplo de 3 si la suma de sus dígitos también lo es, ¿verdad?
* Mirar archivo Punto10.ipynb
* USANDO MÓDULO (%)
Primero creé una función donde use comprensión de listas para hacer todo en una línea de código, por medio de un for mirará cada elemento y si el residuo cuando se divide por 3 es cero entonces se acumulará a la lista que retornará de multiplos de 3, de lo contrario no tendrá en cuenta el valor.

En la función main, se le solicita al usuario ingresar la cantidad de elementos que tendrá su lista, hay un for para que el usuario ingrese cada elemento de la lista, proceso que se repitirá según la longitud de la lista. Se llama la función y se muestra la lista del usuario y, la lista que creó la función con los valores que pertenecían a esta y son múltiplos de 3.
```python
def Multiplos(lista):                                                         # La función retornará los valores que sean multiplos de 3
  return [i for i in lista if i % 3 == 0]                                     # Usando List comprehension
                                                                              # Si el residuo al dividir cada número por 3 es cero, es múltiplo

if __name__ == "__main__":
  lista=[]
  n = int(input("Ingrese la cantidad de elementos de la primera lista: "))    # Ingresar la cantidad de elementos
  for i in range(n):                                                          # Ingresar elementos
    a = int(input("Ingrese un elemento de la primera lista: "))
    lista.append(a)
  rta=Multiplos(lista)                                                        # Se llama la función
  print("--------------------------------------------------")
  print("Tú lista: " + str(lista))                                            # Se imprime la lista original que creó el usuario
  print("Los multiplos de 3 de esa lista son: " + str(rta))                   # Se imprime la lista con los elementos que son múltiplos de 3
```
* EXPLICACION RETO SIN USAR MÓDULO (%)
```python

```
### 11. BONO: Desarrollar un algoritmo que determine si una matriz es mágica. Se dice que una matriz cuadrada es mágica si la suma de cada una de sus filas, de cada una de sus columnas y de cada diagonal es igual.
* EXPLICACIÓN
* Mirar archivo Punto11.py
```pseudocode

```
