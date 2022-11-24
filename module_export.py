#Экспорт данных из телефонного справочника
import crud
import csv

def export_to_csv():
    data =crud.all_contact()

    with open('export.csv', 'w', newline='', encoding='utf-8') as f:
        for x in data:
            writer = csv.writer(f, delimiter=';')

#            writer = csv.writer(f, delimiter=';',quotechar='|', quoting=csv.QUOTE_MINIMAL)
            writer.writerow([x['name'], x['surname'],str.join(",", x['number']),str.join(",",x['email']).replace("\n","")])


    print(f"Экспорт завершен")
