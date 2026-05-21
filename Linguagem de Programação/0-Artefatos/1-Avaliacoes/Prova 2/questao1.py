codigo_carga = int(input("Informe o código da carga, 1 a 5: "))

match codigo_carga:
 case 1 | 2 | 3:
  print("Carga Geral / Manufaturados")
 case 4 |5:
  print("Produtos Perecíveis / Refrigerados")
 case _:
  print("Código inválido - Consultar Supervisor")