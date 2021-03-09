

def sumar(num1 , num2):
    return num1 + num2



def multiplicar(num1 , num2):
    return num1 * num2

def calculadora(num1 , num2):
    if(funcion == 'sumar'):
        sumar(num1 , num2)
    else:
        multiplicar(num1,num2)

num1 = input()
num2 = input()
funcion = input()

calculadora(num1 , num2)