#Crie um progrma que pede para o usuário digitar 3 notas de um aluno
#Em seguida, o progrma deve calcular a média e mostrar na tela!
while True:
 nota_1 = float(input("Digite a primeira nota: "))
 nota_2 = float(input("Digite a segunda nota: "))
 nota_3 = float(input("Digite a terceira nota: "))

 media = (nota_1 + nota_2 + nota_3) / 3

 print(" A nota média é: ", media)

 if media >= 6:
  print("Aprovado!", media)
 else:
  print("Reprovado!", media)

 sair = str(input("Deseja continuar?: S ou N"))
 if sair == "N":
  break