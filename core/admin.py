import time

class Admin:
    def __init__(self, console, repository):
        self.console = console
        self.repository = repository
        self.email = ""
        self.password = ""
    
    def setCredentials(self, email, password):
        self.email = email
        self.password = password

    def login(self):
        self.console.clearConsole()

        email = self.console.askForUserResponse("Insira seu email: ")
        if email == "sair":
            self.console.showMenu()
            return

        password = self.console.askForUserResponse("Insira seu senha: ")
        if  password == "sair":
           self.console.showMenu()
           return

        self.console.clearConsole()
        if self.email == email and self.email != "" and self.password == password and self.password != "":
            print("Usuário logado com sucesso!")
            print("Redirecionando...")
            time.sleep(1.5)
        else:
            print("Credenciais incorretas, insira as novamente!")
            print("Caso deseja voltar para a tela inicial, escreva 'sair'")
            time.sleep(3)
            self.showMenu()

    def showMenu(self):
        self.login()

        print("-------- Menu | Administrador --------")