from editor import get_user_input
from vertices import Note, Theme
from edges import Edge


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

    def add_directed_connection(self, a, b):
        if not (a in self.components and b in self.components):
            return "adding not possible"
        new_connection = Edge(a, b, "directed")
        self.connections.append(new_connection)


    def add_undirected_edge(self, a, b):
        if not (a in self.components and b in self.components):
            return "adding not possible"
        new_connection = Edge(a, b, "undirected")
        self.connections.append(new_connection)



