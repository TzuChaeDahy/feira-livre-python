class ClassProducts:
    def __init__(self, console):
        self.console = console
        self.nomeDoProduto = ""
        self.vendidos = 0
        self.quantidadeDoProduto = int(0)
        self.valorDoProduto = 0
        self.totalFaturado = 0
        
    def setProducts(self, nomeDoProduto, valorDoProduto, quatidadeDoProduto):
        self.nomeDoProduto = nomeDoProduto
        self.valorDoProduto = valorDoProduto
        self.quantidadeDoProduto = quatidadeDoProduto 
        
        return self
        
    def sellProducts(self, valorDoProduto, quantidadeDoProduto):
        self.valorDoProduto = valorDoProduto
        self.quantidadeDoProduto = quantidadeDoProduto
        
        return self
        
    def getName(self):
        return self.nomeDoProduto