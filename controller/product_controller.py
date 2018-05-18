from controller.base_controller import Controller
from model.product_model import *

class ProductController(Controller):
    def all_category(self):
        return get_all_category()

    def product_of_category(self):
        return get_product_of_category(self.data[0])

    def get_product_detail(self):
        return get_product_detail(self.data[0])
