import time
from entities.feirante import Feirante
from services.terminal import Terminal

class Admin:
    def __init__(self, n, e, p):
        self.name = n
        self.email = e
        self.password = p

    def viewAllFeirantes(self, users):
        Terminal().clearTerminal()
        n = 0
        for user in users[1]:
            print("ID: {}\nNome: {}\nEmail: {}\n".format(n, user.name, user.email))
            n = n + 1
        
        input("\nInsira qualquer tecla para voltar ao menu...")
        self.showDefaultAdminMenu(users)

    def addFeirante(self, users):
        Terminal().clearTerminal()
        name = input("Digite o nome do feirante: ")
        email = input("Digite o email do feirante: ")
        password = input("Digite a senha do feirante: ")
        
        feirante = Feirante(name, email, password)
        users[1].append(feirante)

        self.showDefaultAdminMenu(users)
    
    def validateAdminSelectedOption(self, option, users):
        if option == "1":
            self.addFeirante(users)
        elif option == "2":
            self.viewAllFeirantes(users)
        elif option == "3":
            # viewFeirantesResume()
            print("ver resultados")
        # elif option == "4":
        #   resolver isso dps
        else:
            print("Houve um erro ao digitar a opção, tente novamente!")
            time.sleep(1.5)
            self.showDefaultAdminMenu()

    def showDefaultAdminMenu(self, users):
        Terminal().clearTerminal()
        print("Selecione o que deseja realizar:")
        option = input("1 - Cadastrar novo feirante\n2 - Visualizar todos os feirantes\n3 - Visualizar resultados por feirante\n4 - Voltar ao menu inicial")
        self.validateAdminSelectedOption(option, users)
    
    def login(self, users):
        Terminal().clearTerminal()
        for user in users[0]:
            if self.email == user.email and self.password == user.password:
                print("Usuário logado com sucesso!\nRedirecionando...")
                time.sleep(1.5)
                self.showDefaultAdminMenu(users)
            else:
                print("credenciais incorretas")