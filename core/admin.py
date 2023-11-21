import time

from db.admin import admins

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
            print("cadastro")
        elif option == "2":
            print("resultados")
        elif option == "3":
            self.console.showMenu()

    def signUp(self):
        self.console.clearConsole()
        print("-------- Cadastro de administrador --------\n")
        name = self.console.askForUserResponse("Digite o seu nome: ")
        email = self.console.askForUserResponse("Digite o seu email: ")
        password = self.console.askForUserResponse("Digite a sua senha: ")

        admin = Admin(self.console).setCredentials(email, password).setName(name)
        self.setName(name)
        self.setCredentials(email, password)

        admins.append(admin)

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
                print("Usuário logado com sucesso!")
                print("Redirecionando...")
                time.sleep(1.5)
                authorized = True
                break

        if not authorized:
            print("Credenciais incorretas, tente novamente!")
            time.sleep(3)
            self.console.showMenu()

    def showMenu(self):
        if len(admins) <= 0:
            self.console.clearConsole()
            print("Não há nenhum administrador cadastrado, por favor realize o cadastro a seguir:")
            time.sleep(1.5)
            self.signUp()
        else: 
            self.login()

        self.console.clearConsole()
        print("-------- Administrador | {} --------\n".format(self.name.capitalize()))
        print("O que deseja fazer?")
        print("1 - Cadastrar novo feirante")
        print("2 - Visualizar resultados por feirante")
        print("3 - Voltar ao menu inicial")
        option = self.console.askForUserResponse("")
        self.handleUserResponse(option)