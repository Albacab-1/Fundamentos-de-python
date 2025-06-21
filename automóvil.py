class Automovil:
    def __init__(self, marca, color):
        #definir atributos clase
        #empiezan con self
        self.marca = marca
        self.color = color
    
    def avanzar(self):
        print(f"el coche avanza y es un: {self.marca}")
    
    def retrocede(self):
        print(f"el coche retrocede y es de color {self.color}")

if __name__=="__main__":
    auto=Automovil("BMW", "azul")
    auto.avanzar()
    auto.retrocede()
    auto1= Automovil("honda", "Gris")
    auto1.retrocede()
    auto1.avanzar()