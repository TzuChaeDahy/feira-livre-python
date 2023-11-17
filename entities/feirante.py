import time

class Feirante:
    
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def login(self, users):
        for user in users[1]:
            if self.email == user.email and self.password == user.password:
                print("Usuário logado com sucesso!\nRedirecionando...")
                time.sleep(1.5)
                # redirecionar usuário para menu padrão de feirante
            else:
                print("credenciais incorretas")