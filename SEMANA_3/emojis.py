salirChat=0
while salirChat == 0 :
    texto=str(input(">"))
    if texto=="salir":
        salirChat=salirChat+1
    texto=texto.replace(":)","😀")
    texto=texto.replace(":(","😭")
    print(texto)
