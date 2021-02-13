from data.user import User
from model.group import Group


def test_edit_any_group(app):
    app.session.login(User.ADMIN)
    group1 = Group().set_all_parameters_to_random_value()
    app.group_list.new().fill(group1)
    group_new_state = Group().set_random_parameters_to_random_value()
    app.group_list.select_any_group().get().edit(group_new_state)
    app.session.logout()
