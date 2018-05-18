from flask import jsonify
from model.base_model import db
from model.user_model import is_logged_in

class Controller:
    def __init__(self, data : list, post_data : dict, auth=""):
        self.data = data
        self.auth = auth
        if post_data :
            for key, value in post_data.items():
                setattr(self, key, value)

    def render(self, data : dict):
        return jsonify(data)

    def throw_error(self, error : str, code=500):
        data = {
            "msg" : error,
            "code" : code
        }

        return jsonify(data), code

    def is_logged_in(self):
        if not self.auth or self.auth == "":
            print(self.auth)
            return False
        else:
            return is_logged_in(self.auth)

    @classmethod
    def parse(cls, data, post_data, auth, method):
        instance = cls(data, post_data, auth)

        instance_method = getattr(instance, method)

        try:
            db.connect()
            return instance.render(instance_method())
        except Exception as e:
            print(e)
            return instance.throw_error(str(e), 200)
        finally:
            db.close()
