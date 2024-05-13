import networkx as nx
import matplotlib.pyplot as plt
class Graph_relationship:

    def create_graph(goto_results):
        """Cria um grafo dirigido a partir dos resultados de GO TO."""
        G = nx.DiGraph()
        for source, target in goto_results.items():
            G.add_edge(source, target)
        return G

    def plot_graph(G):
        """Visualiza o grafo usando Matplotlib."""
        pos = nx.spring_layout(G, seed=42)  # Fixa a disposição para consistência
        nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=2000, edge_color='k', linewidths=1, font_size=12)
        plt.show()