# -*- coding: utf-8 -*-
import pytest
from fixture.application import Application
from model.contact import Contact
from data.user import User


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_empty_contact(app):
    app.login(User.ADMIN)
    empty_contact = Contact()  # generate empty contact
    app.create_new_contact(empty_contact)
    app.logout()


def test_add_handled_contact(app):
    app.login(User.ADMIN)
    empty_contact = Contact(lastname='aaa', firstname='bbb', middlename='ccc', nickname='ddd', title='kkk',
                            company='lll', address='mmm', home='111', mobile='222', work='333', fax='444',
                            main='a@a.ru', secondary='b@b.ru', other='c@c.ru', homepage='http://', byear='1994',
                            bmonth='April', bday='15', ayear='2003', amonth='September', aday='4', address2='xxx',
                            phone='777', notes='zzz')
    app.create_new_contact(empty_contact)
    app.logout()


def test_add_random_contact(app):
    app.login(User.ADMIN)
    random_contact = Contact().set_random_parameters()  # generate fully random contact
    app.create_new_contact(random_contact)
    app.logout()