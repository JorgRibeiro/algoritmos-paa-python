import heapq

def dijkstra_classico(grafo, inicio):
    # Dicionário para armazenar as distâncias mais curtas conhecidas
    # Todos começam com infinito, exceto o nó inicial, que é 0
    distancias = {no: float('infinity') for no in grafo}
    distancias[inicio] = 0

    # Dicionário para reconstruir o caminho
    predecessores = dict.fromkeys(grafo, None)

    # A fila armazena tuplas de (distância, nó). O heapq sempre manterá
    # a tupla com a menor distância no topo (índice 0).
    fila_prioridade = [(0, inicio)]

    # O loop continua enquanto houver nós "abertos" para explorar na fila.
    while fila_prioridade:
        # Pega o nó da fila que atualmente tem a menor distância da origem.
        distancia_atual, no_atual = heapq.heappop(fila_prioridade)

        # Para cada vizinho do nó atual, verificamos se podemos melhorar (encurtar) o caminho até ele.
        for vizinho, peso in grafo[no_atual]:
            nova_distancia = distancia_atual + peso

            # Se encontrarmos um caminho mais curto para o vizinho
            if nova_distancia < distancias[vizinho]:
                # atualizamos sua distância e seu predecessor
                distancias[vizinho] = nova_distancia
                predecessores[vizinho] = no_atual
                # e o adicionamos à fila para ser explorado futuramente.
                heapq.heappush(fila_prioridade, (nova_distancia, vizinho))

    # Retorna as distâncias finais e os predecessores para reconstrução dos caminhos.
    return distancias, predecessores



grafo = {
    'A': [('B', 13), ('C', 12), ('D', 13)],
    'B': [('A', 12), ('G', 9)],
    'C': [('E', 9), ('D', 2)],
    'D': [('B', 18), ('F', 4)],
    'E': [('F', 6), ('I', 10)],
    'F': [('I', 18), ('H', 14)],
    'G': [('F', 18), ('J', 16)],
    'H': [('J', 11), ('G', 8)],
    'I': [('H', 19)],
    'J': [('H', 14), ('I', 2)]
}

no_inicial = 'A'
distancias_finais, predecessores_finais = dijkstra_classico(grafo, no_inicial)

print("Dicionário de distâncias:")
print(distancias_finais)
    
no_destino = 'J'
print(f"\nDistância para '{no_destino}': {distancias_finais.get(no_destino, 'Inalcançável')}")