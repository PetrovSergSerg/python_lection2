from model.group import Group


class GroupHelper:
    def __init__(self, app):
        self.app = app
        self.menu = app.menu

    def create_new_group(self, group: Group):
        wd = self.app.wd
        self.menu.open_groups_page()
        wd.find_element_by_name("new").click()

        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)

        wd.find_element_by_name("submit").click()
        self.return_to_groups_page()

    def return_to_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()
