#Calculdara de masa corporal
peso=float(input("Dime cuanto pesas:"))
estatura=float(input("Dime cuanto mides en metros, ejemplo 1.73:"))
masaCorporal=peso/(estatura*estatura)
print("Tu masa corporal es de:"+str(masaCorporal))
if masaCorporal <= 20:
    print("Estas delgado")
elif masaCorporal >= 20 and masaCorporal<=26:
    print("Tienes un Peso Normal")
elif masaCorporal >= 26:
    print("Tienes Sobre peso")
