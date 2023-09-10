import networkx as nx
import matplotlib.pyplot as plt

# Crear un nuevo gráfico
G = nx.Graph()

# Agregar nodos y transiciones
G.add_node('q0')
G.add_node('q1')
G.add_edge('q0', 'q1', label='a')
G.add_edge('q0', 'q0', label='b')
G.add_edge('q0', 'q0', label='c')
G.add_edge('q1', 'q1', label='b')
G.add_edge('q1', 'q1', label='c')

# Guardar el gráfico en un archivo
nx.draw(G, with_labels=True, labels=nx.get_edge_attributes(G, 'label'), node_shape='s', font_size=10, font_weight='bold')
plt.savefig('automaton.png', format='png')

# Mostrar el gráfico
plt.show()
