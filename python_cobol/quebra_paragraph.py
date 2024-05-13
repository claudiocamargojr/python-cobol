import re

class QuebraParagraph:
    def __init__(self, file_path, encoding='ISO-8859-1'):
        self.file_path = file_path
        self.encoding = encoding
        self.content = self.read_file()

    def read_file(self):
        with open(self.file_path, 'r', encoding=self.encoding) as file:
            return file.read()

    def find_specific_paragraphs(self, start_paragraph):
        dict_paragraphs_text = {}
        paragraphs = []
        lines = self.content.split('\n')
        current_paragraph = None
        current_text = None
        collect = False
        count = 0

        for line in lines:
            if re.match(r'^ {6}\*', line):  # Ignora linhas de comentários
                continue
            
            paragraph_name = re.match(r'^.{7}([A-Z0-9\-]+)\.', line)
            if paragraph_name:
                paragraph_name = paragraph_name.group(1).strip()
                if paragraph_name == start_paragraph:
                    collect = True  # Começa a coletar a partir deste parágrafo
                if collect:
                    if current_paragraph:
                        dict_paragraphs_text[current_paragraph] = current_text
                   
                    current_paragraph = paragraph_name  # Atualiza o parágrafo atual
                    current_text = ""  # Inicia um novo bloco de texto
                    paragraphs.append(paragraph_name)
            elif current_paragraph and collect:
                if line.strip():  # Atualiza com a última linha válida não vazia
                    current_text = line

        # Salva o último parágrafo processado, se ainda não alcançou o limite
        if current_paragraph and collect:
            dict_paragraphs_text[current_paragraph] = current_text

        return dict_paragraphs_text

    def print_paragraphs_info(self, paragraphs_info):
        print("Aqui estão os parágrafos e suas últimas linhas de texto antes de começar o próximo:")
        for paragraph, text in paragraphs_info.items():
            print(f"Parágrafo: {paragraph}")
            print(f"Texto final do parágrafo: '{text}'\n")  # Adiciona uma linha em branco para melhor separação visual

