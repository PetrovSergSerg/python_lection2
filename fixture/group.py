from model.group import Group


class GroupHelper:
    def __init__(self, app):
        self.app = app
        self.menu = app.menu

    def create(self, group: Group):
        wd = self.app.wd

        self.fill(group)

        wd.find_element_by_name("submit").click()
        GroupHelper.return_to_groups_page(self)

    def edit(self, group: Group):
        wd = self.app.wd

        self.fill(group)

        wd.find_element_by_name("update").click()
        GroupHelper.return_to_groups_page(self)

    def fill(self, group):
        wd = self.app.wd

        if group.name is not None:
            wd.find_element_by_name("group_name").clear()
            wd.find_element_by_name("group_name").send_keys(group.name)
        if group.header is not None:
            wd.find_element_by_name("group_header").clear()
            wd.find_element_by_name("group_header").send_keys(group.header)
        if group.footer is not None:
            wd.find_element_by_name("group_footer").clear()
            wd.find_element_by_name("group_footer").send_keys(group.footer)

    @staticmethod
    def return_to_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()
