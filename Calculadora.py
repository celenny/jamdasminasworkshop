def calculadora():
    operador = input("Escolha entre as operações +, -, * ou /:")
    n1 = input("Digite o primeiro numero: ")
    n2 = input("Digite o segundo numero: ")

    if float(n1) and float(n2):
        n1 = float(n1)
        n2 = float(n2)
        if operador == "+":
            resultado = n1 + n2
            print(resultado)
        elif operador == "-":
            resultado = n1 - n2
            print(resultado)
        elif operador == "*":
            resultado = n1 * n2
            print(resultado)
        elif operador == "/":
            resultado = n1 / n2
            print(resultado)
        else:
            print("Operador inválido!")

    else:
        print("Digite números!!")

def float(s:str):
    try:
        f = float(s)
        return True
    except:
        return False

calculadora()
