import peewee as pw
from datetime import datetime
import os
from util import generate_random_string

curdir = os.path.dirname(os.path.abspath(__file__))

db = pw.SqliteDatabase(os.path.join(curdir, "kultiva.db"))

class BaseModel(pw.Model):
    updatedAt = pw.DateTimeField(default=datetime.now)
    createdAt = pw.DateTimeField(default=datetime.now)

    def save(self, *args, **kwargs):
        self.updatedAt = datetime.now()
        return super(BaseModel, self).save(*args, **kwargs)

    class Meta:
        database = db


class User(BaseModel):
    first_name = pw.CharField()
    last_name = pw.CharField(default="")
    password = pw.CharField()
    profile_pic = pw.CharField(default="")
    public_key = pw.CharField(default="")

    class Meta:
        db_table = "user"


class Session(BaseModel):
    user = pw.ForeignKeyField(User, related_name="session")
    session_id = pw.CharField(default=generate_random_string)

    class Meta:
        db_table = "session"


class Petani(BaseModel):
    user = pw.ForeignKeyField(User, related_name="petani")
    phone = pw.CharField()
    lat = pw.FloatField()
    lng = pw.FloatField()

    class Meta:
        db_table = "petani"


class Customer(BaseModel):
    user = pw.ForeignKeyField(User, related_name="customer")
    email = pw.CharField()

    class Meta:
        db_table = "customer"


class Category(BaseModel):
    name = pw.CharField()

    class Meta:
        db_table = "category"


class Product(BaseModel):
    category = pw.ForeignKeyField(Category, related_name="product")
    name = pw.CharField()
    harga = pw.IntegerField()
    unit = pw.CharField()

    class Meta:
        db_table = "product"


class Order(BaseModel):
    customer = pw.ForeignKeyField(Customer, related_name="order")
    address = pw.CharField()
    product = pw.ForeignKeyField(Product, related_name="order")
    total_qty = pw.FloatField()

    class Meta:
        db_table = "order"


class Supplier(BaseModel):
    order = pw.ForeignKeyField(Order, related_name="supplier")
    petani = pw.ForeignKeyField(Petani, related_name="supplier")
    qty = pw.FloatField()

    class Meta:
        db_table = "supplier"


class Capabilities(BaseModel):
    petani = pw.ForeignKeyField(Petani, related_name="capabilities")
    product = pw.ForeignKeyField(Product, related_name="capabilities")
    volume = pw.FloatField()
    start_date = pw.DateField()
    end_date = pw.DateField()

    class Meta:
        db_table = "capabilities"


class ChatRoom(BaseModel):
    petani = pw.ForeignKeyField(Petani, related_name="chat_room")
    customer = pw.ForeignKeyField(Customer, related_name="chat_room")

    class Meta:
        db_table = "chat_room"


class Chat(BaseModel):
    uid = pw.CharField(default=generate_random_string)
    chat_room = pw.ForeignKeyField(ChatRoom, related_name="chats")
    from_user = pw.ForeignKeyField(User, related_name="chats")
    to_user = pw.ForeignKeyField(User, related_name="chats")

    class Meta:
        db_table = "chat"
