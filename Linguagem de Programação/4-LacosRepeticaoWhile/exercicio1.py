numero = 1
soma = 0

while numero != 0: 
    numero = int(input("Digite um número: "))
    soma+=numero
    if numero == 0:
        print("A soma de todos os números é: ", soma)