# -*- coding: utf-8 -*-

from model.address import Address

def test_modify_name(app):
    app.address.modify(Address(first_name="VIKA"))

def test_modify_street(app):
    app.address.modify(Address(address="10Th Avenue"))

