import time 
from db.admin import admins

class Marketer:
    def __init__(self, console):
        self.console = console
        self.name = ""
        self.email = ""
        self.password = ""
        self.revenue = 0
        self.nomeDoProduto = ""
        self.valorDoProduto = 0
        self.quantidadeDoProduto = 0
    
    def showMenu(self):
        print("-------- MARKETER MENU --------\n")
        print("Seja muito bem-vindo!")
        print("Total faturado: {}".format(self.revenue))
        print("escolha uma das opções a baixo:")
        print("1 - Cadastrar Produto")
        print("2 - Registrar Vendas")
        
        option = self.console.askForUserResponse("")
        self.handleUserResponse(option)
        
    def showRegisterProductMenu(self): 
        nomeDoProduto = self.console.askForUserResponse("Digite o nome do Produto: ")
        valorDoProduto = self.console.askForUserResponse("Digite o valor do produto: ")
        quantidadeDoProduto = self.console.askForUserResponse("Digite a quantidade do produto: ")

    def setCredentials(self, email, password):
        self.email = email
        self.password = password 
        
        return self
    
    def setName(self, name):
        self.name = name
        
        return self
    
    def handleUserResponse(self, option): 
        if option == "1":
           print("1")
        elif option == "2" :
            self.showRegisterProductMenu()
            

    def login(self):
        # self.console.clearConsole()

        # email = self.console.askForUserResponse("Insira seu Email: ")
        # password = self.console.askForUserResponse("Insira sua senha: ")
        # self.console.clearConsole()

        # db = admins

        # for admin in db: 
        #     if admin.email == email and admin.email != "" and admin.password == password and admin.password != "":
        #         print("Usuário logado com sucesso!")
        #         print("Redirecionando...")
        #         time.sleep(1.5)
        #         return
        # print("Credenciais incorretas, tente novamente!")
        # time.sleep(3)
        self.showMenu()
    
            