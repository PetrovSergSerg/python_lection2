from model.group import Group
from random import randint


class GroupHelper:
    def __init__(self, app):
        self.app = app
        self.menu = app.menu

    def create(self, group: Group):
        wd = self.app.wd
        self.menu.groups()

        wd.find_element_by_name("new").click()
        self.fill(group)

        wd.find_element_by_name("submit").click()
        self.return_to_groups_page()

    def edit_any_group(self, group: Group):
        wd = self.app.wd

        checkbox_list = wd.find_elements_by_name("selected[]")
        assert len(checkbox_list) > 0

        checkbox = checkbox_list[randint(0, len(checkbox_list) - 1)]
        checkbox.click()

        wd.find_element_by_name("edit").click()

        self.fill(group)

        wd.find_element_by_name("update").click()
        self.return_to_groups_page()

    def delete_any_group(self):
        wd = self.app.wd
        self.menu.groups()

        checkbox_list = wd.find_elements_by_name("selected[]")
        assert len(checkbox_list) > 0

        checkbox = checkbox_list[randint(0, len(checkbox_list) - 1)]
        checkbox.click()

        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()

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

    def return_to_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()
