from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class ContactListHelper:
    def __init__(self, app):
        self.app = app
        self.menu = app.menu
        self.contact = app.contact

    def get_first_contact(self):
        wd = self.app.wd
        self.menu.home()

        edit = wd.find_element_by_xpath("//img[@title='Edit']")
        edit.click()

        return self.contact

    def get_last_contact(self):
        wd = self.app.wd
        self.menu.home()

        edit_list = wd.find_elements_by_xpath("//img[@title='Edit']")
        assert len(edit_list) > 0

        edit_last = edit_list[len(edit_list) - 1]
        edit_last.click()

        return self.contact

    def delete_first_contact(self):
        wd = self.app.wd
        self.menu.home()

        wd.find_element_by_name("selected[]").click()

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

    def delete_last_contact(self):
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
