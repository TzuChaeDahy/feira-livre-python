from entities.admin import Admin
from entities.feirante import Feirante
from infra.users import users
import time
from services.terminal import Terminal

class Main:

    def startApplication(self):
        self.showInitialMenu()

    def showInitialMenu(self):
        Terminal().clearTerminal()
        print("Olá! Seja bem-vindo à feira!\nComo deseja acessar o sistema?")
        option = input("1 - Admin\n2 - Feirante\n3 - Cliente\n")
        self.validateSelectedUserOption(option)

    def askCredentials(self):
        email = input("Digite o seu email: ")
        password = input("Digite a sua senha: ")

        return email, password

    def validateSelectedUserOption(self, option):
        Terminal().clearTerminal()
        if option == "1":
            email, password = self.askCredentials()
            adm = Admin("", email, password)
            adm.login(users)
        elif option == "2":
            email, password = self.askCredentials()
            feirante = Feirante(email, password)
            feirante.login(users)
        elif option == "3":
            print("Redirecionando...")
            time.sleep(1.5)
        else:
            print("Houve um erro ao digitar a opção, tente novamente!")
            time.sleep(1.5)
            self.showInitialMenu()


Main().startApplication()