import json #импорт модуля json
from csv import DictReader #импорт считывания словаря
INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    lst = [] #создание пустого словаря
    with open(INPUT_FILENAME, 'r', newline="") as csv_file: #открываем исходный файл
        rd = DictReader(csv_file) #считывание строки
        for rww in rd:
            lst.append(rww) #добавление значения в словарь
    with open(OUTPUT_FILENAME, 'w') as json_file: #записываем в конечный файл формата json
        json.dump(obj=lst, fp=json_file, indent=4) #печать строки с отступами=4

if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
