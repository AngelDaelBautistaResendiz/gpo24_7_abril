class Cuadrado:
    def __init__(self, lado):
        self.lado = lado
    
    def area(self):
     if self.lado == 0:
        return 0
     return self.lado * self.lado 