lecturas=int(input("¿Cuántas lecturas de temperatura tienes? "))
x=0
y=0
z=0
while x<lecturas:
  x+=1
  temperatura=float(input("Inserta la temperatura"))
  if y>=10 and y<=40:
    pass
  else:
    z+=1
print("Número de lecturas fuera del rango:",z)
a=(z*100)/lecturas
print("Porcentaje de lecturas fuera del rango:",a,"%")
