# -*- coding: utf-8 -*-

from model.address import Address

def test_modify_name(app):
    app.session.login(username="andrew1973@gmail.com", password="giovanni")
    app.address.modify(Address(first_name="VIKA"))
    app.session.logout()

def test_modify_street(app):
    app.session.login(username="andrew1973@gmail.com", password="giovanni")
    app.address.modify(Address(address="10Th Avenue"))
    app.session.logout()

