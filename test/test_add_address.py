# -*- coding: utf-8 -*-
import time
from model.address import Address

def test_add_first_address(app):
    app.session.login(username="andrew1973@gmail.com", password="giovanni")
    app.address.add(Address(first_name="andrew", last_name="kriv", company="IT", address="Ivana Franka 5/16",
                            zipcode="12345", city="Kyiv", country="Украина", home_phone="123456",
                            mobile_phone="123456", state="Киевская область", assign="andr"))
    app.session.logout()

def test_add_second_address(app):
    app.session.login(username="andrew1973@gmail.com", password="giovanni")
    app.address.add_new(Address(first_name="andrew", last_name="kriv", company="IT", address="George Washington 20",
                                zipcode="67890", city="Columbus", country="США", home_phone="789123",
                                mobile_phone="789123", state="Alabama", assign="MUCHO"))
   # time.sleep(30)
    app.session.logout()

