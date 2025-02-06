import os

class Cinepolis:
    def __init__(self):
        self.precio_boleto = 12
        self.archivo_ventas = "Corte.txt"
        with open(self.archivo_ventas, "w") as archivo:
            archivo.write("Ventas\n")

    def menu1(self):
        print("\n Bienvenido :V")
        print("1. Comprar boletos")
        print("2. Finalizar")

    def pago(self):
        print("\n Método de Pago ")
        print("1. Tarjeta")
        print("2. Efectivo")

    def descuentos(self, num_boletos, total):
        if 3 <= num_boletos <= 5:
            return total * 0.10  
        elif num_boletos > 5:
            return total * 0.15  
        return 0  

    def tarjeta(self, total):
        return total * 0.10  

    def guardar_venta(self, nombre, num_boletos, total_con_descuento):
        with open(self.archivo_ventas, "a") as archivo:
            archivo.write(f"Cliente: {nombre}, Boletos: {num_boletos}, Total: ${total_con_descuento:.2f}\n")

    def leer_ventas(self):
        print("\nHistorial de Ventas \n")
        total_ventas = 0
        try:
            with open(self.archivo_ventas, "r") as archivo:
                for linea in archivo:
                    print(linea.strip())
                    if "Total:" in linea:
                        total_ventas += float(linea.split("$")[1])
        except FileNotFoundError:
            print("No hay ventas aún")
        print(f"Total de ventas: ${total_ventas:.2f}")

    def comprar_boletos(self):
        while True:
            nombre = input("Ingrese su nombre: ")
            while True:
                try:
                    num_personas = int(input("¿Cuántas personas son? "))
                    if num_personas <= 0:
                        print("Debe haber al menos un cliente.")
                        continue
                    break
                except ValueError:
                    print("Ingrese una cantidad válida.")

            while True:
                max_boletos = num_personas * 7
                print(f"Tu máximo de boletos permitidos es {max_boletos}.")
                try:
                    num_boletos = int(input("¿Cuántos boletos comprará? "))
                    if num_boletos <= 0 or num_boletos > max_boletos:
                        print("Número de boletos no permitido. Ajuste el número de personas si es necesario.")
                        continue  
                    break
                except ValueError:
                    print("Ingrese un número válido.")
            
            total = num_boletos * self.precio_boleto
            descuento = self.descuentos(num_boletos, total)
            total_con_descuento = total - descuento

            print(f"\nTotal sin descuento: ${total:.2f}")
            print(f"Descuento aplicado: -${descuento:.2f}")
            print(f"Total después del descuento: ${total_con_descuento:.2f}\n")

            self.pago()
            while True:
                metodo_pago = input("¿Cuál será su método de pago? ")
                if metodo_pago == "1":  
                    descuento_tarjeta = self.tarjeta(total_con_descuento)
                    total_con_descuento -= descuento_tarjeta  
                    print(f"Descuento por pago con tarjeta: -${descuento_tarjeta:.2f}")
                    print(f"Total Final: ${total_con_descuento:.2f}\n")
                    break
                elif metodo_pago == "2":  
                    print(f"Total Final: ${total_con_descuento:.2f}\n")
                    break
                else:
                    print("Opción no válida. Intente nuevamente.")

            self.guardar_venta(nombre, num_boletos, total_con_descuento)
            print("\n¿Desea realizar otra compra?")
            print("1. Hacer otra compra")
            print("2. Finalizar")
            otra_compra = input("Seleccione una opción ")
            if otra_compra == "2":
                self.leer_ventas()
                break

    def iniciar(self):
        while True:
            self.menu1()
            opcion = input("Seleccione una opción ")
            if opcion == "1":
                self.comprar_boletos()
            elif opcion == "2":
                print("Gracias por su compra")
                self.leer_ventas()
                break
            else:
                print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    cinepolis = Cinepolis()
    cinepolis.iniciar()
