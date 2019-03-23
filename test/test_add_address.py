# -*- coding: utf-8 -*-
from model.address import Address

# при запусте тестов вначале определяется и запускается фикстура метод app указанный в парамете теста

def test_add_first_address(app): # так же параметер app принимает объект Application из фикстуры
    old_addresses = app.address.get_addresses_list()
    app.address.add(Address(first_name="andreW", last_name="kriv", company="IT", address="Ivana Franka 5/16",
                            zipcode="12345", city="Kyiv", country="Украина", home_phone="123456",
                            mobile_phone="123456", state="Киевская область", title="andr"))
    new_addresses = app.address.get_addresses_list()
    assert len(old_addresses) + 1 == len(new_addresses)

def test_add_second_address(app):
    old_addresses = app.address.get_addresses_list()
    app.address.add_new(Address(first_name="andrew", last_name="kriV", company="IT", address="George Washington 20",
                                zipcode="67890", city="Columbus", country="США", home_phone="789123",
                                mobile_phone="789123", state="Alabama", title="MUCHO"))
    new_addresses = app.address.get_addresses_list()
    assert len(old_addresses) + 1 == len(new_addresses)


