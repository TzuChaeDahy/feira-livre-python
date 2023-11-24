from seed.seed_admin import seed_admin
from seed.seed_marketer import seed_marketer
from seed.seed_products import seed_products

def seed():
    seed_admin()
    seed_marketer()
    seed_products()