from Saving import Saving
from Checker import check_file
from Reading import read_file, read_one_note


def editing_note(path):
    if not check_file(path):
        print("Нет заметок для редактирования")
    else:
        note_dct = read_file(path)
        note_number = input("Введите номер заметки, которую хотите изменить: ")
        key_list = [key for key in note_dct]
        if note_number in key_list:
            read_one_note(path, note_number)
            note_name = input("Введите название заметки(enter - оставить без изменений): ")
            if note_name != "":
                note_dct[note_number][1]['title'] = note_name
            content_name = input("Введите текст заметки(enter - оставить без изменений): ")
            if content_name != "":
                note_dct[note_number][2]['text'] = content_name
            save = Saving(note_dct)
            save.saving_note()
        else:
            print("Такой заметки не существует. Попробуйте снова")