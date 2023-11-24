from core.marketer import Marketer
from app.console import Console
from db.marketer import marketers

def seed_marketer():
    marketer = Marketer(Console()).setCredentials("levid@feirante.com", "12345").setName("levid")

    marketers.append(marketer)
