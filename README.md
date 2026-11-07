# 🕸️ Algoritmos em Grafos - Python

Este repositório contém implementações de algoritmos desenvolvidos em Python. O objetivo deste projeto é servir como material de estudo e consulta para disciplinas de Algoritmos em Grafos.

## 🚀 Algoritmos Implementados

O projeto está dividido em scripts independentes, cada um focando em um conceito ou algoritmo específico:

1. **Buscas e Representação (`buscas_grafos.py`)**
   * Criação de grafos orientados.
   * Representação por Matriz de Adjacência e Lista de Adjacência.
   * **BFS (Busca em Largura):** Explora o grafo nível por nível.
   * **DFS (Busca em Profundidade):** Explora o grafo indo o mais fundo possível antes de retroceder.

2. **Caminhos Mínimos**
   * **`dijkstra.py`**: Algoritmo de Dijkstra para encontrar o menor caminho a partir de um vértice inicial. Utiliza fila de prioridade (`heapq`) para maior eficiência. *(Não aplicável a pesos negativos).*
   * **`bellman_ford.py`**: Algoritmo de Bellman-Ford para caminhos mínimos. Diferente do Dijkstra, é capaz de lidar com arestas de pesos negativos e detecta **ciclos negativos**.

3. **Árvores Geradoras Mínimas (AGM / MST)**
   * **`prim.py`**: Algoritmo de Prim para encontrar a Árvore Geradora Mínima de um grafo não orientado conexo.
   * **`kruskal.py`**: Algoritmo de Kruskal para AGM, implementado utilizando a eficiente estrutura de dados *Union-Find* (Conjuntos Disjuntos).

## 🛠️ Tecnologias Utilizadas

* **Python 3.x**
* Bibliotecas padrão do Python (como `heapq` para filas de prioridade). Nenhuma biblioteca externa é necessária.

## 💻 Como Executar

1. Clone este repositório para a sua máquina local:
   ```bash
   git clone [https://github.com/SEU_USUARIO/NOME_DO_REPOSITORIO.git](https://github.com/SEU_USUARIO/NOME_DO_REPOSITORIO.git)
