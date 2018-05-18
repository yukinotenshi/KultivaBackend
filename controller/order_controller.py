from controller.base_controller import Controller
import model.order_model as m

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
