while True:
 velocidade = int(input("Digite a velocidade do veículo: "))
 multa = (velocidade - 80) * 7

 if velocidade <= 80:
    print("Dentro do limite de velocidade. ")
 else: 
    print("Acima do limite de velocidade, 80KM/H, multado em: ", multa)

 sair = str(input("Deseja continuar? Digite Sim ou Não: "))
 if sair != "Sim":
  break

