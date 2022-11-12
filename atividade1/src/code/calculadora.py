menu = """
1...............Somar
2...............Subtrair
3...............Multiplicar
4...............Dividir
"""

print(menu)

opc = int(input("Informe uma operação: "))

num1 = int(input("Informe um número: "))
num2 = int(input("Informe outro número: "))

class Calculadora: 
    """Classe calculadora que engloba métodos respectivos às operações: somar, subtrair, multiplicar e dividir"""
    def Somar(num1, num2):
        """Método de somar que recebe dois números e retorna a adição deles"""
        soma = num1 + num2
        return soma

    def Subtrair(num1, num2): 
        """Método de subtrair que recebe dois números e retorna a subtração deles"""
        subtrair = num1 - num2
        return subtrair

    def Multiplicar(num1, num2): 
        """Método de multiplicar que recebe dois números e retorna a multiplicação deles"""
        multiplicar = num1 * num2
        return multiplicar