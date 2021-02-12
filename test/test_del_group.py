from data.user import User


def test_delete_first_group(app):
    app.session.login(User.ADMIN)
    app.group.delete_first_group()  # generate empty
    app.session.logout()

