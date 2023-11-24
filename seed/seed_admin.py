from core.admin import Admin
from app.console import Console
from db.admin import admins

def seed_admin():
    admin = Admin(Console()).setCredentials("marcos@admin.com", "12345").setName("marcos")

    admins.append(admin)