from model.project import Project
import random
from random import randrange

__author__ = 'viktor'


def test_delete_project(app):
    username = "administrator"
    password = "root"
    app.session.login(username, password)
    if len(app.soap.get_projects(username, password)) == 0:
        app.project.create(Project(name="TestProject28", status="obsolete", inherit_global="X", view_state="public",
                      description="Hello2"))
    old_projects = app.soap.get_projects(username, password)
    index = randrange(len(app.soap.get_projects(username, password)))
    app.project.delete_project_by_index(index)
    new_projects = app.soap.get_projects(username, password)
    assert len(old_projects) - 1 == len(app.soap.get_projects(username, password))
    old_projects[index:index + 1] = []
    assert old_projects == new_projects


def test_delete_project_by_id(app):
    username = "administrator"
    password = "root"
#    app.session.login(username, password)
    if len(app.soap.get_projects(username, password)) == 0:
        app.project.create(Project(name="TestProject29", status="obsolete", inherit_global="X", view_state="public",
                      description="Hello2"))
    old_projects = app.soap.get_projects(username, password)
    project = random.choice(old_projects)
    app.project.delete_project_by_id(project.id)
    new_projects = app.soap.get_projects(username, password)
    assert len(old_projects) - 1 == len(new_projects)
    old_projects.remove(project)
    assert old_projects == new_projects
