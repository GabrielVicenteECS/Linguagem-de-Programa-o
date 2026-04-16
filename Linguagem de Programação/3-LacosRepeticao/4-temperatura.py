# A defesa civil de Itajaí registrou as temperaturas
# médias de 7 dias: [22, 15, 14, 25, 17, 28, 13]
# crie um progrma que percorra essa lista e,
# ao final, informe ao usuário quantos desses dias,
# tiveram temperaturas abaixo de 18°C.
#e a temperatura média da semana.

temperaturas = [22, 15, 14, 25, 17, 28, 13,]
contador = 0
media = 0
dias = 0

for y in temperaturas:
    media = media + y
    dias = dias + 1

    if y <= 18:
        print("Temperatura do dia: ", y,"°C")
        contador = contador + 1

print("Temperatura média: {:.2f}" .format(media / dias),"°C")
print("Dias com temperatura inferior a 18°C: ", contador,"dias")