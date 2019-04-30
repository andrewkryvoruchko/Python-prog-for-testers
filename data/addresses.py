# -*- coding: utf-8 -*-
from model.address import Address

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
