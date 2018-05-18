from model.base_model import Product, Category, Capabilities

def get_all_category():
    category = Category.select()
    data = {
        "categories" : []
    }

    for c in category:
        data["categories"].append({
            "id" : c.id,
            "name" : c.name
        })

    return data


def get_product_of_category(id : int):
    category = Category.get(Category.id == id)
    product = Product.select().where(Product.category == category)

    data = {
        "products" : []
    }

    for p in product:
        data['products'].append({
            "id" : p.id,
            "name" : p.name,
            "unit" : p.unit,
            "price" : p.harga
        })

    return data

def get_product_detail(id: int):
    product = Product.get(Product.id == id)

    data = {
        "id" : product.id,
        "name" : product.name,
        "unit" : product.unit,
        "price" : product.harga,
        "locations" : []
    }

    capabilities = Capabilities.select().where(Capabilities.product == product)

    for c in capabilities:
        data['locations'].append({
            "lat" : c.petani.lat,
            "lng" : c.petani.lng
        })

    return data
