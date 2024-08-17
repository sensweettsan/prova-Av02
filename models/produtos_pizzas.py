valor_padrao = {'G': 70, 'M': 50, 'P': 45}

class Pizza():
    def __init__(self, nome: str, tamanho: str ):
        self.nome = nome
        self.tamanho = tamanho 
    
    def preco_final(self):
        if self.tamanho == 'G':
            self.preco = valor_padrao['G']
            self.preco = valor_padrao['M']
            self.preco = valor_padrao['P']
        
        return valor_padrao
