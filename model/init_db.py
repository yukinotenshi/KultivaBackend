from model.base_model import *

db.connect()
db.create_tables([
    User, Session,
    Petani, Customer,
    Capabilities, Product,
    Order, OrderLine, Supplier,
    ChatRoom, Chat, Category
])

db.close()
