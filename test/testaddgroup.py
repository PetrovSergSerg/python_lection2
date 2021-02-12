# -*- coding: utf-8 -*-
import pytest
from fixture.application import Application
from model.group import Group
from data.user import User


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_empty_group(app):
    app.session.login(User.ADMIN)
    group = Group()
    app.group.create_new_group(group)  # generate empty
    app.session.logout()


def test_add_handled_group(app):
    app.session.login(User.ADMIN)
    group = Group(name='any group', header='any header', footer='any footer')
    app.group.create_new_group(group)
    app.session.logout()


def test_add_random_group(app):
    app.session.login(User.ADMIN)
    group = Group().set_random_parameters()  # generate fully random group
    app.group.create_new_group(group)
    app.session.logout()
