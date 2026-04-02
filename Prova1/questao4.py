valor_produto = float(input("Informe o valor do produto: "))
pagamento = int(input("Digite 1 para pagar à Vista ou 2 para pagar Parcelado: "))

valor_vista = valor_produto - (valor_produto * 0.10)
valor_parcelado = valor_produto / 3

if pagamento == 1:
    print("Valor a pagar: ", valor_vista )
else:
    print("Valor a pagar em parcelas (3x): ", valor_parcelado)