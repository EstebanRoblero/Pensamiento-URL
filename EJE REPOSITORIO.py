# EJERCICIO 1

# class ExperimentoFisico:
#     def realizar_experimento(self):
#         print("Este método debe ser implementado por una subclase.")

# class CaidaLibre(ExperimentoFisico):
#     def __init__(self,altura,gravedad):
#         self.altura=altura
#         self.gravedad=gravedad

#     def realizar_experimento(self):
#         if self.altura<0:
#             print("el error es que La altura no puede ser negativa.")
#             return
#         if self.gravedad==0:
#             print("no es posible que la gravedad sea cero.")
#             return

#         tiempo=((2*self.altura)/self.gravedad)**0.5
#         print("Tiempo de caída:", round(tiempo, 2), "segundos")


# try:
#     metros=float(input("puede ingresar la altura en metros: "))
#     cuadrado=float(input("puede ingresar la gravedad en m/s²: "))

#     experimento=CaidaLibre(altura=metros, gravedad=cuadrado)
#     experimento.realizar_experimento()

# except ValueError:
#     print("esto es un error  ingrese los numeros validos ")


# EJERCICIO 2


class Raiz:
    def calcular(self,n):
        print("sintax error"if n<0 else round(n**0.5,2))

class Potencia:
    def calcular(self,b,e):
        print(b**e)

class Logarimo:
    def calcular(self,n):
        print("sintax error"if n<=0 else round(n**0.5, 2))

class Factorial:
    def calcular(self,n):
        if n<0 or n!=int(n): print("Error")
        else:
            x=1
            for i in range(1,int(n)+1): x*=i
            print(x)

calcular=input(" oprcion 1=Raíz opcion 2=Pot opcion 3=Log opcion 4=Fact: ")
if calcular=="1":
    Raiz().calcular(float(input("numero: ")))
elif calcular=="2":
    Potencia().calcular(float(input("base: ")), float(input("Exp: ")))
elif calcular== "3":
    Logarimo().calcular(float(input("numero: ")))
elif calcular=="4":
    Factorial().calcular(float(input("numero: ")))
else:
    print("la opción no es valida intente de nuevo")