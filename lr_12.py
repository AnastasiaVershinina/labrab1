numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
numbers.pop(4) #удаление элемента None из списка
summ = sum(numbers)
number_of_elements = len(numbers)+1
average_value = summ/number_of_elements
numbers.insert(4, average_value) #вставление среднего значения в список
print('Измененный список:', numbers)
