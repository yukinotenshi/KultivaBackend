from model.base_model import *

db.connect()
c = Category.get(
   Category.name == "Sayur"
)
c.save()

p = Product(
    category = c,
    name = "Kangkung",
    harga = 5000,
    unit = "kg"
)
p.save()

db.close()
