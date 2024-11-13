numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
del numbers[4]
sred=sum(numbers)/len(numbers)
numbers.insert(4,sred)
print(numbers)