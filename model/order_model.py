from model.base_model import Order, OrderLine, Supplier, Customer, User, Product, Capabilities
from datetime import date, timedelta
from operator import itemgetter

def distance(lat1, lng1, lat2, lng2):
    x = lat1 - lat2
    y = lng1 - lng2

    return x**2 + y**2

def calculate_distance(capabilites, lat : float, lng: float):
    result = []
    for c in capabilites:
        print(c)
        result.append((
            c, distance(c.petani.lat, c.petani.lng, lat, lng)
        ))

    return result


def get_capabilities(id : int):
    product = Product.get(Product.id == id)
    caps = Capabilities.select().where(Capabilities.product == product)
    data = {
        "capacity" : 0,
        "petani" : [],
        "capability" : []
    }

    for c in caps:
        if date.today() < c.start_date - timedelta(days=14):
            continue
        elif date.today() > c.end_date:
            continue

        data['capacity'] += c.volume
        data['petani'].append(c.petani)
        data['capability'].append(c)

    return data

def create_order(user : User, address :str, items):
    #check balance
    #balance -= usage

    for c in user.customer:
        customer = c
        break

    order = Order(
        customer = customer,
        address = address
    )

    order.save()

    return order


def split_order(id : int, qty : float):
    caps = get_capabilities(id)

    for c in caps["capability"]:
        if c.volume >= qty:
            return [c]

    capable = []
    print("YEEE")
    capabilities = calculate_distance(caps["capability"], 0.0, 0.0)
    capabilities = sorted(capabilities, key=itemgetter(1))

    qty_left = qty

    for c in capabilities:
        if (qty_left <= 0):
            break
        capable.append(c[0])
        qty_left -= c[0].volume

    return capable

def set_order_line(product_id : int, qty : float, order : Order):
    product = Product.get(Product.id == product_id)
    caps = split_order(product_id, qty)

    print(caps)

    order_line = OrderLine(
        order = order,
        product = product,
        total_qty = qty
    )

    order_line.save()
    qty_left = qty

    for c in caps:
        supplier = Supplier(
            order_line = order_line,
            petani = c.petani,
            qty = c.volume if c.volume < qty_left else qty_left
        )
        supplier.save()
        c.volume = c.volume - supplier.qty
        c.save()

        qty_left -= supplier.qty



