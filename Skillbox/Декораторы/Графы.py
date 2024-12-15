import networkx as nx
import matplotlib.pyplot as plt


# Создание пустого графа
graf = nx.Graph()

# Добавление вершин
graf.add_node('A')
graf.add_nodes_from(["B", "C", "D"])
graf.add_node('E')
graf.add_node('F')

# Добавление рёбер
graf.add_edge("A", "B")
graf.add_edges_from([("B", "C"), ("C", "D"), ("D", "A")])
graf.add_edge("D", "E")
graf.add_edges_from([("E", "F"), ("F", "A")])


# Получение списка вершин и рёбер
nodes = graf.nodes()
edges = graf.edges()

# Визуализация графа
nx.draw(graf, with_labels=True, node_color='lightblue', edge_color='gray')
plt.show()


"""Библиотека igraph не работает, просит установить pycairo or cairocffi
   построение графика недоступно"""

# import igraph as ig
#
# # Создание пустого графа
# graf_ig = ig.Graph()
#
# # Добавление вершин
# graf_ig.add_vertices(4)
#
# # Добавление рёбер
# graf_ig.add_edges([(0, 1), (1, 2), (2, 3), (3, 0)])
#
# # Получение списка вершин и рёбер
# nodes_ig = graf_ig.vs
# edges_ig = graf_ig.es
#
# # Визуализация графа
# layout = graf_ig.layout('circle')
# ig.plot(graf_ig, layout=layout, vertex_color='lightblue', edge_color='gray')
