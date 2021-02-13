from selenium.webdriver.support.ui import Select
from model.contact import Contact
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class ContactHelper:
    def __init__(self, app):
        self.app = app
        self.menu = app.menu

    def create(self, contact: Contact):
        wd = self.app.wd
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

        self.menu.home()

    def delete_first_contact_form_itself(self):
        wd = self.app.wd
        self.menu.home()

        edit = wd.find_element_by_xpath("//img[@title='Edit']")
        edit.click()

        delete = wd.find_element_by_xpath("//input[@type='submit'][@value='Delete']")
        delete.click()

        self.menu.home()

    def delete_first_contact_from_list(self):
        wd = self.app.wd
        self.menu.home()

        wd.find_element_by_name("selected[]").click()

        delete = wd.find_element_by_xpath("//input[@type='button'][@value='Delete']")
        delete.click()

        try:
            WebDriverWait(wd, 1).until(EC.alert_is_present(), 'Не дождались алёрта')
            alert = wd.switch_to_alert()
            alert.accept()
        except TimeoutException:
            print("no alert")
        finally:
            self.menu.home()

    def delete_last_contact_form_list(self):
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
            alert = wd.switch_to_alert()
            alert.accept()
        except TimeoutException:
            print("no alert")
        finally:
            self.menu.home()
