from models.produtos_pizzas import Pizza

class Pizza_especiai(Pizza):
    def __init__(self, nome: str, tamanho: str, preco: float, ingredientes: float):
        super().__init__(nome, tamanho, preco)
        self.ingredientes = ingredientes
    
   