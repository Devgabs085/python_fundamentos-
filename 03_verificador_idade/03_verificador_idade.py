idade = int(input("Digite a sua idade:"))
if idade < 0:
    print("idade invadlida")
else:
    if idade >= 18:
        print("maior de idade")
    else:
        print("Menor de idade")