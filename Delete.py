from Checker import check_file
from Reading import read_file

def del_note(path):

    if check_file(path):
        note_number = input("Введите номер заметки, которую нужно удалить: ")
        note_dct = read_file(path)
        key_list = [key for key in note_dct]
        if note_number in key_list:
            del note_dct[note_number]
            print("Заметка удалена")
    else:
        print("Нет заметок для удаления")

    return note_dct