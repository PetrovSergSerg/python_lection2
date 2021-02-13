from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from random import randint


class ContactListHelper:
    def __init__(self, app):
        self.app = app
        self.menu = app.menu
        self.contact = app.contact

    def get_any_contact(self):
        wd = self.app.wd
        self.menu.home()

        edit_list = wd.find_elements_by_xpath("//img[@title='Edit']")
        assert len(edit_list) > 0

        edit = edit_list[randint(0, len(edit_list) - 1)]
        edit.click()

        return self.contact

    def select_any_contact(self):
        wd = self.app.wd
        self.menu.home()

        checkbox_list = wd.find_elements_by_name("selected[]")
        assert len(checkbox_list) > 0

        checkbox = checkbox_list[randint(0, len(checkbox_list) - 1)]
        checkbox.click()

        return self

    def delete(self):
        wd = self.app.wd

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
