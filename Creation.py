import datetime
from Reading import read_file
from Checker import check_file


class Creation:
    def __init__(self, title, text):
        self.title = title
        self.text = text

    def note(self):
        if not check_file("note.json"):
            note_dct = {}
            number = 0
        else:
            note_dct = read_file("note.json")
            number = len(note_dct)
        data = datetime.datetime.today().strftime("%m/%d/%Y")
        number += 1
        note_dct[number] = []
        note_dct[number].append({"data": data})
        note_dct[number].append({"title": self.title})
        note_dct[number].append({"text": self.text})
        return note_dct


if __name__ == "__main__":
    note = Creation("первая заметка", "тело заметки")
    print(note.note())