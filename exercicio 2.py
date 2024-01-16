
import math
import matplotlib.pyplot as plt

# Solicita um número ao usuário
numero = float(input("Digite um número: "))

# Verifica se o número é positivo ou negativo
if numero >= 0:
    # Calcula a raiz quadrada se o número for positivo
    raiz_quadrada = math.sqrt(numero)
    print(f"A raiz quadrada de {numero} é: {raiz_quadrada}")
else:
    # Mostra uma mensagem e exibe uma imagem se o número for negativo
    print(f"O número {numero} é inválido.")
    img = plt.imread('D:\PROJETOS DE TESTE\exercicio 1\errou.png')  
    plt.imshow(img)
    plt.axis('off')  # Oculta os eixos
    plt.show()
