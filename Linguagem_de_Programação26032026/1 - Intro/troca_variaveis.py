#Exercício: O Mistério das Variáveis Trocadas
#O Contexto:
#Imagine que você tem duas variávis no Python guardem

#A variável gaveta_A está guardando "Mouse".

#A variável gaveta_B está guardando "Teclado".

#O desafio::
#Seu objetivo é escrever um código que troque os
#Valores das duas. No final, a gaveta_A deve exibir "Teclado e a gaveta_B deve exibir "Mouse"

gaveta_A = "Mouse"
gaveta_B = "Teclado"
auxiliar = 0

auxiliar = gaveta_A
gaveta_A = gaveta_B
gaveta_B = auxiliar



print("Gaveta A: " , gaveta_A)
print("Gaveta B: " , gaveta_B)

