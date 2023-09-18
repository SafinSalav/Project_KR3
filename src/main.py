import json
from zipfile import ZipFile


def load_operations():
    '''
    Распаковка архива и загрузка json файла в данные data
    :return: данные data
    '''
    with ZipFile('../data/operations.zip', 'r') as myzip:
        myzip.extract('operations.json', path='../data')
    with open('../data/operations.json', encoding='utf-8') as file:
        data = json.load(file)
    return data


def input_information(dic):
    '''
    Вывод информации об операции
    :param dic: словарь операции
    '''
    try:
        list_from = list(dic['from'].split())
        from_ = ' '.join(list_from[:-1]) + f' {list_from[-1][:4]} {list_from[-1][4:6]}** **** {list_from[-1][-4:]} -> '#маска для счета отправителя
    except KeyError:
        from_ = ''

    list_to = list(dic['to'].split())
    to_ = ' '.join(list_to[:-1]) + f' **{list_to[-1][-4:]}'#маска для счета получателя

    print(f"""{dic['date'][:10]} {dic['description']}
{from_}{to_}
{dic['operationAmount']['amount']} {dic['operationAmount']['currency']['name']}
""")


def sort_date(operations):
    '''
    Сортировка данных о выполненных операциях по времени
    :param operations: данные об операциях
    :return: отсортированное  время
    '''
    date = []
    for i in operations:
        try:
            if i['state'] == 'EXECUTED':
                date.append(i['date'])
        except KeyError:
            pass
    date.sort(reverse=True)
    return date


def start():
    '''
    Вывод информации о пяти последних выполненных операциях
    '''
    operations = load_operations().copy()
    sorted_date = sort_date(operations).copy()
    count = 0
    while count < 5:
        for i in operations:
            try:
                if i['state'] == 'EXECUTED':
                    if i['date'] == sorted_date[count]:
                        input_information(i)
            except KeyError:
                pass
        count += 1


start()
