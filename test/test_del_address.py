# -*- coding: utf-8 -*-
from model.address import Address


def test_delete_first_address(app):
    if app.address.count() == 0:
        app.address.add_new(Address(first_name="ANDREW", last_name="KRIV", company="IT", address="Ivana Franka 5/16",
                                zipcode="12345", city="Kyiv", country="Украина", home_phone="123456",
                                mobile_phone="123456", state="Киевская область", assign="andr"))
    app.address.delete_first_address()

