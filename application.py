from selenium import webdriver
from selenium.webdriver.support.ui import Select
from group import Group
from contact import Contact
from user import User


class Application:
    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def login(self, user: User):
        wd = self.wd
        self.open_home_page()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(user.login)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(user.password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_groups_page(self):
        wd = self.wd
        wd.find_element_by_link_text("groups").click()

    def create_new_group(self, group: Group):
        wd = self.wd
        self.open_groups_page()
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
        wd = self.wd
        wd.find_element_by_link_text("groups").click()

    def create_new_contact(self, contact: Contact):
        wd = self.wd
        wd.find_element_by_link_text("add new").click()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("middlename").send_keys(contact.middlename)
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        wd.find_element_by_name("nickname").send_keys(contact.nickname)

        wd.find_element_by_name("title").send_keys(contact.title)
        wd.find_element_by_name("company").send_keys(contact.company)
        wd.find_element_by_name("address").send_keys(contact.address)

        wd.find_element_by_name("home").send_keys(contact.home)
        wd.find_element_by_name("mobile").send_keys(contact.mobile)
        wd.find_element_by_name("work").send_keys(contact.work)
        wd.find_element_by_name("fax").send_keys(contact.fax)

        wd.find_element_by_name("email").send_keys(contact.main)
        wd.find_element_by_name("email2").send_keys(contact.secondary)
        wd.find_element_by_name("email3").send_keys(contact.other)
        wd.find_element_by_name("homepage").send_keys(contact.homepage)

        selector = Select(wd.find_element_by_name("bday"))
        selector.select_by_visible_text(contact.bday)
        selector = Select(wd.find_element_by_name("bmonth"))
        selector.select_by_visible_text(contact.bmonth)
        wd.find_element_by_name("byear").send_keys(contact.byear)

        selector = Select(wd.find_element_by_name("aday"))
        selector.select_by_visible_text(contact.aday)
        selector = Select(wd.find_element_by_name("amonth"))
        selector.select_by_visible_text(contact.amonth)
        wd.find_element_by_name("ayear").send_keys(contact.ayear)

        wd.find_element_by_name("address2").send_keys(contact.address2)
        wd.find_element_by_name("phone2").send_keys(contact.phone)
        wd.find_element_by_name("notes").send_keys(contact.notes)

        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

        self.return_to_home_page()

    def return_to_home_page(self):
        wd = self.wd
        wd.find_element_by_link_text("home").click()

    def logout(self):
        wd = self.wd
        wd.find_element_by_link_text("Logout").click()

    def destroy(self):
        self.wd.quit()
