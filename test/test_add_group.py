from model.group import Group
from data.user import User


def test_add_empty_group(app):
    app.session.login(User.ADMIN)
    group = Group().set_empty_parameters()
    app.group.create(group)
    app.session.logout()


def test_add_handled_group(app):
    app.session.login(User.ADMIN)
    group = Group(name='any group', header='any header', footer='any footer')
    app.group.create(group)
    app.session.logout()


def test_add_random_group(app):
    app.session.login(User.ADMIN)
    group = Group().set_all_parameters_to_random_value()
    app.group.create(group)
    app.session.logout()
