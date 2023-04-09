import json

def read_file(path):
    with open(path, "r", encoding="utf-8") as json_file:
        note_dct = json.load(json_file)
    return note_dct

def read_all_notes(path):
    note_dct = read_file(path)
    for key in note_dct:
        print(f"Заметка № {key}.")
        print(f'Дата созднания: {note_dct[key][0]["data"]}')
        print(f'Название: {note_dct[key][1]["title"]}')
        print(f'Текст: {note_dct[key][2]["text"]}')
        print()

def read_one_note(path, note_number):
    note_dct = read_file(path)
    print(f"Заметка № {note_number}.")
    print(f'Дата созднания: {note_dct[note_number][0]["data"]}')
    print(f'Название: {note_dct[note_number][1]["title"]}')
    print(f'Текст: {note_dct[note_number][2]["text"]}')
    print()