from quebra_paragraph import QuebraParagraph
from cobolAnalyzer import CobolAnalyzer
from graphDataBase import GraphDataBase
from graphrelationship import Graph_relationship

class Orchestrator:
    def __init__(self, file_path, json_output_path):
        self.file_path = file_path
        self.json_output_path = json_output_path
        self.extractor = QuebraParagraph(file_path)
        self.analyzer = CobolAnalyzer(file_path)
        self.graph_db = GraphDataBase()

    def execute(self):
        # Extração e processamento de parágrafos específicos
        specific_paragraphs = self.extractor.find_specific_paragraphs("010-INICIO-PROGRAMA")
        self.extractor.print_paragraphs_info(specific_paragraphs)

        # Análise de 'GO TO' no arquivo COBOL
        self.analyzer.parse_file()
        goto_results = self.analyzer.analyze_goto()

        # Criação, visualização do grafo e exportação para json
        G = self.graph_db.create_graph(goto_results)
        self.graph_db.plot_graph(G)
        self.graph_db.print_graph_data(goto_results)
        self.graph_db.export_graph_to_json(goto_results, self.json_output_path)

# Uso da classe Orchestrator
if __name__ == '__main__':
    file_path = "C:/devalci/S0347-FTE-411-01_anterior.cob"  # Substitua pelo caminho correto do arquivo
    json_output_path = "C:/devalci/relationships.json"        # Substitua pelo caminho do arquivo json de saída
    orchestrator = Orchestrator(file_path, json_output_path)
    orchestrator.execute()
