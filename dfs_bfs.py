def criar_grafo():
    n = int(input("Digite o número de vértices: "))
    
    # Criar matriz
    matriz = []
    for i in range(n):
        matriz.append([0] * n)
        
    # Criar lista de adjacência
    lista = []
    for i in range(n):
        lista.append([])
        
    # Conjunto para controlar arestas repetidas
    arestas_cadastradas = set()
    quantidade = int(input("Digite o número de arestas: "))
    contador = 0
    
    while contador < quantidade:
        print(f"\nAresta {contador + 1}")
        origem = int(input("Vértice de origem: "))
        destino = int(input("Vértice de destino: "))
        
        # Validar vértices
        if origem < 1 or origem > n or destino < 1 or destino > n:
            print("ERRO: vértice inválido!")
            print(f"Digite vértices entre 1 e {n}")
            continue
            
        # Não permitir laços
        if origem == destino:
            print("ERRO: não é permitido ligar um vértice a ele mesmo!")
            continue
            
        # No grafo orientado a ordem importa
        aresta = (origem, destino)
        
        # Verificar repetição
        if aresta in arestas_cadastradas:
            print("ERRO: esta aresta já foi cadastrada!")
            continue
            
        arestas_cadastradas.add(aresta)
        
        # Matriz de adjacência
        matriz[origem - 1][destino - 1] = 1
        # Lista de adjacência
        lista[origem - 1].append(destino)
        contador += 1
        
    print("\nGrafo criado com sucesso!")
    return n, matriz, lista

# -----------------------------
# Mostrar o grafo
# -----------------------------
def mostrar_grafo(n, matriz, lista):
    print("\nMATRIZ DE ADJACÊNCIA")
    for linha in matriz:
        print(linha)
        
    print("\nLISTA DE ADJACÊNCIA")
    for i in range(n):
        print(f"{i + 1} -> {lista[i]}")

# -----------------------------
# Busca em Profundidade - DFS
# -----------------------------
def busca_profundidade(lista, inicio):
    visitados = set()
    
    def dfs(vertice):
        visitados.add(vertice)
        print(vertice, end=" ")
        
        for vizinho in lista[vertice - 1]:
            if vizinho not in visitados:
                dfs(vizinho)
                
    print("\nBUSCA EM PROFUNDIDADE:")
    dfs(inicio)
    print()

# -----------------------------
# Busca em Largura - BFS
# -----------------------------
def busca_largura(lista, inicio):
    visitados = set()
    fila = []
    
    fila.append(inicio)
    visitados.add(inicio)
    print("\nBUSCA EM LARGURA:")
    
    while fila:
        vertice = fila.pop(0)
        print(vertice, end=" ")
        
        for vizinho in lista[vertice - 1]:
            if vizinho not in visitados:
                visitados.add(vizinho)
                fila.append(vizinho)
    print()

# -----------------------------
# Programa principal
# -----------------------------
n = 0
matriz = []
lista = []

while True:
    print("\n==============================")
    print(" MENU - GRAFOS")
    print("==============================")
    print("1 - Criar Grafo")
    print("2 - Mostrar Grafo")
    print("3 - Busca em Profundidade")
    print("4 - Busca em Largura")
    print("5 - Sair")
    print("==============================")
    
    opcao = input("Escolha uma opção: ")
    
    # Criar grafo
    if opcao == "1":
        n, matriz, lista = criar_grafo()
        
    # Mostrar grafo
    elif opcao == "2":
        if n == 0:
            print("ERRO: primeiro crie o grafo!")
        else:
            mostrar_grafo(n, matriz, lista)
            
    # Busca em profundidade
    elif opcao == "3":
        if n == 0:
            print("ERRO: primeiro crie o grafo!")
        else:
            inicio = int(input("Digite o vértice inicial: "))
            if inicio < 1 or inicio > n:
                print("ERRO: vértice inválido!")
            else:
                busca_profundidade(lista, inicio)
                
    # Busca em largura
    elif opcao == "4":
        if n == 0:
            print("ERRO: primeiro crie o grafo!")
        else:
            inicio = int(input("Digite o vértice inicial: "))
            if inicio < 1 or inicio > n:
                print("ERRO: vértice inválido!")
            else:
                busca_largura(lista, inicio)
                
    # Sair
    elif opcao == "5":
        print("Programa encerrado.")
        break
        
    else:
        print("Opção inválida!")