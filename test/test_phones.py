
from data.addresses import fixed_testdata


# прямая проверка производится обрезка
def test_phones_on_address_page(app):
    if app.address.count() == 0:
        app.address.add(fixed_testdata[0])
    contact_from_address_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_from_edit_page(0)
    assert app.contact.clear(contact_from_address_page.home_phone) == \
           app.contact.clear(contact_from_edit_page.home_phone)
    assert app.contact.clear(contact_from_address_page.mobile_phone) == \
           app.contact.clear(contact_from_edit_page.mobile_phone)

# обратная проверка производится склейка
def test_merge_phones_on_address_page(app):
    if app.address.count() == 0:
        app.address.add(fixed_testdata[0])
    contact_from_address_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_from_edit_page(0)
    assert app.contact.clear(contact_from_address_page.all_phones) == \
           app.contact.merge_phones(contact_from_edit_page)

