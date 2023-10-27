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