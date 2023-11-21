from db.admin import admins

class AdminRepository:

    def __init__(self):
        self.db = admins

    def getAll(self):
        for admin in self.db:
            print("ola")