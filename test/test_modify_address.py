# -*- coding: utf-8 -*-

from model.address import Address

def test_modify_name(app):
    old_addresses = app.address.get_addresses_list()
    app.address.modify(Address(first_name="VIKA"))
    new_addresses = app.address.get_addresses_list()
    assert len(old_addresses) == len(new_addresses)

def test_modify_street(app):
    old_addresses = app.address.get_addresses_list()
    app.address.modify(Address(address="10Th Avenue"))
    new_addresses = app.address.get_addresses_list()
    assert len(old_addresses) == len(new_addresses)

