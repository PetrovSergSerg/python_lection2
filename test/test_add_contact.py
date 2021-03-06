from model.contact import Contact
from data.user import User


def test_add_empty_contact(app):
    app.session.login(User.ADMIN)
    empty_contact = Contact().set_empty_parameters()  # generate empty contact
    app.contact.create(empty_contact)
    app.session.logout()


def test_add_handled_contact(app):
    app.session.login(User.ADMIN)
    contact = Contact(lastname='aaa', firstname='bbb', middlename='ccc', nickname='ddd', title='kkk',
                      company='lll', address='mmm', phone_home='111', mobile='222', phone_work='333', fax='444',
                      email_main='a@a.ru', email_secondary='b@b.ru', email_other='c@c.ru', homepage='http://',
                      byear='1994', bmonth='April', bday='15', ayear='2003', amonth='September', aday='4',
                      address_secondary='xxx', phone_secondary='777', notes='zzz')
    app.contact.create(contact)
    app.session.logout()


def test_add_random_contact(app):
    app.session.login(User.ADMIN)
    random_contact = Contact().set_all_parameters_to_random_value()  # generate fully random contact
    app.contact.create(random_contact)
    app.session.logout()
