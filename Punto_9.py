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



