from controller.base_controller import Controller
from model.product_model import *
from model.base_model import Product

class ProductController(Controller):
    def all_category(self):
        return get_all_category()

    def product_of_category(self):
        return get_product_of_category(self.data[0])

    def get_product_detail(self):
        return get_product_detail(self.data[0])

    def all_product(self):
        products = Product.select()
        data = {
            "products" : []
        }

        for p in products:
            data["products"].append({
                "id" : p.id,
                "name" : p.name,
                "price" : p.harga,
                "image" : p.image
            })

        return data
