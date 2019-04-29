# -*- coding: utf-8 -*-
from model.address import Address
import random
import string


def random_all_symbols(maxlen):
    symbols = string.ascii_letters + string.digits  # + string.punctuation + " " * 10
    return "".join([random.choice(symbols) for i in range(maxlen)])  # фиксированное количество символов
                                                # range(random.randrange(maxlen))])  # случайное количество
def random_letters(maxlen):
    letters = string.ascii_letters #+ " " * 10
    return "".join([random.choice(letters) for i in range(maxlen)])

def random_digits(maxlen):
    digits = string.digits
    return "".join([random.choice(digits) for i in range(maxlen)])

random_testdata = [
    Address(first_name=random_letters(10),
            last_name=random_letters(10),
            company=random_all_symbols(7),
            address=random_letters(20),
            zipcode=random_digits(5),
            city=random_all_symbols(10),
            country="США",
            home_phone=random_digits(15),
            mobile_phone=random_digits(15),
            state="Alabama",
            title=random_letters(5))
    for i in range(5)
]

fixed_testdata = [
    Address(first_name="Andrew", last_name="Kriv", company="IT", address="Ivana Franka 5/16",
                            zipcode="12345", city="Kyiv", country="Украина", home_phone="+(1) 11-111",
                            mobile_phone="+(2) 22-222", state="Киевская область", title="AK"),
    Address(first_name="Piter", last_name="Johnson", company="IT", address="George Washington 20",
                      zipcode="67890", city="Columbus", country="США", home_phone="+(3) 33-333",
                      mobile_phone="+(4) 44-444", state="Alabama", title="PJ"),
    Address(first_name="John", last_name="Smith", company="IT", address="Linkoln Avenu 15",
                      zipcode="11121", city="Trenton", country="США", home_phone="+(5) 55-555",
                      mobile_phone="+(6) 66-666", state="New Jersey", title="JS")
]
