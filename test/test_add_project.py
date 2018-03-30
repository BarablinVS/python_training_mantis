from model.project import Project


def test_login(app):
    username = "administrator"
    password = "root"
    app.session.login(username, password)
    old_projects = app.soap.get_projects(username, password)
    project = Project(name="Test1", status="obsolete", inherit_global="False", view_state="public",
                      description="Hello2")
    app.project.create(project)
    assert len(old_projects) + 1 == len(app.soap.get_projects(username, password))
    new_projects = app.soap.get_projects(username, password)
    old_projects.append(project)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)