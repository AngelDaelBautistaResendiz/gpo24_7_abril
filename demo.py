class Cuadrado:
    def __init__(self, lado):
        self.lado = lado
    
    def area(self):
     if self.lado == 0:
        return 0
     return self.lado * self.lado 

##################################
lado = int(input("ingresa el valor del lado: "))
mi_ejemplo = Cuadrado(lado)
total = mi_ejemplo.area

print(f"el area es {total}") 