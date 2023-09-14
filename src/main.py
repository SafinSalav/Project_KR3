import json
from zipfile import ZipFile


def load_operations():
    '''
    Распаковка архива и загрузка json файла в данные data
    :return: данные data
    '''
    with ZipFile('C:/Users/Lenovo/PycharmProjects/Project_KR3/data/operations.zip', 'r') as myzip:
        myzip.extract('operations.json', path='C:/Users/Lenovo/PycharmProjects/Project_KR3/data')
    with open('C:/Users/Lenovo/PycharmProjects/Project_KR3/data/operations.json', encoding='utf-8') as file:
        data = json.load(file)
    return data


def input_information(dic):
    '''
    Вывод информации об операции
    :param dic: словарь операции
    '''
    try:
        A = list(dic['from'].split())
        from_ = ' '.join(A[:-1]) + f' {A[-1][:4]} {A[-1][4:6]}** **** {A[-1][-4:]} -> '
    except KeyError:
        from_ = ''
    B = list(dic['to'].split())
    to_ = ' '.join(B[:-1]) + f' **{B[-1][-4:]}'
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
