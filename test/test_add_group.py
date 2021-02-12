from model.group import Group
from data.user import User


def test_add_empty_group(app):
    app.session.login(User.ADMIN)
    group = Group()
    app.group.create(group)  # generate empty
    app.session.logout()


def test_add_handled_group(app):
    app.session.login(User.ADMIN)
    group = Group(name='any group', header='any header', footer='any footer')
    app.group.create(group)
    app.session.logout()


def test_add_random_group(app):
    app.session.login(User.ADMIN)
    group = Group().set_random_parameters()  # generate fully random group
    app.group.create(group)
    app.session.logout()
