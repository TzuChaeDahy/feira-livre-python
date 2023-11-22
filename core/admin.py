import time

from db.admin import admins
from db.marketer import marketers
from db.product import products

from core.marketer import Marketer
from core.products import ClassProducts

class Admin:
    def __init__(self, console):
        self.console = console
        self.email = ""
        self.password = ""
        self.name = ""
    
    def setCredentials(self, email, password):
        self.email = email
        self.password = password

        return self

    def setName(self, name):
        self.name = name
        
        return self

    def handleUserResponse(self, option):
        if option == "1":
            self.showRegisterMarketerMenu()
        elif option == "2":
            self.viewAllMarketers()
        elif option == "3":
            self.viewMarketersResults()
        elif option == "4":
            self.console.showMenu()
        else:
            self.console.clearConsole()
            print("Houve um erro de digitação, tente novamente!")
            time.sleep(1.5)
            self.showMenu()

    def viewMarketersResults(self):
        self.console.clearConsole()
        email = self.console.askForUserResponse("Digite o email do feirante que deseja busca: ")

        if email in products:
            p = products[email]

            self.console.clearConsole()
            contador = 0
            for n in p:
                print("ID do produto: {}".format(contador))
                print("Preço: {}".format(n.valorDoProduto))
                print("Quantidade vendida: {}".format(n.vendidos))
                print("Faturamento: {}".format(n.totalFaturado))
                
            self.console.askForUserResponse("Aperte qualquer tecla para sair...")
        else:
            self.console.clearConsole()
            print("Não existe feirante com esse email...")
            self.showMenu()
        
        self.showMenu()

    def viewAllMarketers(self):
        id = 0
        if len(marketers) <= 0:
            self.console.clearConsole()
            print("Não há feirantes cadastrados...")
            time.sleep(1.5)
            self.showMenu()
        else:
            self.console.clearConsole()
            for marketer in marketers:
                print("ID: {}".format(id))
                print("Nome: {}".format(marketer.name))
                print("Email: {}".format(marketer.email))
                print("Faturamento: R$ {}\n".format(marketer.revenue))

            print("Aperte qualquer tecla para sair...")
            self.console.askForUserResponse("")

            self.showMenu()

    def showRegisterMarketerMenu(self):
        self.console.clearConsole()
        print("------- Registrar novo feirante --------\n")
        name = self.console.askForUserResponse("Digite o nome do feirante: ")
        email = self.console.askForUserResponse("Digite o email do feirante: ")
        password = self.console.askForUserResponse("Digite a senha do feirante: ")

        marketers.append(Marketer(self.console).setCredentials(email, password).setName(name))
        self.console.clearConsole()
        print("Registrando feirante...")
        time.sleep(1.5)

        self.showMenu()

    def signUp(self):
        self.console.clearConsole()
        print("-------- Cadastro de administrador --------\n")
        name = self.console.askForUserResponse("Digite o seu nome: ")
        email = self.console.askForUserResponse("Digite o seu email: ")
        password = self.console.askForUserResponse("Digite a sua senha: ")

        self.setName(name)
        self.setCredentials(email, password)

        admin = Admin(self.console).setCredentials(email, password).setName(name)
        admins.append(admin)

        self.console.clearConsole()
        print("Registrando novo administrador...")
        time.sleep(1.5)

        return self

    def login(self):
        self.console.clearConsole()
        print("-------- Login de administrador --------\n")
        email = self.console.askForUserResponse("Digite seu email: ")
        password = self.console.askForUserResponse("Insira seu senha: ")

        self.console.clearConsole()

        authorized = False
        for admin in admins:
            if admin.email == email and admin.email != "" and admin.password == password and admin.password != "":
                self.setName(admin.name)
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
        if len(admins) <= 0:
            self.console.clearConsole()
            print("Não há nenhum administrador cadastrado, por favor realize o cadastro a seguir:")
            time.sleep(1.5)
            self.signUp()
        elif self.name == "" or self.password == "": 
            self.login()

        self.console.clearConsole()
        print("-------- Administrador | {} --------\n".format(self.name.capitalize()))
        print("O que deseja fazer?\n")
        print("1 - Cadastrar novo feirante")
        print("2 - Visualizar todos os feirantes")
        print("3 - Visualizar resultados por feirante")
        print("4 - Voltar ao menu inicial")
        option = self.console.askForUserResponse("")
        self.handleUserResponse(option)