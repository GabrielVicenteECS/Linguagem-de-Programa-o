print("===Escola de Esportes===")

idade=int(input("\nInforme a idade do participante para saber a Classificação: "))

if idade < 12:
    print("Infantil")
elif idade >= 12 and idade <= 17:
    print("Juvenil")
elif idade >= 18:
    print("Adulto")
    seguro=(input("Possui seguro saúde? (Sim/Não): "))
    if seguro != "Sim":
     print("Atenção: Seguro saúde obrigatório para adultos")