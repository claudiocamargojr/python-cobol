import networkx as nx
import json

class GraphDataBase:
    def create_graph(self, goto_results):
        """Cria um grafo dirigido a partir dos resultados de GO TO."""
        G = nx.DiGraph()
        for source, target in goto_results.items():
            G.add_edge(source, target)
        return G

    def plot_graph(self, G):
        """Visualiza o grafo usando Matplotlib."""
        import matplotlib.pyplot as plt
        nx.draw(G, with_labels=True)
        plt.show()

    def print_graph_data(self, goto_results):
        """Imprime dados do grafo para verificação."""
        for source, target in goto_results.items():
            print(f"{source} -> {target}")

    def export_graph_to_json(self, goto_results, file_path):
        """Exporta os resultados do grafo para um arquivo JSON."""
        graph_data = []
        for source, target in goto_results.items():
            graph_data.append({"source": source, "target": target})

        try:
            with open(file_path, 'w', encoding='utf-8') as file:
                json.dump(graph_data, file, indent=4)
        except IOError as e:
            print(f"Não foi possível escrever no arquivo {file_path}: {e}")

