__author__ = 'viktor'

from model.project import Project
import time


class ProjectHelper:

    def __init__(self, app):
        self.app = app


    def open_project_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Manage").click()
        wd.find_element_by_link_text("Manage Projects").click()

    def change_field(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
#            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def change_value_from_list(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            element = wd.find_element_by_xpath('//select[@name="%s"]' % field_name)
            all_options = element.find_elements_by_tag_name("option")
            for option in all_options:
                if option.text == text:
                    option.click()

    def change_checkbox_value(self, field_name, text):
        wd = self.app.wd
        if text == "True":
            pass
        elif text == "False":
            wd.find_element_by_name("%s" % field_name).click()

    def fill_project_form(self, project):
        wd = self.app.wd
        self.change_field("name", project.name)
        self.change_value_from_list("status", project.status)
        self.change_checkbox_value("inherit_global", project.inherit_global)
        self.change_value_from_list("view_state", project.view_state)
        self.change_field("description", project.description)

    def create(self, project):
        wd = self.app.wd
        self.open_project_page()
        wd.find_element_by_xpath("//table[3]/tbody/tr[1]/td/form/input[2]").click()
        self.fill_project_form(project)
        wd.find_element_by_xpath("//div[3]/form/table/tbody/tr[7]/td/input").click()
        self.project_cache = None

    def delete_project_by_index(self, index):
        wd = self.app.wd
        self.open_project_page()
        wd.find_elements_by_xpath('//a[contains(@href,"manage_proj_edit_page.php?project_id=")]')[index].click()
        wd.find_element_by_xpath("//div[4]/form/input[3]").click()
        wd.find_element_by_xpath("//div[2]/form/input[4]").click()
        self.project_cache = None

    def delete_project_by_id(self, id):
        wd = self.app.wd
        self.open_project_page()
        wd.find_element_by_xpath('//a[contains(@href,"manage_proj_edit_page.php?project_id=%s")]' % id).click()
        wd.find_element_by_xpath("//div[4]/form/input[3]").click()
        wd.find_element_by_xpath("//div[2]/form/input[4]").click()
        self.project_cache = None


    def count(self):
        wd = self.app.wd
        self.open_project_page()
        return len(wd.find_elements_by_xpath('//table[3]/tbody/tr')[2:])

    project_cache = None

    def get_project_list(self):
        if self.project_cache is None:
            wd = self.app.wd
            self.open_project_page()
            self.project_cache = []
            i = 1
            for i in range(self.count()):
                wd.find_elements_by_xpath('//a[contains(@href,"manage_proj_edit_page.php?project_id=")]')[i].click()
                id = wd.find_element_by_xpath('//input[@name="project_id"]').get_attribute("value")
                name = wd.find_element_by_name("name").get_attribute("value")
                status = (wd.find_element_by_xpath('//select[@name="status"]//option[@selected="selected"]')).text
                if wd.find_element_by_xpath('//input[@name="inherit_global"]').is_selected():
                    inherit_global = "True"
                else:
                    inherit_global = "False"
                view_state = (wd.find_element_by_xpath('//select[@name="view_state"]//option[@selected="selected"]')).text
                description = wd.find_element_by_xpath('//textarea[@name="description"]').text
                self.project_cache.append(Project(id=id, name=name, status=status, inherit_global=inherit_global,
                                                  view_state=view_state, description=description))
                self.open_project_page()
                i = i + 1
        return list(self.project_cache)


