#Exercício: Classificador de Escalões de Idade

#Um sistema de inscrições para um evento desportivo precisa
#de categorizar os participantes automaticamente cp, nase
#na idade introduzida. Regras de classificação:

#Idade inferior a 12 anos: "Escalão Infantil"
#Idae entre 12 e 17 anos: "Escalão Juvenil"
#Idade igual ou superior a 18 anos: "Escalão Adulto"

print("===Evento Desportivo 2026===")

idade=int(input("\nInforme a idade do participante para saber a modalidade: "))

if idade < 12:
    print("Escalão Infantil");
elif idade >= 12 and idade <= 17:
    print("Escalão Juvenil");
elif idade >= 18:
    print("Escalão Adulto");

