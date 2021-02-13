from data.user import User


def test_delete_first_contact_from_list(app):
    app.session.login(User.ADMIN)
    app.contact.delete_first_contact_from_list()
    app.session.logout()


def test_delete_first_contact_from_itself(app):
    app.session.login(User.ADMIN)
    app.contact.delete_first_contact_form_itself()
    app.session.logout()


def test_delete_last_contact_from_list(app):
    app.session.login(User.ADMIN)
    app.contact.delete_last_contact_form_list()
    app.session.logout()

