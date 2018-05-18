from controller.base_controller import Controller
from model.base_model import Capabilities, Product
from datetime import datetime

class CapabilityController(Controller):
    def all(self):
        user = self.is_logged_in()
        if not user:
            raise Exception("Unexpected login status")

        for p in user.petani:
            petani = p
            break

        caps = Capabilities.select().where(Capabilities.petani == petani)

        data = {
            "capabilities" : []
        }

        for c in caps:
            data["capabilities"].append({
                "id" : c.id,
                "volume" : c.volume,
                "start_date" : c.start_date,
                "end_date" : c.end_date,
                "product" : c.product.id
            })


        return data

    def update(self):
        user = self.is_logged_in()
        if not user:
            raise Exception("Unexpected login status")

        for p in user.petani:
            petani = p
            break

        cap = Capabilities.get(Capabilities.id == self.data[0], Capabilities.petani == petani)
        cap.volume = self.volume
        cap.start_date = datetime.strptime(self.start_date, "%d-%m-%Y").date()
        cap.end_date = datetime.strptime(self.end_date, "%d-%m-%Y").date()

        cap.save()

        return {
            "id" : cap.id,
            "volume" : cap.volume,
            "start_date" : cap.start_date,
            "end_date" : cap.end_date,
            "product" : cap.product.id
        }

    def insert(self):
        user = self.is_logged_in()
        if not user:
            raise Exception("Unexpected login status")

        for p in user.petani:
            petani = p
            break

        product = Product.get(Product.id == self.product_id)

        cap = Capabilities(
            volume = self.volume,
            petani = petani,
            start_date = datetime.strptime(self.start_date, "%d-%m-%Y").date(),
            end_date = datetime.strptime(self.end_date, "%d-%m-%Y").date(),
            product = product
        )
        cap.save()

        return {
            "id" : cap.id,
            "volume" : cap.volume,
            "start_date" : cap.start_date,
            "end_date" : cap.end_date,
            "product" : cap.product.id
        }
