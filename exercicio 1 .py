# Solicita dois números ao usuário
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Verifica qual número é maior
if num1 > num2:
    print(f"O número {num1} é maior que {num2}.")
elif num2 > num1:
    print(f"O número {num2} é maior que {num1}.")
else:
    print("Os números são iguais.")