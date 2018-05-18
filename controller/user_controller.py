from controller.base_controller import Controller
from model.user_model import login_petani, login_customer, register_customer, register_petani, edit_profile_customer, edit_profile_petani

class UserController(Controller):
    def login_status(self):
        if self.is_logged_in():
            return {"status" : True}
        else:
            return {"status" : False}


    def login_petani(self):
        if self.is_logged_in():
            raise Exception("Unexpected login status")

        session = login_petani(self.phone, self.password)

        for p in session.user.petani:
            petani = p
            break

        data = {
            "first_name" : session.user.first_name,
            "last_name" : session.user.last_name,
            "phone" : petani.phone,
            "public_key" : session.user.public_key,
            "session_id" : session.session_id
        }

        return data

    def login_customer(self):
        if self.is_logged_in():
            raise Exception("Unexpected login status")

        session = login_customer(self.email, self.password)

        for c in session.user.customer:
            customer = c
            break

        data = {
            "first_name" : session.user.first_name,
            "last_name" : session.user.last_name,
            "email" : customer.email,
            "public_key" : session.user.public_key,
            "session_id" : session.session_id
        }

        return data

    def register_petani(self):
        if self.is_logged_in():
            raise Exception("Unexpected login status")

        session = register_petani(
            self.first_name,
            self.last_name,
            self.phone,
            self.password,
            self.lat,
            self.lng
        )

        for p in session.user.petani:
            petani = p
            break

        data = {
            "first_name" : session.user.first_name,
            "last_name" : session.user.last_name,
            "phone" : petani.phone,
            "public_key" : session.user.public_key,
            "session_id" : session.session_id
        }

        return data

    def register_customer(self):
        if self.is_logged_in():
            raise Exception("Unexpected login status")

        session = register_customer(
            self.first_name,
            self.last_name,
            self.email,
            self.password
        )

        for c in session.user.customer:
            customer = c
            break

        data = {
            "first_name" : session.user.first_name,
            "last_name" : session.user.last_name,
            "email" : customer.email,
            "public_key" : session.user.public_key,
            "session_id" : session.session_id
        }

        return data

    def edit_profile_customer(self):
        user = self.is_logged_in()
        if not user:
            raise Exception("Unexpected login status")

        customer = edit_profile_customer(user, self.email, self.password)

        data = {
            "first_name" : customer.user.first_name,
            "last_name" : customer.user.last_name,
            "email" : customer.email,
            "public_key" : customer.user.public_key,
        }

        return data

    def edit_profile_petani(self):
        user = self.is_logged_in()

        if not user:
            raise Exception("Unexpected login status")

        petani = edit_profile_petani(user, self.phone, self.password, self.lat, self.lng)

        data = {
            "first_name" : petani.user.first_name,
            "last_name" : petani.user.last_name,
            "phone" : petani.phone,
            "public_key" : petani.user.public_key,
            "lat" : petani.lat,
            "lng" : petani.lng
        }

        return data

    def profile_customer(self):
        user = self.is_logged_in()

        if not user:
            raise Exception("Unexpected login status")

        for c in user.customer:
            customer = c
            break

        data = {
            "id" : user.id,
            "first_name" : user.first_name,
            "last_name" : user.last_name,
            "profile_pic" : user.profile_pic,
            "email" : customer.email
        }

        return data

    def profile_petani(self):
        user = self.is_logged_in()

        if not user:
            raise Exception("Unexpected login status")

        for c in user.petani:
            petani = c
            break

        data = {
            "id" : user.id,
            "first_name" : user.first_name,
            "last_name" : user.last_name,
            "profile_pic" : user.profile_pic,
            "phone" : petani.phone
        }

        return data
