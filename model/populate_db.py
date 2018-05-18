from model.base_model import *
from datetime import date, timedelta
from model.user_model import register_petani
db.connect()
'''c = Category.get(
   Category.name == "Sayur"
)
c.save()

p = Product(
    category = c,
    name = "Kangkung",
    harga = 5000,
    unit = "kg"
)
p.save()'''

#petani = Petani.get(Petani.id == 1)
petani = register_petani(
    first_name= "petani2",
    last_name =  "",
    phone = "+6283815133899",
    password = "secret",
    lat = 0.0,
    lng = 0.0
)
petani.save()

product = Product.get(Product.id == 1)
c = Capabilities(
    product = product,
    petani = petani,
    volume = 2,
    start_date = date.today() - timedelta(days=1),
    end_date = date.today() + timedelta(days=3)
)
c.save()

db.close()
