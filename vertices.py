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
        self.tags = None
        self.connected_notes = None
        self.tags = []

    def _parse_note(self):
        raw = self.content
        if self.tags == None:
            self.tags = list(self._parse_tags())
        if self.connected_notes == None:
            self.connected_notes = list(self._parse_connected_notes())

    def _parse_tags(self):
        unparsed = self.content
        while parse_complete == False:
            if tagsymbol not in unparsed:
                parse_complete = True
            unparsed = unparsed.split(tagsymbol, 1)[1]
            new_tag = unparsed.split(" ", 1)[0]
            self.tags.append(new_tag)


    def _parse_connected_notes(self):
        pass


class Theme(Node):
    """
    A theme is one or a couple of words
    A note can be connected to a theme
    Themes can be connected to each other
    """

    def __init__(self, theme):
        self.content = theme
        self.node_type = "theme"


