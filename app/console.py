import os, time

from core.admin import Admin
from core.marketer import Marketer
from core.client import Client

from repo.adminRepository import AdminRepository

class Console:

    def handleUserResponse(self, option):
        if option == "1":
            Admin(Console(), AdminRepository()).showMenu()
        elif option == "2":
            Marketer(Console()).showMenu()
        elif option == "3":
            Client(Console()).showMenu()
        else:
            self.clearConsole()
            print("Houve um erro de digitação, tente novamente!")
            time.sleep(1.5)
            self.showMenu()

    def askForUserResponse(self, text):
        response = input(text)
        return response

    def clearConsole(self):
        os.system("cls||clear")

    def showMenu(self):
        self.clearConsole()
        print("-------- MENU PRINCIPAL --------\n")
        print("Seja muito bem-vindo!")
        print("Como você deseja entrar no sistema?\n")
        print("1 - Como administrador...")
        print("2 - Como feirante...")
        print("3 - Como cliente...")

        option = self.askForUserResponse("")
        self.handleUserResponse(option)

    def start(self):
        self.showMenu()