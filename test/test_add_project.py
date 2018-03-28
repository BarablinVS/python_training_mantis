from model.project import Project


def test_login(app):
    old_projects = app.project.get_project_list()
    project = Project(name="TestProject27", status="obsolete", inherit_global="X", view_state="public",
                      description="Hello2")
    app.project.create(project)
    assert len(old_projects) + 1 == app.project.count()
    new_projects = app.project.get_project_list()
    old_projects.append(project)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)