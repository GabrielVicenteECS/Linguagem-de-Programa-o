#Crie uma função chamada coverter_dolar
# que receba o valor_dolar e a cotacao.
# A função deve retornar o valor equivalente
# em Reais.
# No programa principal, peça os valores
# ao usuário e exiba o resultado
def converter_dolar(valor_dolar, cotacao):
   return  valor_dolar * cotacao

valor1 = float(input("Insira a quantia desejada em doláres: $"))
valor2 = float(input("Informe a cotação de hoje: "))

print("\nO valor em Reais é: R$", converter_dolar(valor1, valor2))