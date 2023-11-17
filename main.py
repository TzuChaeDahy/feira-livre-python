from entities.admin import Admin
from entities.feirante import Feirante
from infra.users import users
import os, time

def startApplication():
    showInitialMenu()

def clearTerminal():
    os.system('cls||clear')

def showInitialMenu():
    clearTerminal()
    print("Olá! Seja bem-vindo à feira!\nComo deseja acessar o sistema?")
    option = int(input("1 - Admin\n2 - Feirante\n3 - Cliente\n"))
    validateSelectedUserOption(option)

def askCredentials():
    email = input("Digite o seu email: ")
    password = input("Digite a sua senha: ")

    return email, password
    
def validateSelectedUserOption(option):
    clearTerminal()
    if option == 1:
        email, password = askCredentials()
        adm = Admin(email, password)
        adm.login(users)
    elif option == 2:
        email, password = askCredentials()
        feirante = Feirante(email, password)
        feirante.login(users)
    elif option == 3:
        print("Redirecionando...")
        time.sleep(1.5)
    else:
        print("Houve um erro ao digitar a opção, tente novamente!")
        time.sleep(1.5)
        showInitialMenu()

startApplication()