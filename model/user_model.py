from model.base_model import User, Petani, Session, Customer
from util import hash_keyword

def is_logged_in(auth):
    if not auth or auth == "":
        return None

    try:
        session = Session.get(Session.session_id == auth)
    except Exception as e:
        print(e)
        return None

    return session.user


def is_petani_exists(phone : str):
    try:
        petani = Petani.get(Petani.phone == phone)
        return petani
    except:
        return False


def is_customer_exists(email: str):
    try:
        customer = Customer.get(Customer.email == email)
        return customer
    except:
        return False


def register_petani(first_name : str, last_name : str, phone : str, password : str, lat : float, lng : float):
    if is_petani_exists(phone):
        raise Exception("User already exist")

    password = hash_keyword(password)

    user = User(
        first_name = first_name,
        last_name = last_name,
        password = password
    )

    user.save()

    petani = Petani(
        user = user,
        phone = phone,
        lat = lat,
        lng = lng
    )

    petani.save()

    session = Session(
        user = user
    )

    session.save()

    return session

def register_customer(first_name : str, last_name : str, email : str, password : str):
    if is_customer_exists(email):
        raise Exception("User already exists")

    password = hash_keyword(password)

    user = User(
        first_name = first_name,
        last_name = last_name,
        password = password
    )

    user.save()

    customer = Customer(
        user = user,
        email = email
    )

    customer.save()

    session = Session(
        user = user
    )

    session.save()

    return session


def login_petani(phone : str, password : str):
    petani = is_petani_exists(phone)
    if not petani:
        raise  Exception("User not found")

    if petani.user.password == hash_keyword(password):
        session = Session(user = petani.user)
        session.save()
        return session


def login_customer(email: str, password: str):
    customer = is_customer_exists(email)
    if not customer:
        raise Exception("User not found")

    if customer.user.password == hash_keyword(password):
        session = Session(user = customer.user)
        session.save()
        return session

def edit_profile_customer(user, email : str, password: str):
    for c in user.customer:
        customer = c
        break

    customer.email = email
    user.password = hash_keyword(password)

    customer.save()
    user.save()

    return customer

def edit_profile_petani(user, phone : str, password: str, lat=0.0, lng=0.0):
    for p in user.petani:
        petani = p
        break

    petani.phone = phone
    petani.lat = lat
    petani.lng = lng
    user.password = hash_keyword(password)

    petani.save()
    user.save()

    return petani
