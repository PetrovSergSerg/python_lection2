from selenium.webdriver.support.ui import Select
from model.contact import Contact
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from random import randint


class ContactHelper:
    def __init__(self, app):
        self.app = app
        self.menu = app.menu

    def create(self, contact: Contact):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

        if contact.firstname is not None:
            wd.find_element_by_name("firstname").send_keys(contact.firstname)
        if contact.middlename is not None:
            wd.find_element_by_name("middlename").send_keys(contact.middlename)
        if contact.lastname is not None:
            wd.find_element_by_name("lastname").send_keys(contact.lastname)
        if contact.nickname is not None:
            wd.find_element_by_name("nickname").send_keys(contact.nickname)

        if contact.title is not None:
            wd.find_element_by_name("title").send_keys(contact.title)
        if contact.company is not None:
            wd.find_element_by_name("company").send_keys(contact.company)
        if contact.address is not None:
            wd.find_element_by_name("address").send_keys(contact.address)

        if contact.phone_home is not None:
            wd.find_element_by_name("home").send_keys(contact.phone_home)
        if contact.mobile is not None:
            wd.find_element_by_name("mobile").send_keys(contact.mobile)
        if contact.phone_work is not None:
            wd.find_element_by_name("work").send_keys(contact.phone_work)
        if contact.fax is not None:
            wd.find_element_by_name("fax").send_keys(contact.fax)

        if contact.email_main is not None:
            wd.find_element_by_name("email").send_keys(contact.email_main)
        if contact.email_secondary is not None:
            wd.find_element_by_name("email2").send_keys(contact.email_secondary)
        if contact.email_other is not None:
            wd.find_element_by_name("email3").send_keys(contact.email_other)
        if contact.homepage is not None:
            wd.find_element_by_name("homepage").send_keys(contact.homepage)

        if contact.bday is not None:
            selector = Select(wd.find_element_by_name("bday"))
            selector.select_by_visible_text(contact.bday)
        if contact.bmonth is not None:
            selector = Select(wd.find_element_by_name("bmonth"))
            selector.select_by_visible_text(contact.bmonth)
        if contact.byear is not None:
            wd.find_element_by_name("byear").send_keys(contact.byear)

        if contact.aday is not None:
            selector = Select(wd.find_element_by_name("aday"))
            selector.select_by_visible_text(contact.aday)
        if contact.amonth is not None:
            selector = Select(wd.find_element_by_name("amonth"))
            selector.select_by_visible_text(contact.amonth)
        if contact.ayear is not None:
            wd.find_element_by_name("ayear").send_keys(contact.ayear)

        if contact.address_secondary is not None:
            wd.find_element_by_name("address2").send_keys(contact.address_secondary)
        if contact.phone_secondary is not None:
            wd.find_element_by_name("phone2").send_keys(contact.phone_secondary)
        if contact.notes is not None:
            wd.find_element_by_name("notes").send_keys(contact.notes)

        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

        self.menu.home()

    def edit_any_contact(self, new_contact: Contact):
        wd = self.app.wd
        self.menu.home()

        edit_list = wd.find_elements_by_xpath("//img[@title='Edit']")
        assert len(edit_list) > 0

        edit = edit_list[randint(0, len(edit_list) - 1)]
        edit.click()

        if new_contact.firstname is not None:
            wd.find_element_by_name("firstname").clear()
            wd.find_element_by_name("firstname").send_keys(new_contact.firstname)
        if new_contact.middlename is not None:
            wd.find_element_by_name("middlename").clear()
            wd.find_element_by_name("middlename").send_keys(new_contact.middlename)
        if new_contact.lastname is not None:
            wd.find_element_by_name("lastname").clear()
            wd.find_element_by_name("lastname").send_keys(new_contact.lastname)
        if new_contact.nickname is not None:
            wd.find_element_by_name("nickname").clear()
            wd.find_element_by_name("nickname").send_keys(new_contact.nickname)

        if new_contact.title is not None:
            wd.find_element_by_name("title").clear()
            wd.find_element_by_name("title").send_keys(new_contact.title)
        if new_contact.company is not None:
            wd.find_element_by_name("company").clear()
            wd.find_element_by_name("company").send_keys(new_contact.company)
        if new_contact.address is not None:
            wd.find_element_by_name("address").clear()
            wd.find_element_by_name("address").send_keys(new_contact.address)

        if new_contact.phone_home is not None:
            wd.find_element_by_name("home").clear()
            wd.find_element_by_name("home").send_keys(new_contact.phone_home)
        if new_contact.mobile is not None:
            wd.find_element_by_name("mobile").clear()
            wd.find_element_by_name("mobile").send_keys(new_contact.mobile)
        if new_contact.phone_work is not None:
            wd.find_element_by_name("work").clear()
            wd.find_element_by_name("work").send_keys(new_contact.phone_work)
        if new_contact.fax is not None:
            wd.find_element_by_name("fax").clear()
            wd.find_element_by_name("fax").send_keys(new_contact.fax)

        if new_contact.email_main is not None:
            wd.find_element_by_name("email").clear()
            wd.find_element_by_name("email").send_keys(new_contact.email_main)
        if new_contact.email_secondary is not None:
            wd.find_element_by_name("email2").clear()
            wd.find_element_by_name("email2").send_keys(new_contact.email_secondary)
        if new_contact.email_other is not None:
            wd.find_element_by_name("email3").clear()
            wd.find_element_by_name("email3").send_keys(new_contact.email_other)
        if new_contact.homepage is not None:
            wd.find_element_by_name("homepage").clear()
            wd.find_element_by_name("homepage").send_keys(new_contact.homepage)

        if new_contact.bday is not None:
            selector = Select(wd.find_element_by_name("bday"))
            selector.select_by_visible_text(new_contact.bday)
        if new_contact.bmonth is not None:
            selector = Select(wd.find_element_by_name("bmonth"))
            selector.select_by_visible_text(new_contact.bmonth)
        if new_contact.byear is not None:
            wd.find_element_by_name("byear").clear()
            wd.find_element_by_name("byear").send_keys(new_contact.byear)

        if new_contact.aday is not None:
            selector = Select(wd.find_element_by_name("aday"))
            selector.select_by_visible_text(new_contact.aday)
        if new_contact.amonth is not None:
            selector = Select(wd.find_element_by_name("amonth"))
            selector.select_by_visible_text(new_contact.amonth)
        if new_contact.ayear is not None:
            wd.find_element_by_name("ayear").clear()
            wd.find_element_by_name("ayear").send_keys(new_contact.ayear)

        if new_contact.address_secondary is not None:
            wd.find_element_by_name("address2").clear()
            wd.find_element_by_name("address2").send_keys(new_contact.address_secondary)
        if new_contact.phone_secondary is not None:
            wd.find_element_by_name("phone2").clear()
            wd.find_element_by_name("phone2").send_keys(new_contact.phone_secondary)
        if new_contact.notes is not None:
            wd.find_element_by_name("notes").clear()
            wd.find_element_by_name("notes").send_keys(new_contact.notes)

        update = wd.find_element_by_xpath("//input[@type='submit'][@value='Update']")
        update.click()

        self.menu.home()

    def delete_any_contact_from_itself(self):
        wd = self.app.wd
        self.menu.home()

        edit_list = wd.find_elements_by_xpath("//img[@title='Edit']")
        assert len(edit_list) > 0

        edit = edit_list[randint(0, len(edit_list) - 1)]
        edit.click()

        delete = wd.find_element_by_xpath("//input[@type='submit'][@value='Delete']")
        delete.click()

        self.menu.home()

    def delete_any_contact_form_list(self):
        wd = self.app.wd
        self.menu.home()

        checkbox_list = wd.find_elements_by_name("selected[]")
        assert len(checkbox_list) > 0

        checkbox_last = checkbox_list[len(checkbox_list) - 1]
        checkbox_last.click()

        delete = wd.find_element_by_xpath("//input[@type='button'][@value='Delete']")
        delete.click()

        try:
            WebDriverWait(wd, 1).until(EC.alert_is_present(), 'Не дождались алёрта')
            alert = wd.switch_to.alert
            alert.accept()
        except TimeoutException:
            print("no alert")
        finally:
            self.menu.home()
