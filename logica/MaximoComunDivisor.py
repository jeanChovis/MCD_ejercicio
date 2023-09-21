from Exceptions.NumeroNegativo import NumeroNegativo

class MaximoComunDivisor():
    def validarTipo(self):
        while True:
            try:
                self.num1 = int(input("Ingrese el primer numero natural: "))
                self.num2 = int(input("Ingrese el segundo numero natural: "))

                if self.num1 < 0 or self.num2 < 0:
                    raise NumeroNegativo
                break
            except ValueError as err:
                print("Oops! Ingrese un número natural. Intente otra vez...")
            except NumeroNegativo as err:
                print("Oops! Ingrese un número mayor a cero. Intente otra vez...")
        return self.num1, self.num2

    def maximoDivisor(self, a, b):
        while b:
            a, b = b, a % b
        return a