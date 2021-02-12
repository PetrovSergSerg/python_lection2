from model.contact import Contact
from data.user import User


def test_add_empty_contact(app):
    app.session.login(User.ADMIN)
    empty_contact = Contact()  # generate empty contact
    app.contact.create(empty_contact)
    app.session.logout()


def test_add_handled_contact(app):
    app.session.login(User.ADMIN)
    empty_contact = Contact(lastname='aaa', firstname='bbb', middlename='ccc', nickname='ddd', title='kkk',
                            company='lll', address='mmm', home='111', mobile='222', work='333', fax='444',
                            main='a@a.ru', secondary='b@b.ru', other='c@c.ru', homepage='http://', byear='1994',
                            bmonth='April', bday='15', ayear='2003', amonth='September', aday='4', address2='xxx',
                            phone='777', notes='zzz')
    app.contact.create(empty_contact)
    app.session.logout()


def test_add_random_contact(app):
    app.session.login(User.ADMIN)
    random_contact = Contact().set_random_parameters()  # generate fully random contact
    app.contact.create(random_contact)
    app.session.logout()