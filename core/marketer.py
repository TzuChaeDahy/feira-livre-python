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
        nomeDoProduto = self.console.askForUserResponse("Digite o nome do Produto: ")
        valorDoProduto = self.console.askForUserResponse("Digite o valor do produto em reais: ")
        quantidadeDoProduto = self.console.askForUserResponse("Digite a quantidade do produto: ")
        
            
        products[self.email].append(ClassProducts(self.console).setProducts(nomeDoProduto, int(valorDoProduto), int(quantidadeDoProduto)))
        self.console.clearConsole()
        print("Registrando Produto...")
        time.sleep(1.5)
    
        self.showMenu()
                
        return self
        
    def showRegisterSellMenu(self):
        self.console.clearConsole()
        print("------- Registrar venda --------\n")
        print("Selecione o produto que foi vendido:\n")
        
        i = 1
        if len(products[self.email]) <= 0:
            print('Não há produtos cadastrados...')
            time.sleep(1.5)
            self.showMenu()
        else:
            for product in products[self.email]:
                print('{} - {}'.format(i, product.nomeDoProduto))
                i += 1    
        
        option = int(self.console.askForUserResponse(""))
        x = 0
        self.revenue = 0
        encontrado = False
        for n in products[self.email]:
            x = x + 1
            if option == x:
                quantidade = int(self.console.askForUserResponse("Digite a quantidade do produto: "))
                if int(n.quantidadeDoProduto) < quantidade:
                    print("Quantidade do produto indisponível...")
                else:
                    n.vendidos += quantidade
                    n.quantidadeDoProduto -= quantidade
                    n.totalFaturado = n.vendidos * n.valorDoProduto
                    self.console.clearConsole()
                    print("Venda cadastrada com sucesso!")
                    encontrado = True
                    time.sleep(1.5)

        if not encontrado:
            print(x)
            print("Selecione uma opção válida...")
            time.sleep(1.5)
            self.showMenu()
        
        self.console.clearConsole()
        self.showMenu()
    
    def setRevenue(self, faturamentoDoProduto):
        self.revenue = self.revenue + faturamentoDoProduto
        
        return self
        
    def calculateTotalRevenue(self): 
        for product in products[self.email]:
            self.setRevenue(product.totalFaturado)
                
        return self
    
    def showStock(self):
        self.console.clearConsole()
        print("------- Estoque --------\n")
        if len(products[self.email]) <= 0:
            print('Não há produtos cadastrados...')
            time.sleep(1.5)
            self.showMenu()
        else:
            for product in products[self.email]:
                print("{} {} UN R${}".format(product.nomeDoProduto, product.quantidadeDoProduto, product.valorDoProduto))   
        print("Digite qualquer tecla para sair do estoque: ")
        self.console.askForUserResponse("")
        self.showMenu()
        
    def handleUserResponse(self, option): 
        if option == "1":
           self.showRegisterProductMenu()
        elif option == "2" :
            self.showRegisterSellMenu()
        elif option == "3":
            self.showStock()     
        elif option == "4":
            self.console.showMenu()
        else:
            print("Houve um erro de digitação, tente novamente")   
            time.sleep(1.5)
            self.showMenu()
    
    def setOldRevenue(self, oldRevenue):
        self.revenue = oldRevenue
        return self
            
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
            self.setOldRevenue(marketer.revenue)
                                
            print("Usuário logado com sucesso!")
            print("Redirecionando...")
            time.sleep(1.5)
            authorized = True
            break
       
       if not authorized:
        print("Credenciais incorretas, tente novamente!")
        time.sleep(1.5)
        self.console.showMenu()
            
       return self
    
    def showMenu(self):
        if self.email == "" or self.password == "":
            self.login()
            
        self.calculateTotalRevenue()
        
        self.console.clearConsole()
        print("-------- MARKETER | {} --------\n".format(self.name.capitalize()))
        print("Seja muito bem-vindo!")
        print("Total faturado: R$ {}".format(self.revenue))
        print("escolha uma das opções a baixo:")
        print("1 - Cadastrar Produto")
        print("2 - Registrar Vendas")
        print("3 - Mostrar estoque")
        print("4 - Voltar ao menu inicial")
        option = self.console.askForUserResponse("")
        self.handleUserResponse(option)