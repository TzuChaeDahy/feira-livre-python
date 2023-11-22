import time 
from db.marketer import marketers
from db.product import products
from core.products import ClassProducts

class Marketer:
    def __init__(self, console):
        self.console = console
        self.name = ""
        self.email = ""
        self.password = ""
        self.revenue = 0

    def setCredentials(self, email, password):
        self.email = email
        self.password = password 
        
        return self
    
    def setName(self, name):
        self.name = name
        
        return self
    
    def showRegisterProductMenu(self): 
        self.console.clearConsole()
        print("------- Registrar novo produto --------\n")
        ClassProducts.nomeDoProduto = self.console.askForUserResponse("Digite o nome do Produto: ")
        ClassProducts.valorDoProduto = self.console.askForUserResponse("Digite o valor do produto: ")
        ClassProducts.quantidadeDoProduto = self.console.askForUserResponse("Digite a quantidade do produto: ")
        
        products.append(ClassProducts(self.console).setProducts(nomeDoProduto, valorDoProduto, quatidadeDoProduto))
        self.console.clearConsole()
        print("Registrando Produto...")
        time.sleep(1.5)
        
        self.showMenu()
    
    def handleUserResponse(self, option): 
        if option == "1":
           print("1")
        elif option == "2" :
            self.showRegisterProductMenu()
            

    def login(self):
       self.console.clearConsole()
       print("-------- Login de Marketer --------\n")
       email = self.console.askForUserResponse("Digite seu email: ")
       password = self.console.askForUserResponse("Insira seu senha: ")
       
       self.console.clearConsole()
       
       authorized = False
       for marketer in marketers:
        if marketer.email == email and marketer.email != "" and marketer.password == password and marketer.password != "":
            self.setName(marketer.name)
            self.setCredentials(email, password)
            
            print("Usuário logado com sucesso!")
            print("Redirecionando...")
            time.sleep(1.5)
            authorized = True
            break
        if not authorized:
            print("Credenciais incorretas, tente novamente!")
            time.sleep(3)
            self.console.showMenu()
            
        return self
    
    def showMenu(self):
        if len(marketers) <= 0:
            self.console.clearConsole()
            print("Não há nenhum marketer cadastrado, por favor realize o cadastro a seguir:")
            time.sleep(1.5)
            self.showRegisterProductMenu()
        elif self.name == "" or self.password == "":
            self.login()
        
        
        self.console.clearConsole()
        print("-------- MARKETER | {} --------\n".format(self.name.capitalize()))
        print("Seja muito bem-vindo!")
        print("Total faturado: {}".format(self.revenue))
        print("escolha uma das opções a baixo:")
        print("1 - Cadastrar Produto")
        print("2 - Registrar Vendas")
        option = self.console.askForUserResponse("")
        self.handleUserResponse(option)
       

    
            