def encriptarTexto(rutaArchivo):
    archivo= open(rutaArchivo, 'r')
    texto=archivo.read()
    archivo.close()
    textoEncriptado=encriptar(texto)

    archivo= open(rutaArchivo, 'w')
    archivo.write(textoEncriptado)
    archivo.close()
def desencriptarTexto(rutaArchivo):
    archivo= open(rutaArchivo, 'r')
    texto=archivo.read()
    archivo.close()
    textoDESncriptado=desencriptar(texto)

    archivo= open(rutaArchivo, 'w')
    archivo.write(textoDESncriptado)
    archivo.close()



def encriptar(texto):
    textofinal=""
    for letra in texto:
        ascii=ord(letra)
        ascii+=1
        textofinal+= chr(ascii)
    return textofinal


def desencriptar(texto):
    contador=0
    textofinal = ""
    for letra in texto:
        ascii = ord(letra)
        ascii -= 1
        textofinal += chr(ascii)
    return textofinal



respuestaEncriptar=input("E para encriptar o D para desencriptar")
rutaArchivo=input("Especifica la ruta del archivo que quieres usar")
if respuestaEncriptar=="E":
    encriptarTexto(rutaArchivo)
    print("Se encripto el archivo correctamente")
elif respuestaEncriptar=="D":
    desencriptarTexto(rutaArchivo)
    print("Se desencripto el archivo correctamente")