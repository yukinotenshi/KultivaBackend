from model.base_model import *

db.connect()
db.drop_tables([Supplier, Order])
db.create_tables([Order, OrderLine, Supplier])

db.close()
