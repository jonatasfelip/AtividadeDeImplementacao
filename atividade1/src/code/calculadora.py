import unittest
menu = """
1...............Somar
2...............Subtrair
3...............Multiplicar
4...............Dividir
"""

print(menu)

opc = int(input("Informe uma operação:"))

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

    def Dividir(num1, num2): 
        """Método de dividir que recebe dois números e retorna a divisão deles"""
        dividir = num1 / num2
        return dividir

    def Documentacao():
        documentacao = Calculadora.__doc__, Calculadora.Somar.__doc__,
        Calculadora.Subtrair.__doc__, Calculadora.Multiplicar.__doc__ ,
        Calculadora.Dividir.__doc__
        return documentacao

class Teste(unittest.TestCase):
    def teste_soma(self):
        self.assertEqual(Calculadora.Somar(4,2),6)

    def teste_subtrair(self):
        self.assertEqual(Calculadora.Subtrair(8,1),7)

    def teste_multiplicar(self):
        self.assertEqual(Calculadora.Multiplicar(9,9),81)

    def teste_dividir(self):
        self.assertEqual(Calculadora.Dividir(125,5),25)

if (opc == 1):
    print(num1, " + ", num2, " = ", Calculadora.Somar(num1, num2))

elif (opc == 2):
    print(num1, " - ", num2, " = ", Calculadora.Subtrair(num1, num2))

elif (opc == 3):
    print(num1, " * ", num2, " = ", Calculadora.Multiplicar(num1, num2))

elif (opc == 4):
    print(num1, " / ", num2, " = ", Calculadora.Dividir(num1, num2))

else:
    print("Informe uma opção válida!")

if __name__ == '__main__':
    unittest.main()



