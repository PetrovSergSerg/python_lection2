from data.user import User
from model.contact import Contact


def test_delete_first_contact_from_list(app):
    app.session.login(User.ADMIN)
    contact1 = Contact(lastname='first', firstname='contact')
    contact2 = Contact(lastname='second', firstname='contact')
    app.contact.create(contact1)
    app.contact.create(contact2)
    app.contact_list.delete_first_contact()
    app.session.logout()


def test_delete_last_contact_from_list(app):
    app.session.login(User.ADMIN)
    contact1 = Contact(lastname='first', firstname='contact')
    contact2 = Contact(lastname='second', firstname='contact')
    app.contact.create(contact1)
    app.contact.create(contact2)
    app.contact_list.delete_last_contact()
    app.session.logout()


def test_delete_first_contact_from_itself(app):
    app.session.login(User.ADMIN)
    contact1 = Contact(lastname='first', firstname='contact')
    contact2 = Contact(lastname='second', firstname='contact')
    app.contact.create(contact1)
    app.contact.create(contact2)
    app.contact_list.get_first_contact().delete()
    app.session.logout()


def test_delete_last_contact_from_itself(app):
    app.session.login(User.ADMIN)
    contact1 = Contact(lastname='first', firstname='contact')
    contact2 = Contact(lastname='second', firstname='contact')
    app.contact.create(contact1)
    app.contact.create(contact2)
    app.contact_list.get_last_contact().delete()
    app.session.logout()




