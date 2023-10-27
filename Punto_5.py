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



