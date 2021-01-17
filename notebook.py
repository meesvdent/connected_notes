from editor import get_user_input
from models import Note, Theme, Connection


class Notebook():

    def __init__(self):
        self.components = []
        self.connections = []

    def __repr__(self):
        return ("Components: " + str(self.components) + "\n" +
                "Connections: " + str(self.connections))

    def add_note(self, raw):
        new_note = Note(raw)
        self.components.append(new_note)

    def add_theme(self, raw):
        new_theme = Theme(raw)
        self.components.append(new_theme)

    def add_connection(self, a, b):
        if not (a in self.components and b in self.components):
            return "adding not possible"
        new_connection = Connection(a, b)
        self.connections.append(new_connection)
