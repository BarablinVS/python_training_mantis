__author__ = 'viktor'

from model.project import Project


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
        if text == "check":
            pass
        elif text == "not_check":
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
            for element in wd.find_elements_by_xpath('//table[3]/tbody/tr')[2:]:
                columns = (element.text).split(' ')
                name = columns[0]
                status = columns[1]
                inherit_global = columns[2]
                view_state = columns[3]
                description = columns[4]
                id = (element.find_element_by_css_selector('a').get_attribute("href")).\
                    replace("http://localhost/mantisbt-1.2.20/manage_proj_edit_page.php?project_id=", "")
                self.project_cache.append(Project(id=id, name=name, status=status, inherit_global=inherit_global,
                                                  view_state=view_state, description=description))
        return list(self.project_cache)


