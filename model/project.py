__author__ = 'viktor'


class Project:
    def __init__(self, name=None, status="development", inherit_global=None, view_state="public", description=None):
        self.name = name
        self.status = status
        self.inherit_global = inherit_global
        self.view_state = view_state
        self.description = description
        self.id = id

#    def __repr__(self):
#        return "%s:%s:%s:%s" % (self.id, self.name, self.header, self.footer)

#    def __eq__(self, other):
#       return (self.id is None or other.id is None or self.id == other.id) and self.name == other.name