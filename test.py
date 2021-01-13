"""
come on, let's try to write a proper test this time
let me just do something real quick
"""


from models import Note, Theme, Connection


def test_notes():
    print("testing new notes")
    first_note = Note("hello_world")
    second_note = Note("goodbye_world")
    assert str(first_note) == "hello_world", "Should be hello_wolrd"
    print("new notes added succesfully")
    return [first_note, second_note]


def test_themes():
    print("testing new themes")
    test_theme = Theme("testing")
    assert str(test_theme) == "testing", "Should be testing"
    print("new theme added succesfully")


def test_connections(test_notes):
    print("testing new connections")
    first_note = test_notes[0]
    second_note = test_notes[1]
    first_connection = Connection(first_note, second_note)
    assert str(first_connection) == "hello_world -> goodbye_world", (
        "Shoulb be hello_world -> goodbye world"
        )
    assert str(first_connection.connection_type()) == "note -> note", (
        "Should be note -> note"
        )
    print("new connections added succesfully")


if __name__ == "__main__":
    test_notes = test_notes()
    test_connections(test_notes)
    test_themes()
    print("\nall tests passed")
