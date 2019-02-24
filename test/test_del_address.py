# -*- coding: utf-8 -*-

def test_delete_first_address(app):
    app.session.login(username="andrew1973@gmail.com", password="giovanni")
    app.address.delete_first_address()
    app.session.logout()

