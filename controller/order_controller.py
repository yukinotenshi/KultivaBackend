from controller.base_controller import Controller
import model.order_model as m
from model.base_model import Order

class OrderController(Controller):
    def create_order(self):
        user = self.is_logged_in()
        if not user:
            raise Exception("Unexpected login status")

        order = m.create_order(user, self.address, self.items)

        for item in self.items:
            m.set_order_line(
                item["id"],
                item["qty"], order
            )

        return {
            "status" : "success",
            "order_id" : order.id,
            "items" : self.items
        }

    def get_all_order(self):
        user = self.is_logged_in()
        if not user:
            raise Exception("Unexpected login status")

        for c in user.customer:
            customer = c
            break

        orders = Order.select().where(Order.customer == customer)

        data = {
            "orders" : []
        }

        for order in orders:
            data["orders"].append({
                "id" : order.id,
                "order_lines" : []
            })

            order_lines = order.order_line

            for ol in order_lines:
                data["orders"][-1]["order_lines"].append({
                    "id" : ol.id,
                    "product_id" : ol.product.id,
                    "qty" : ol.total_qty,
                    "updated_at" : ol.updatedAt,
                    "supplier" : []
                })
                supplier = ol.supplier
                for s in supplier:
                    data["orders"][-1]["order_lines"][-1]["supplier"].append({
                        "petani_id" : s.petani.id,
                        "lat" : s.petani.lat,
                        "lng" : s.petani.lng
                    })

        return data


    def get_orderline_petani(self):
        user = self.is_logged_in()
        if not user:
            raise Exception("Unexpected login status")

        return m.get_order_lines(user)

