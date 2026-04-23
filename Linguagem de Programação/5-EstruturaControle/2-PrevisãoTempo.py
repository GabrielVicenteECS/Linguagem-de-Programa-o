clima = int(input("Informe o clima:" \
"\n 1 se está com Sol," \
"\n 2 se está Chuva," \
"\n 3 se está Nublado," \
"\n 4 se está Neve. " \
"\n Clima: "))

match clima:
 case 1 | 3:
  print("Leve um óculos escuro")
 case 2 | 4:
  print("Não esqueça o guarda-chuva ou casaco")
 case _:
  print("Informe o Clima!")
