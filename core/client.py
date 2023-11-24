from db.product import products
import time
from db.marketer import marketers

class Client:
    def _init_(self, console):
        self.console = console
    
    def showMenu(self):
        print("-------- Menu --------\n")
        print("Selecione o feirante: ")
        i = 1
        if len(products) <= 0:
            print('Não há feirantes cadastrados...\n')
            print("Pressione Enter para voltar ao menu inicial...")
            self.console.askForUserResponse("")
            self.console.showMenu()
            
        else:
            for marketer in marketers:
                print('{} - {}'.format(i, marketer.name))
                i += 1  
                self.console.askForUserResponse("")
                self.console.showMenu()