import networkx as nx
from collections import deque
import matplotlib.pyplot as plt

def gerar_vizinhos(estado, capacidades):
    n = len(estado)
    vizinhos = []

    for i in range(n):
        # Encher o vaso i
        if estado[i] < capacidades[i]:
            novo = list(estado)
            novo[i] = capacidades[i]
            vizinhos.append(tuple(novo)) 

        # Esvaziar o vaso i
        if estado[i] > 0:
            novo = list(estado)
            novo[i] = 0
            vizinhos.append(tuple(novo))

        # Transferir do vaso i para o vaso j
        for j in range(n):
            if i != j and estado[i] > 0 and estado[j] < capacidades[j]:
                novo = list(estado)
                transferir = min(estado[i], capacidades[j] - estado[j])
                novo[i] -= transferir
                novo[j] += transferir
                vizinhos.append(tuple(novo))

    return vizinhos

def vasos(vasos, capacidades, alvo):
    G = nx.DiGraph()
    inicial = tuple(vasos)
    fila = deque([inicial])
    visitados = set([inicial])

    # Construir grafo de estados possíveis
    while fila:
        atual = fila.popleft()

        if alvo in atual:
            break

        for viz in gerar_vizinhos(atual, capacidades):
            if viz not in visitados:
                visitados.add(viz)
                fila.append(viz)
                G.add_edge(atual, viz, weight=1)

    # Encontrar caminho até algum estado que contenha o alvo
    destinos = [n for n in G.nodes if alvo in n]
    if not destinos:
        print("Impossível alcançar o alvo.")
        return

    menor_destino = min(destinos, key=lambda d: nx.shortest_path_length(G, inicial, d))
    caminho = nx.shortest_path(G, inicial, menor_destino)

    print(f"Alvo {alvo} encontrado em {len(caminho)-1} passos:")
    for passo in caminho:
        print(passo)

    # Visualização
    pos = nx.spring_layout(G, seed=42)  # layout fixo
    plt.figure(figsize=(12, 10))

    # Desenhar todos os nós e arestas
    nx.draw(G, pos, with_labels=False, node_size=300, node_color="lightgray", edge_color="gray", arrowsize=10)
    nx.draw_networkx_labels(G, pos, labels={n: str(n) for n in G.nodes}, font_size=8)

    # Destacar o caminho encontrado
    edge_path = list(zip(caminho[:-1], caminho[1:]))
    nx.draw_networkx_edges(G, pos, edgelist=edge_path, edge_color="red", width=2)
    nx.draw_networkx_nodes(G, pos, nodelist=caminho, node_color="red", node_size=400)

    plt.title(f"Menor caminho até alcançar {alvo}L")
    plt.axis("off")
    plt.show()


vasos([0, 0, 0], [3, 5, 8], 4)
