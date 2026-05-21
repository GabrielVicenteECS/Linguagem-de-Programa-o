temperatura = 0

while temperatura < 100:
    print("Termômetro °C - Limite 100°C")
    temperatura = int(input("Informe a temperatura: "))
    print("Temperatura: ", temperatura, "°C" )
    if temperatura >= 100:
        break