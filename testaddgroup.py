# -*- coding: utf-8 -*-
import pytest
from application import Application
from group import Group
from user import User


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_empty_group(app):
    app.login(User.ADMIN)
    group = Group()
    app.create_new_group(group)  # generate empty
    app.logout()


def test_add_handled_group(app):
    app.login(User.ADMIN)
    group = Group(name='any group', header='any header', footer='any footer')
    app.create_new_group(group)
    app.logout()


def test_add_random_group(app):
    app.login(User.ADMIN)
    group = Group().set_random_parameters()  # generate fully random group
    app.create_new_group(group)
    app.logout()
