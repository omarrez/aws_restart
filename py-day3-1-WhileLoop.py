import random

print("\t\tBienvenido al juego de la adivinanza!")
print("\nLa regla es simple... pensare un numero y lo tienes que adivinar")
print("\nEl numero sera del 1 al 10")

number = random.randint(1,10)
conteo=1
finalizado = False
while finalizado!=True:
    intento = int(input("Cual eliges??... "))
    
    if (intento == number):
        print(f"Felicidades!! El numero SI es {number}")
        print(f"Total de intentos = {conteo}")
        finalizado = True
    elif (intento>0 and intento<number):
        print ("El numero buscado es mayor\n")
    elif (intento<11 and intento>number):
        print("El numero buscado es menor\n")
    else: 
        print("Ingresaste un numero fuera del rango buscado!!\n")

    conteo+=1