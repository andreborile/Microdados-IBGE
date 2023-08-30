class Variavel:

    def __init__ (self, posicao_inicial, tamanho, codigo, descricao):
        self.posicao_inicial = int(posicao_inicial) - 1
        self.tamanho = tamanho
        self.codigo = codigo
        self.descricao = descricao
        self.categoria = {}

    def add_categoria(self, categoria):
        self.categoria[categoria.get('categoria_tipo')] = categoria.get('categoria_descricao_tipo')


    def __str__(self):
        return f'{self.codigo} - {self.descricao}'