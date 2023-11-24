from datetime import datetime

class Automovil:

    def __init__(self, marca, modelo, num_asientos, color, tipo, tipo_combustible, precio, años_garantia, fecha_de_ingreso):
        self.marca = marca
        self.modelo = modelo
        self.num_asientos = num_asientos
        self.color = color
        self.tipo = tipo
        self.tipo_combustible = tipo_combustible
        self.precio = precio
        self.años_garantia = años_garantia
        self.fecha_de_ingreso = fecha_de_ingreso

    def informacion_carro(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Asientos: {self.num_asientos}")
        print(f"Color: {self.color}")
        print(f"Tipo: {self.tipo}")
        print(f"Precio: ${self.precio}")
        print(f"Garantia: {self.años_garantia} años")
        print(f"Fecha: {self.fecha_de_ingreso.strftime('%d-%B-%Y')}")
        print()

# Autos
print("---Autos---")
print()
Automovil1 = Automovil("Mitsubishi", "Outlander", 5, "Rojo", "SUV", "Gasolina", 30000, 3, datetime(2023, 1, 1))
Automovil2 = Automovil("Kia", "Sorento", 7, "Azul", "SUV", "Híbrido", 35000, 5, datetime(2023, 2, 15))
Automovil3 = Automovil("Toyota", "Camry", 5, "Plateado", "Sedán", "Gasolina", 25000, 2, datetime(2023, 3, 10))
Automovil4 = Automovil("Nissan", "Rogue", 5, "Negro", "SUV", "Gasolina", 28000, 4, datetime(2023, 4, 5))
Automovil5 = Automovil("Hyundai", "Tucson", 5, "Blanco", "SUV", "Eléctrico", 32000, 3, datetime(2023, 5, 20))

# Informacion de los autos

Automovil1.informacion_carro()
Automovil2.informacion_carro()
Automovil3.informacion_carro()
Automovil4.informacion_carro()
Automovil5.informacion_carro()
