class ClassProducts:
    def __init__(self, console):
        self.console = console
        self.nomeDoProduto = ""
        self.maiorQuantidade = 0
        self.quantidadeDoProduto = 0
        self.valorDoProduto = 0
        self.totalFaturado = 0
        
    def setProducts(self, nomeDoProduto, quatidadeDoProduto, valorDoProduto):
        self.nomeDoProduto = nomeDoProduto
        self.valorDoProduto = valorDoProduto
        self.quantidadeDoProduto = quatidadeDoProduto 
        
        
