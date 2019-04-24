
from model.address import Address


# прямая проверка производится обрезка
def test_phones_on_address_page(app):
    if app.address.count() == 0:
        app.address.add(Address(first_name="ANDREW", last_name="KRIV", company="IT",
                                          address="Ivana Franka 5/16", zipcode="12345", city="Kyiv",
                                          country="Украина", home_phone="+(1) 23-456", mobile_phone="+(7) 89-456",
                                          state="Киевская область", title="AND"))
    contact_from_address_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_from_edit_page(0)
    assert app.contact.clear(contact_from_address_page.home_phone) == \
           app.contact.clear(contact_from_edit_page.home_phone)
    assert app.contact.clear(contact_from_address_page.mobile_phone) == \
           app.contact.clear(contact_from_edit_page.mobile_phone)

# обратная проверка производится склейка
def test_merge_phones_on_address_page(app):
    if app.address.count() == 0:
        app.address.add(Address(first_name="ANDREW", last_name="KRIV", company="IT",
                                          address="Ivana Franka 5/16", zipcode="12345", city="Kyiv",
                                          country="Украина", home_phone="+(1) 23-456", mobile_phone="+(7) 89-456",
                                          state="Киевская область", title="ANDR"))
    contact_from_address_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_from_edit_page(0)
    assert app.contact.clear(contact_from_address_page.all_phones) == \
           app.contact.merge_phones(contact_from_edit_page)

