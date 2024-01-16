import math
import matplotlib.pyplot as plt
from tkinter import *
from PIL import Image, ImageTk  # Para exibir a imagem na interface

def calcular_raiz():
    numero = float(.get("digite um numero"))
    if numero >= 0:
        raiz_quadrada = math.sqrt(numero)
        resultado_label.config(text=f"A raiz quadrada de {numero} é: {raiz_quadrada}")
    else:
        resultado_label.config(text=f"O número {numero} é inválido.")
        img = Image.open(D:\PROJETOS DE TESTE\exercicio 1\errou.png')  # Insira o caminho para sua imagem aqui
        img = img.resize((200, 200), Image.ANTIALIAS)  # Redimensiona a imagem
        img = ImageTk.PhotoImage(img)
        imagem_label.config(image=img)
        imagem_label.image = img  # Mantém uma referência para a imagem

# Criando a janela principal
root = Tk()
root.title("Calculadora de Raiz Quadrada")
root.geometry("400x300")

# Criando e posicionando os widgets na janela
label_instrucao = Label(root, text="Digite um número:")
label_instrucao.pack()

entry_numero = Entry(root)
entry_numero.pack()

calcular_button = Button(root, text="Calcular", command=calcular_raiz)
calcular_button.pack()

resultado_label = Label(root, text="", font=("Arial", 12))
resultado_label.pack()

imagem_label = Label(root)
imagem_label.pack()

root.mainloop()
