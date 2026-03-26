# Um parque de diversões exige que uma criança tenha 
# pelo menos 1.40m de altura para andar na Montanha Russa.
# E que ela seja maior que de 15 anos
# Vamos criar um sensor digital para o operador do brinquedo?

idade = int(input("Digite a idade da pessoa: "))
altura = float(input("Digite a altura da pessoa em metros: "))

resultado = idade and altura

if idade >= 15 and altura >= 1.40:
 resultado = True;
 print("Pode andar na Montanha-Russa")
else:
 resultado = False;
 print("Pessoa não autorizada a andar na Montanha-Russa")