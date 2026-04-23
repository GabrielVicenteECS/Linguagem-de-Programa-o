valor_1 = float(input("Digite o valor: "))
operacao = (input("\n Informe a operação desejada " \
"\n Operações disponíveis: +, -, *, / " \
"\n Operação:  "))
valor_2 = float(input("\n Digite o valor: "))


match operacao:
     case "+":
      print ("O valor da soma é: ", valor_1 + valor_2)
     case "-":
      print ("O valor da subtração é: ", valor_1 - valor_2)
     case "*":
      print ("O valor da multiplicação é: ", valor_1 * valor_2)
     case "/":
      print ("O valor da divisão é: ", valor_1 / valor_2)
     case _:
      print ("Informe uma operação válida")
