class MenuHelper:
    def __init__(self, app):
        self.app = app

    def home(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()

    def groups(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()
