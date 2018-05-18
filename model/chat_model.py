from model.base_model import ChatRoom, Chat, User

def send_message(from_user : User, room_id : int, msg : str, tipe: str):
    room = ChatRoom.get(ChatRoom.id == room_id)

    if from_user == room.customer.user:
        to_user = room.petani.user
    elif from_user == room.petani.user:
        to_user = room.customer.user
    else:
        raise Exception("Invalid chat room")

    chat = Chat(
        chat_room = room,
        from_user = from_user,
        to_user = to_user,
        tipe = tipe,
        msg = msg
    )

    chat.save()

    data = {
        "uid" : chat.uid,
        "to_user" : to_user.id,
        "room" : room.id,
        "tipe" : chat.tipe,
        "msg" : chat.msg
    }

    return data

def get_chat_rooms(user: User):
    for c in user.customer:
        real_user = c
        customer = True
        petani = False
        break

    for p in user.petani:
        real_user = p
        petani = True
        customer = False
        break

    if customer:
        rooms = ChatRoom.select().where(ChatRoom.customer == real_user)
    elif petani:
        rooms = ChatRoom.select().where(ChatRoom.petani == real_user)

    data = {
        "rooms" : []
    }

    for r in rooms:
        data["rooms"].append({
            "id" : r.id,
            "with_user" : r.petani.user.id if customer else r.customer.user.id
        })

    return data

def get_messages(user: User, uid : str, room_id: int):
    room = ChatRoom.get(ChatRoom.id == room_id)

    if (user.id == room.customer.user.id):
        pass
    elif (user.id == room.petani.user.id):
        pass
    else:
        raise Exception("Invalid chat room")

    if uid != "":
        created_at = Chat.get(Chat.uid == uid).createdAt
        messages = Chat.select().where(Chat.createdAt > created_at, Chat.chat_room == room)
    else:
        messages = Chat.select().where(Chat.chat_room == room)

    data = {
        "messages" : []
    }

    for m in messages:
        data["messages"].append({
            "uid" : m.uid,
            "msg" : m.msg,
            "from_user" : m.from_user.id
        })

    return data
