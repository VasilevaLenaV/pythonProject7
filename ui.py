# Пользовательский интерфейс
import crud
import module_import as import_data
import module_export as export_data

print('\nТелефонный справочник')


def ls_menu():
    while True:
        print('\nМЕНЮ')
        print('1. Все контакты.')
        print('2. Добавить новый контакт.')
        print('3. Поиск контакта')
        print('4. Импорт контактов')
        print('5. Эскпорт контактов')
        print('0. Выход.\n')
        n = сhecking_the_number(input('Выберите пункт меню: '))

        if n == 0:
            break

        elif n == 4:
            import_data.import_from_csv()

        elif n == 5:
            export_data.export_to_csv()

        elif n == 1:
            contacts = crud.all_contact()
            [print(f"\n{contact['surname']} {contact['name']}") for contact in contacts]

        elif n == 2:
            result = crud.add_contact(get_contact())
            if result != "":
                print(result)

        elif n == 3:
            search_result = crud.search_contact(get_contact())
            len_search_data = len(search_result)

            print(f"Найдено записей: {len_search_data}")

            if len_search_data == 0:
                continue

            print(f"Найдено записей: {len_search_data}")
            [print(f"\nID= {cc.doc_id}"
                   f"\nПолное имя= {cc['surname']} {cc['name']}"
                   f"\nТелефон:{cc['number']}"
                   f"\nЭлектронная почта:{cc['email']}\n")
             for cc in search_result]

            select_contact = 0

            if len_search_data > 1:
                select_input = input(f"\nВыберите ID контакта: ")
                if not crud.is_int(select_input):
                    print(f"Некорректный ввод")
                    continue

                select_contact = int(select_input)
            else:
                select_contact = search_result[0].doc_id

            print('1. Изменить контакт.')
            print('2. Удалить контакт.')
            print('0. Выход.')

            change = сhecking_the_number(input('Введите номер пункта: '))

            if change == 0:
                continue
            elif change == 1:
                change_contact = crud.get_contact_by_id(select_contact)

                if len(change_contact) == 0:
                    print("Не верно указанный ID")
                    continue

                crud.change_contact(select_contact, get_change_contact(change_contact))
            elif change == 2:
                crud.delete_contact(select_contact)
            else:
                print('\nТакого пункта меню не существует.\nВведите цифру, соответствующую пункту меню.')

        else:
            print(
                '\nТакого пункта меню не существует.\nВведите цифру, соответствующую пункту меню.')


def get_change_contact(change_):
    if len(change_) == 0:
        return
    old_number = ""
    old_email = ""
    name = input(f"Введите имя [{change_['name']}]: ")
    surname = input(f"Введите фамилию [{change_['surname']}]: ")
    change_tel = input(f"Добавить(Y),Изменить(N) номер телефона: ")
    if change_tel == 'N':
        old_number = input(f"Введите номер телефона который нужно изменить: ")
    number = input(f"Введите новый номер телефона: ")

    change_email = input(f"Добавить(Y),Изменить(N) электронную почту: ")
    if change_email == 'N':
        old_email = input(f"Введите электронную почту который нужно изменить: ")
    email = input(f"Введите новую электронную почту: ")

    return name, surname, number, old_number, email, old_email


def get_contact():

    name = input('Введите имя: ')
    surname = input('Введите фамилию: ')
    number = input('Введите номер телефона: ')
    email = input('Введите электронную почту: ')

    return name, surname, number, email


def сhecking_the_number(arg):
    while not arg.isdigit():
        print('\nВы ввели не число.')
        arg = input('Введите соответствующий пункт меню: ')
    return int(arg)
