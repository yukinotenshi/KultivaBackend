from controller.base_controller import Controller
from model.chat_model import send_message, get_chat_rooms, get_messages

class ChatController(Controller):
    def get_rooms(self):
        user = self.is_logged_in()
        if not user:
            raise Exception("Unexpected login status")

        return get_chat_rooms(user)

    def get_messages(self):
        user = self.is_logged_in()
        if not user:
            raise Exception("Unexpected login status")

        return get_messages(user, self.uid, self.room_id)

    def send_message(self):
        user = self.is_logged_in()
        if not user:
            raise Exception("Unexpected login status")


        return send_message(user, self.room_id, self.msg, self.tipe)
