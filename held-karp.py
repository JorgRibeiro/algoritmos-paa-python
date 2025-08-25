import itertools

def held_karp(dist_matrix):
    n = len(dist_matrix)
    memo = {}  # Dicionário para memoização (programação dinâmica)

    # --- Passo 1: Casos base ---
    # Inicializa a tabela de memoização com os custos para ir do nó inicial (0)
    # para qualquer outro nó. O subconjunto de nós visitados contém apenas {0, k}.
    for k in range(1, n):
        # A chave é uma tupla: (frozenset do subconjunto, nó final)
        # Usamos frozenset porque é imutável e pode ser usado como chave de dicionário.
        memo[(frozenset([0, k]), k)] = (dist_matrix[0][k], [0, k])

    # --- Passo 2: Iterar sobre subconjuntos de tamanhos crescentes ---
    # Itera de 3 até n (tamanho do subconjunto)
    for subset_size in range(3, n + 1):
        # Gera todas as combinações de subconjuntos do tamanho atual que contêm o nó 0
        for subset_tuple in itertools.combinations(range(n), subset_size):
            subset = frozenset(subset_tuple)
            if 0 not in subset:
                continue

            # Para cada nó final 'k' no subconjunto atual
            for k in subset:
                if k == 0:
                    continue

                # Subconjunto anterior (sem o nó final 'k')
                prev_subset = subset - {k}
                min_cost = float('inf')
                best_prev_node = -1
                
                # Encontra o caminho mais curto para chegar em 'k' a partir de um nó 'm' no subconjunto anterior
                for m in prev_subset:
                    if m == 0:
                        continue
                        
                    # Custo = custo do subproblema anterior + distância do nó 'm' ao 'k'
                    cost = memo[(prev_subset, m)][0] + dist_matrix[m][k]

                    if cost < min_cost:
                        min_cost = cost
                        best_prev_node = m
                
                # Armazena o custo mínimo e o caminho para chegar em 'k'
                path = memo[(prev_subset, best_prev_node)][1] + [k]
                memo[(subset, k)] = (min_cost, path)

    # --- Passo 3: Calcular o custo final do tour ---
    # Considera o custo de voltar ao nó inicial 0 a partir do último nó visitado
    full_set = frozenset(range(n))
    min_tour_cost = float('inf')
    final_path = []

    for k in range(1, n):
        # Custo total = custo para chegar em 'k' visitando todos os nós + distância de 'k' de volta para 0
        cost, path = memo[(full_set, k)]
        total_cost = cost + dist_matrix[k][0]

        if total_cost < min_tour_cost:
            min_tour_cost = total_cost
            final_path = path + [0] # Adiciona o retorno ao início

    return min_tour_cost, final_path

# --- Instância do Problema ---
# Matriz de distâncias para 4 cidades (0, 1, 2, 3)
distancias = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

# --- Execução do Algoritmo ---
custo_otimo, caminho_otimo = held_karp(distancias)

# --- Exibição dos Resultados ---
print("--- Problema do Caixeiro Viajante com Held-Karp ---")
print(f"Matriz de Distâncias: {distancias}")
print("\n--- Resultado ---")
print(f"O custo mínimo do tour é: {custo_otimo}")
# Ajusta o caminho para mostrar a numeração das cidades a partir de 1 para melhor leitura
caminho_legivel = [node + 1 for node in caminho_otimo]
print(f"O caminho ótimo é: {' -> '.join(map(str, caminho_legivel))}")