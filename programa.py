# programa àra saber el precio de una llamada telefonica

print("------------------------------")
print("---precio de la llamada-------")
print("------------------------------")

# input

dl = int(input("El tiempo de la llamada es de: "))

#procesing

if (dl<=3):
    print("El costo de la llamada es de 300 pesos")
else:
    t=dl - 3
    p = 300 + (50*t)    
    print("El costo de la llamada es: " + str(p) + " pesos.")