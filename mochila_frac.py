def mochila_frac(itens, capacidade_mochila):
    # Calcula valor por peso e guarda índice
    peso_valor = []
    for i, (peso, valor) in enumerate(itens):
        valor_por_peso = valor / peso
        peso_valor.append((valor_por_peso, peso, valor))

    # Ordena por valor/peso decrescente
    peso_valor.sort(reverse=True)

    itens_mochila = []
    valor_total = 0
    
    # Itera sobre a lista de itens pela maior relação valor/peso
    for valor_por_peso, peso, valor in peso_valor:    

        if capacidade_mochila >= peso:  # Verifica se o item inteiro cabe na mochila
            itens_mochila.append((peso, valor))     
            capacidade_mochila -= peso
            valor_total += valor 
        elif capacidade_mochila > 0:   # Se o item inteiro não cabe, mas ainda há espaço
            fracao = capacidade_mochila / peso  # Fraciona o item  
            itens_mochila.append((capacidade_mochila, valor * fracao)) #Coloca o Item fracionado 
            capacidade_mochila = 0
            break

    return itens_mochila, valor_total        

itens = [  # peso, valor
    (1, 5),
    (2, 6),
    (3, 1),
    (10, 5),
    (2, 4),
    (7, 3),
    (1, 1),
    (4, 7),
    (2, 2),
    (6, 6)
]

itens_mochila,valor_total = mochila_frac(itens, 30)

print("Itens na mochila (peso, valor):", itens_mochila)
print("Valor total:", valor_total)           