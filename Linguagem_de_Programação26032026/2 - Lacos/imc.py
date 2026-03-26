peso = float(input("Digite seu peso em kilogramas: "))
altura = float(input("Digite sua altura em metros: "))

imc = peso / (altura * altura)

print("IMC (Indice de Massa Corporal):", imc)

if imc <= 18.5:
    print("Abaixo do peso!! ")

elif imc < 25:
    print("Você está no peso normal! ")

elif imc < 30:
    print ("Dentro da faixa de sobrepeso!!: ")

else:
    print("Dentro da faixa de obesidade!!!")