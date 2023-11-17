import time

class Admin:
    def __init__(self, e, p):
        self.email = e
        self.password = p
    
    def login(self, users):
        for user in users[0]:
            if self.email == user.email and self.password == user.password:
                print("Usuário logado com sucesso!\nRedirecionando...")
                time.sleep(1.5)
                # redirecionar usuário para menu padrão de ADM
            else:
                print("credenciais incorretas")