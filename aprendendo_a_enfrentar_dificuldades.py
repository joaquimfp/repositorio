# Defina as calorias para cada item individual
panqueca_de_banana = 350
café_preto = 70
torrada_com_queijo = 275
arroz = 230
feijão = 230
frango = 153
legumes = 69
macarrão = 378
ovo = 144
barrinha_de_chocolate = 205

# Crie listas para as refeições
café_da_manhã = [panqueca_de_banana, café_preto, torrada_com_queijo]
almoço = [arroz, feijão, frango, legumes]
jantar = [macarrão, barrinha_de_chocolate, ovo]

# Calcule o total de calorias para cada refeição
total_café_da_manhã = sum(café_da_manhã)
total_almoço = sum(almoço)
total_jantar = sum(jantar)

# Calcule o total de calorias para o dia inteiro
total_calorias_dia = total_café_da_manhã + total_almoço + total_jantar

# Exiba os totais de calorias
print(f"Total de calorias no café da manhã: {total_café_da_manhã} kcal")
print(f"Total de calorias no almoço: {total_almoço} kcal")
print(f"Total de calorias no jantar: {total_jantar} kcal")
print(f"Total de calorias no dia inteiro: {total_calorias_dia} kcal")
