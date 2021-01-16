from editor import get_user_input
from models import Note


class Notebook():

    def __init__(self):
        self.components = []
        self.connections = []

    def add_note(self):
        raw = get_user_input()
        new_note = Note(raw)
        self.components.append(new_note)
