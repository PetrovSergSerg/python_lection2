from data.user import User
from model.contact import Contact


def test_delete_any_contact_from_list(app):
    app.session.login(User.ADMIN)
    contact1 = Contact(lastname='first', firstname='contact')
    contact2 = Contact(lastname='second', firstname='contact')
    app.contact.create(contact1)
    app.contact.create(contact2)
    app.contact.delete_any_contact_form_list()
    app.session.logout()


def test_delete_any_contact_from_itself(app):
    app.session.login(User.ADMIN)
    contact1 = Contact(lastname='first', firstname='contact')
    contact2 = Contact(lastname='second', firstname='contact')
    app.contact.create(contact1)
    app.contact.create(contact2)
    app.contact.delete_any_contact_from_itself()
    app.session.logout()





