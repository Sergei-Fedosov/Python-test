from Checker import check_file
from Reading import read_file
from Saving import Saving


def sort_note(path, order=True):
    if not check_file(path):
        print("Нет заметок для сортировки")
    else:
        note_dct = read_file(path)
        key_list = [key for key in note_dct]
        value_list = [note_dct[key] for key in note_dct]
        if order:
            for i in range(len(value_list)):
                for j in range(i + 1, len(value_list)):
                    if value_list[i][0]["data"][-4:] > value_list[j][0]["data"][-4:]:
                        value_list[i], value_list[j] = value_list[j], value_list[i]
        else:
            for i in range(len(value_list)):
                for j in range(i + 1, len(value_list)):
                    if value_list[i][0]["data"][-4:] < value_list[j][0]["data"][-4:]:
                        value_list[i], value_list[j] = value_list[j], value_list[i]
        sorted_dct = {}
        for key, value in zip(key_list, value_list):
            sorted_dct[key] = value
        save = Saving(sorted_dct)
        save.saving_note()
        return sorted_dct