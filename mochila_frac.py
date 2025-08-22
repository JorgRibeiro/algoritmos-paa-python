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

# Calcula valor por peso e guarda índice
peso_valor = []
for i, (peso, valor) in enumerate(itens):
    valor_por_peso = valor / peso
    peso_valor.append((valor_por_peso, peso, valor))

# Ordena por valor/peso decrescente
peso_valor.sort(reverse=True)

capacidade_mochila = 30
itens_mochila = []
valor_total = 0
      
for valor_por_peso, peso, valor in peso_valor:
    if capacidade_mochila >= peso:
        itens_mochila.append((peso, valor))  # item inteiro
        capacidade_mochila -= peso
        valor_total += valor 
    elif capacidade_mochila > 0:
        fracao = capacidade_mochila / peso
        itens_mochila.append((capacidade_mochila, valor * fracao))  # item fracionado
        valor_total += valor * fracao
        capacidade_mochila = 0
        break

print("Itens na mochila (peso, valor):", itens_mochila)
print("Valor total:", valor_total)   
        

        