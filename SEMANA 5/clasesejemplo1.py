class cuadrado:
    def __init__(self,ancho,alto):
        self.ancho=ancho
        self.alto=alto
    def calcularArea(self):
        area=self.ancho*self.alto
        return area
figura=cuadrado(10,12)
print(figura.ancho)
print(figura.alto)
print(figura.calcularArea())