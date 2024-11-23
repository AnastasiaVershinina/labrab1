import json #импорт формата json

def task(file_name): #создание функции
    with open(file_name) as dict:#для каждого словаря в файле
        return sum([element['score']*element['weight'] for element in json.load(dict)])#значение суммы произведений в каждом словаре


print('%.3f' % task('input.json'))#вывод с округлением до 3 знаков после запятой полученной суммы
