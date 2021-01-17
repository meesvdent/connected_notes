"""
models for the connected notes program

warning, this commit was written while halfway into my third gt



So what we should do?

First I just want to make a class which stores my notes.
It should store:
    * Notes
    * Note numbersss
    * Nothing more? Connections are saved in a database?
    * What's right here? Adding it to my let's find out list

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
    That's it
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


class Connection():
    """
    Stores connections
    Adds connections
    """

    def __init__(self, from_node, to_node):
        self.from_node = from_node
        self.to_node = to_node

    def __repr__(self):
        return str(self.from_node) + " -> " + str(self.to_node)

    def connection_type(self):
        connection_type = (
                self.from_node.node_type +
                " -> " +
                self.to_node.node_type
                )
        return connection_type
