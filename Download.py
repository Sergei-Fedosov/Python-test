from Checker import check_file
from Reading import read_file
import json
def download_notes(path):

    if check_file(path):
        note_dct = read_file(path)
        with open("downloads.json", "w", encoding="utf-8") as file:
            json.dump(note_dct, file, indent=4)
        print("Записи выгружены в файл 'downloads.json'")
    else:
        print("Нет записей для загрузки")