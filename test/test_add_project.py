from model.project import Project

def test_login(app):
    app.session.login("administrator", "root")
    old_projects = app.project.get_project_list()
    project = Project(name="Test Project6", status="stable", inherit_global="not_check", view_state="private",
                      description="3432rwgfsg344gtw")
    app.project.create(project)
    assert len(old_projects) + 1 == app.project.count()
    new_projects = app.project.get_project_list()
    old_projects.append(project)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)