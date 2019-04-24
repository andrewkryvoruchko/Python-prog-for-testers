# -*- coding: utf-8 -*-

from model.address import Address
from random import randrange


def test_modify(app):
    if app.address.count() == 0:
        app.address.add(Address(first_name="ANDREW", last_name="KRIV", company="IT",
                                          address="Ivana Franka 5/16", zipcode="12345", city="Kyiv",
                                          country="Украина", home_phone="123456", mobile_phone="123456",
                                          state="Киевская область", title="AN"))
    old_address_list = app.address.get_address_list()
    index = randrange(len(old_address_list))
    address = Address(first_name="VIKA", address="10Th Avenue")
    address.id = old_address_list[index].id
    address.title = old_address_list[index].title
    app.address.modify_by_index(index, address)
    new_address_list = app.address.get_address_list()
    assert len(old_address_list) == len(new_address_list)
    old_address_list[index] = address
    assert sorted(old_address_list, key=Address.title) == sorted(new_address_list, key=Address.title)

