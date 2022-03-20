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
        count=0
        for i in self.asientos:
            if type(i)==Asiento:
                count+=1
        return count
    
    def verificarIntegridad(self):
        regMotor= self.motor.registro
        if(regMotor!=self.registro):
            return "Las piezas no son originales"
       
        for i in self.asientos:
            if type(i)==Asiento:
                if(self.registro!=i.registro):
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
        colores=["rojo","amarillo","negro","blanco","verde"]
        if(color in colores):
            self.color = color



a1 = Asiento("blanco", 5000, 435)
a2 = Asiento("blanco", 5000, 435)

a1.cambiarColor("naranja")
a2.cambiarColor("verde")

ok = False

if(a1.color == "blanco" and a2.color == "verde"):
    ok = True

print(ok)
