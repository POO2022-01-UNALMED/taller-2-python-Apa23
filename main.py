class Auto:
    cantidadCreados=0
    def __init__(self, modelo, precio, asientos, marca, motor, registro, ):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro
    
    def cantidadAsientos(self):
        return len(self.asientos)
    
    def verificarIntegridad(self):
        regMotor= self.motor.registro
        if(regMotor!=self.registro):
            return "Las piezas no son originales"
        regAsientos=self.asientos[0]
        for i in self.asientos:
            if(regAsientos!=i.registro):
                return "Las piezas no son originales"
            regAsientos =i.registro
        if(regAsientos!=self.registro):
            return "Las piezas no son originales"
        return "Auto original"

        
class Motor:
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro

    def cambiarRegistro(self, registro):
        self.registro=registro
    
    def asignarTipo(self, tipo):
        if(tipo == "electrico" or tipo=="gasolina"):
            self.tipo = tipo
        


class Asiento:
    def __init__(self, color, precio, registro):
        self.color= color
        self.precio = precio
        self.registro = registro
    
    def cambiarColor(self, color):
        colores=["rojo","amarillo","negro","blanco","verde","amarillo"]
        if(color is colores):
            self.color = color

