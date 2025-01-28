class Formula:

    def __init__(self):

        self.x1 = 0

        self.y1 = 0

        self.x2 = 0

        self.y2 = 0



    def datos(self):

        print("Ingrese las coordenadas de x e y:")

        self.x1 = int(input("Coordenada de x1: "))

        self.y1 = int(input("Coordenada de y1: "))


        self.x2 = int(input("Coordenada de x2: "))


        self.y2 = int(input("Coordenada de y2: "))

    def resultado(self):


        distancia = ((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2) ** 0.5


        print("La distancia entre los dos puntos es:", distancia)


def main():

    obj = Formula()  

    obj.datos()


    obj.resultado()


if __name__ == "__main__":

    
    main()
