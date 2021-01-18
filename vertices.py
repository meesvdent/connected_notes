"""
models for the connected notes program

"""


class Node():
    """
    Parent class for nodes
    Stores their identity
    """

    def __init__(self, identity, node_type):
        self.content = identity
        self.node_type = self.node_type

    def __repr__(self):
        return (
            self.node_type + ": " + self.content
            )

    def __str__(self):
        return self.content


class Note(Node):
    """
    Stores notes
    """

    def __init__(self, note):
        self.content = note
        self.node_type = "note"


class Theme(Node):
    """
    A theme is one or a couple of words
    A note can be connected to a theme
    Themes can be connected to each other
    """

    def __init__(self, theme):
        self.content = theme
        self.node_type = "theme"


