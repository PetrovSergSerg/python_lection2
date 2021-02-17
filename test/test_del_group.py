from data.user import User
from model.group import Group


def test_delete_any_group(app):
    app.session.login(User.ADMIN)
    group1 = Group().set_all_parameters_to_random_value()
    group2 = Group().set_all_parameters_to_random_value()
    app.group.create(group1)
    app.group.create(group2)
    app.group.delete_any_group()
    app.session.logout()
