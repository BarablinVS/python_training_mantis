from model.project import Project
import random
from random import randrange

__author__ = 'viktor'


def test_delete_project(app):
    if app.project.count() == 0:
        app.project.create(Project(name="TestProject28", status="obsolete", inherit_global="X", view_state="public",
                      description="Hello2"))
    old_projects = app.project.get_project_list()
    index = randrange(len(old_projects))
    app.project.delete_project_by_index(index)
    new_projects = app.project.get_project_list()
    assert len(old_projects) - 1 == len(new_projects)
    old_projects[index:index + 1] = []
    assert old_projects == new_projects


def test_delete_project_by_id(app):
    if app.project.count() == 0:
        app.project.create(Project(name="TestProject29", status="obsolete", inherit_global="X", view_state="public",
                      description="Hello2"))
    old_projects = app.project.get_project_list()
    project = random.choice(old_projects)
    app.project.delete_project_by_id(project.id)
    new_projects = app.project.get_project_list()
    assert len(old_projects) - 1 == len(new_projects)
    old_projects.remove(project)
    assert old_projects == new_projects
