from db.product import products
import time
from db.marketer import marketers

class Client:
    def __init__(self, console):
        self.console = console
    
    def showMenu(self):
        print("-------- Menu --------\n")
        for marketerEmail in products:
            print(marketerEmail.split('@')[0])
            if len(products[marketerEmail]) <= 0:
                print("Sem Estoque...")
            else:
                for productsArray  in products[marketerEmail]:
                        print("{} - R${}".format(productsArray.nomeDoProduto, productsArray.valorDoProduto))    
            print("")
        self.console.askForUserResponse("")       
        self.console.showMenu()           