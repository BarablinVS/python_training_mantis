from model.project import Project

def test_login(app):
    app.session.login("administrator", "root")
    project = Project(name="Test Project", status="stable", inherit_global="not_check", view_state="private", description="3432rwgfsg344gtw")
    app.project.create(project)