from logica.MaximoComunDivisor import MaximoComunDivisor

if __name__ == '__main__':

    divisor = MaximoComunDivisor()

    numero1, numero2 = divisor.validarTipo()

    resultado = divisor.maximoDivisor(numero1, numero2)

    print(f"El maximo comun divisor es : {resultado}")
