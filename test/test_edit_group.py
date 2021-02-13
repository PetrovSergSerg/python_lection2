from data.user import User
from model.group import Group


def test_edit_first_group(app):
    app.session.login(User.ADMIN)
    group1 = Group().set_all_parameters_to_random_value()  # generate partial random group
    app.group_list.new().fill(group1)
    group_new_state = Group().set_random_parameters_to_random_value()  # generate partial random group
    app.group_list.select_first_group().get().edit(group_new_state)
    app.session.logout()


def test_edit_last_group(app):
    app.session.login(User.ADMIN)
    group1 = Group().set_all_parameters_to_random_value()  # generate partial random group
    app.group_list.new().fill(group1)
    group_new_state = Group().set_random_parameters_to_random_value()  # generate partial random group
    app.group_list.select_last_group().get().edit(group_new_state)
    app.session.logout()
