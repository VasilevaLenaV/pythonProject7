# Операции обработки данных
# Создание, Чтение, Изменение, Удаление

from tinydb import TinyDB, Query

global db
db = TinyDB('db.json', ensure_ascii=False, encoding='utf-8')
contacts = db.table("Contacts")
query = Query()


def init_db():
    db.table("Contacts")


def get_contact_by_id(id):
    return contacts.get(doc_id=id)


def change_contact(contactid,cdata):
    cct =get_contact_by_id(contactid)

    if len(cdata) == 0:
        return

    name =cct["name"]
    surname =cct["surname"]

    if name !=cdata["name"]:
        name =cdata["name"]
    if surname !=cdata["surname"]:
        surname =cdata["surname"]

    numbers = cct["number"]

    if cdata[3] == "":
        numbers.append(cdata[2])
    else:
        numbers = list(map(lambda x: x.replace(cdata[3], cdata[2]), numbers))

    emails = cct["email"]

    if cdata[5] == "":
        emails.append(cdata[4])
    else:
        emails = list(map(lambda x: x.replace(cdata[5], cdata[4]), emails))

    contacts.update({"name": name, "surname": surname, "number": numbers, "email": emails}, doc_ids=contactid)


def add_contact(data):
    contact = {"name": data[0], "surname": data[1], "number": [data[2]], "email": [data[3]]}
    if contacts.contains(query.name == data[0]):
        return f"!! Контакт уже существует !!"

    contacts.insert(contact)


def all_contact():
    return contacts.all()


digits = lambda y: list(int(a) for a in list(y) if is_int(a))


def delete_contact(list_input):
    if list_input == "":
        return

    list_split = str(list_input).split(',')
    ids = digits(list(list_split))
    contacts.remove(doc_ids=ids)


def is_int(c):
    try:
        int(c)
        return True
    except ValueError:
        return False


list_contains = lambda value, search: search in value


def search_contact(search_data):

    return list(contacts.search(
        (query.name == search_data[0])
        | (query.surname == search_data[1])
        | query.number.test(list_contains, search_data[2])
        | query.email.test(list_contains, search_data[3]))
    )
