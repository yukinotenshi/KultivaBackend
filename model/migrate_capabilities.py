from model.base_model import *
from playhouse.migrate import *
import peewee as pw

db.connect()
db.drop_tables([Capabilities])
db.create_tables([Capabilities])
migrator = SqliteMigrator(db)
status = pw.IntegerField(default=0)
migrate(
    migrator.add_column("order_line", 'status', status)
)
db.close()
