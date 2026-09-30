numero1 = int(input("Digite o primeiro numero:"))
numero2 = int(input("Digite o segundo numero:"))
operacao = input("Digite a operação:")
if operacao == "+":
    resultado = numero1 + numero2
    print(resultado)
elif operacao == "-":
    resultado = numero1 - numero2
    print(resultado)
elif operacao == "*":
    resultado = numero1 * numero2
    print(resultado)
elif operacao == "/":
    if numero2 != 0:
        resultado = numero1 / numero2
        print(resultado)
    else:
        print("Não é possível dividir por zero")
else:
    print("operação invalida")