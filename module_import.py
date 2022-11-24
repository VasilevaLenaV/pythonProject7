# Импорт данных в телефонный справочник
import crud

def import_from_csv():
    file = open("import.csv", 'r')
    for str_row in file:
        data_to_import = str_row.replace("\n", "").split(";")
        crud.add_contact(data_to_import)
    file.close()

    print(f"Импорт завершен")
