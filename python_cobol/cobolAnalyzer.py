import re

class CobolAnalyzer:
    def __init__(self, file_path):
        self.file_path = file_path
        self.paragraphs = {}
        self.goto_regex = re.compile(r'GO TO\s+(\d{3}-[\w-]+)')

    def parse_file(self):
        """Lê e analisa o arquivo COBOL para extrair parágrafos e seus conteúdos."""
        paragraph_start_regex = re.compile(r'^\d{6}\s+(\d{3}-[\w-]+)')
        try:
            with open(self.file_path, 'r', encoding='latin1') as file:
                current_paragraph = None
                content = []

                for line in file:
                    start_match = paragraph_start_regex.match(line)
                    if start_match:
                        # Finaliza o parágrafo anterior e começa um novo
                        if current_paragraph:
                            self.paragraphs[current_paragraph] = '\n'.join(content)
                        current_paragraph = start_match.group(1)
                        content = [line]
                    else:
                        content.append(line)

                # Não esqueça de adicionar o último parágrafo encontrado ao dicionário
                if current_paragraph:
                    self.paragraphs[current_paragraph] = '\n'.join(content)

        except FileNotFoundError:
            print(f"Erro: O arquivo {self.file_path} não foi encontrado.")
        except Exception as e:
            print(f"Erro ao ler o arquivo: {e}")

    def analyze_goto(self):
        """Analisa os parágrafos para encontrar referências 'GO TO' e seus destinos."""
        results = {}
        for name, data in self.paragraphs.items():
            goto_match = self.goto_regex.search(data)
            if goto_match:
                results[name] = goto_match.group(1)
        return results
