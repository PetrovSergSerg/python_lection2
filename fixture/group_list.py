from fixture.group import GroupHelper


class GroupListHelper:
    def __init__(self, app):
        self.app = app
        self.menu = app.menu
        self.group = app.group

    def select_first_group(self):
        wd = self.app.wd
        self.menu.groups()

        wd.find_element_by_name("selected[]").click()

        return self

    def select_last_group(self):
        wd = self.app.wd
        self.menu.groups()

        checkbox_list = wd.find_elements_by_name("selected[]")
        assert len(checkbox_list) > 0

        checkbox_last = checkbox_list[len(checkbox_list) - 1]
        checkbox_last.click()

        return self

    def delete(self):
        wd = self.app.wd

        wd.find_element_by_name("delete").click()
        GroupHelper.return_to_groups_page(self)

    def get(self):
        wd = self.app.wd

        wd.find_element_by_name("edit").click()

        return self.group

    def new(self):
        wd = self.app.wd
        self.menu.groups()

        wd.find_element_by_name("new").click()

        return self.group
