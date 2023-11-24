from core.products import ClassProducts
from app.console import Console
from db.product import products

def seed_products():
    productOne = ClassProducts(Console()).setProducts("banana", 10, 5.50)
    productTwo = ClassProducts(Console()).setProducts("pêra", 15, 3.60)

    products["levid@feirante.com"].append(productOne)
    products["levid@feirante.com"].append(productTwo)