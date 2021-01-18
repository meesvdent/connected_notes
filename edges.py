"""
Contains the classes which store connections
"""


class Edge():
    """
    Stores connections
    """

    def __init__(self, from_node, to_node, orientation):
        self.from_node = from_node
        self.to_node = to_node
        self.orientation = orientation

    def __repr__(self):
        arrow = self._get_arrow()
        return str(self.from_node) + arrow + str(self.to_node)

    def _get_arrow(self):
        if self.orientation == "undirected":
            arrow = " <-> "
        elif self.orientation == "directed":
            arrow = " -> "
        return arrow

    def connection_type(self):
        arrow = self._get_arrow()
        connection_type = (
            self.from_node.node_type +
            arrow +
            self.to_node.node_type
        )
        return connection_type

