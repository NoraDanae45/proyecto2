from abc import ABC, abstractmethod

# Clase abstracta y herencia

class Persona (ABC):
    def __init__ (self, nombre, documento):
        self.nombre = nombre
        self.documento = documento

    @abstractmethod
    def mostrar_rol(self):
        pass

class Recepcionista(Persona):
    def mostrar_rol(self):
        return f"Recepcionista: {self.nombre}"
    def registrar_cliente(self):
        return f"{self.nombre} esta registrando un cliente"

#Asociacion

class Veterinario(Persona):
    def __init__(self, nombre, documento, especialidad):
        super().__init__(nombre,documento)
        self.especialidad = especialidad
        
    def mostrar_rol(self):
        return f"Veterinario: {self.nombre}"
    
    def atender_mascota(self):
        return f"{self.nombre} esta atendiendo una mascota"

# Agregacion

class Cliente(Persona):
    def __init__(self, nombre, documento):
        super().__init__(nombre, documento)
        self.mascotas = []

    def agregar_mascota(self, mascota):
        self.mascotas.append(mascota)

    def mostrar_mascotas(self):
        return [m.nombre for m in self.mascotas]
    
    def mostrar_rol(self):
        return f"Cliente: {self.nombre}"
    
class Mascota:
    def __init__(self, nombre, especie, edad, peso):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
        self.peso = peso

# Composicion

class Consulta:
    def __init__(self, veterinario, mascota):
        self.veterinario = veterinario
        self.mascota = mascota
        self.lista_tratamientos = []

    def crear_tratamiento(self, nombre, costo, duracion):
        tratamiento = Tratamiento(nombre, costo, duracion)
        self.lista_tratamientos.append(tratamiento)
    
    def mostrar_resumen(self):
        tratamientos = [t.nombre_t for t in self.lista_tratamientos]
        return f"Resumen clinico: Veterinario {self.veterinario.nombre}, Mascota: {self.mascota.nombre}, Tratamiento {tratamientos}"
    
    def calcular_costo_consulta(self):
       total = sum(t.costo for t in self.lista_tratamientos)
       return total
    
class Tratamiento:
    def __init__(self, nombre_t, costo, duracion_dias):
        self.nombre_t = nombre_t
        self.costo = costo
        self.duracion_dias = duracion_dias

    def mostrar_tratamiento(self):
        return f"Tratamiento: {self.nombre_t}, duracion: {self.duracion_dias} dias, costo: {self.costo}"
    
# Polimorfismo

class MetodoPago(ABC):
    @abstractmethod
    def procesar_pago(self, monto):
        pass

class PagoEfectivo(MetodoPago):
    def procesar_pago(self, monto):
        return f"Pago en efectivo ${monto} realizado"

class PagoTarjeta(MetodoPago):
    def procesar_pago(self, monto):
        return f"Pago con tarjeta ${monto} realizado"

class PagoTransferencia(MetodoPago):
    def procesar_pago(self, monto):
        return f"Pago con transferencia ${monto} realizado"
    

class Factura:
    def __init__(self, consulta, impuesto=0.19):
        self.consulta = consulta
        self.impuesto = impuesto
        self.total = 0
        
    def calcular_total(self):
        subtotal = self.consulta.calcular_costo_consulta()
        self.total = subtotal + (subtotal * self.impuesto)

        return self.total
    
    def pagar(self, metodo_pago):
        return metodo_pago.procesar_pago(self.total)
    

#Crear cliente 1
cliente1 = Cliente("Nora", "123456")
#Crear mascota 1
mascota1 = Mascota("Menchi", "Perro", 3, 10)
#Crear mascota 2
mascota2 = Mascota("Bochi", "gato", 7, 7)

# Asociación mascota- cliente
cliente1.agregar_mascota(mascota1)
cliente1.agregar_mascota(mascota2)

print(cliente1.mostrar_mascotas())

# Crear Veterinario
vet = Veterinario("Miguel", "7891011", "Cirugia")

# Crear consulta
consulta = Consulta(vet, mascota1)

# Crear tratamientos
consulta.crear_tratamiento("Vacuna", 200, 1)
consulta.crear_tratamiento("Desparasitación", 150, 3)

#Ver resumen
print(consulta.mostrar_resumen())

# Calcular costo
costo = consulta.calcular_costo_consulta()
print("Costo consulta: ", costo)

# Crear factura
factura = Factura(consulta, impuesto=0.19)
total = factura.calcular_total()
print("Total con impuesto: ", total)

# Pagos (Polimorfismo)
pago1 = PagoEfectivo()
pago2 = PagoTarjeta()
pago3 = PagoTransferencia()

print(factura.pagar(pago1))
print(factura.pagar(pago2))
print(factura.pagar(pago3))