# models
import random

from faker import Faker

fake = Faker()


class FakeUserData:
    @staticmethod
    def random():
        username = fake.email()
        password = fake.password()
        return {"username": username, "password": password}

    @staticmethod
    def random_user_info():
        phone = fake.phone_number()
        email = fake.email()
        address = {
            "city": fake.city(),
            "street": fake.street_address(),
            "home_number": fake.building_number()
        }
        return {"phone": phone, "email": email, "address": address}

    @staticmethod
    def random_product():
        items = list()
        r = random.randrange(100)
        for i in range(r):
            words = fake.lexify(text='Product ??????????')
            items.append(words)
        return {"items": items}

    @staticmethod
    def random_item():
        word = fake.lexify(text='Product ??????????')
        return word

    @staticmethod
    def random_store_item(store_id):
        number = random.randrange(100)
        # price = f"{number}{fake.cryptocurrency()}"
        price = number
        description = fake.lexify(text='?????????????????')
        image = f"{fake.lexify(text='?????????????????.')}{fake.file_extension(category='image')}"
        return {"price": price, "store_id": store_id, "description": description, "image": image}


class ResponseModel:
    def __init__(self, status: int, response: dict = None):
        self.status = status
        self.response = response
