def Calculator():
 while True:
   print("=== CALCULADORA == ===")


#Dados
try:
  num1 = float(input("Digite o primeiro número: "))
  operacao = input("Digite a operacao (+, -, *, /): ")
  num2 = float(input("Digite o segundo número: "))

#Operação
  if operacao == "+":
     resultado = num1 + num2
  elif operacao == "-":
     resultado = num1 - num2
  elif operacao == "*":
     resultado = num1 * num2
  elif operacao == "/":
     resultado = num1 / num2
     if num2 != 0:
         resultado = num1 / num2
     else:
         resultado = "Erro: Divisão por zero."
  else:
     resultado = "Operação inválida."

  print(f"Resultado: {resultado}")

except ValueError:
   print("Erro: Entrada inválida. Digite números.")

   continuar = input("Deseja fazer outro cálculo? (s/n): ").lower()

   if continuar.lower() != "s":
         break

Calculator()