sul = []
def find_common_participants(str0, str1,sep =','):
    sul=list(set(str0.split('|')) & set(str1.split('|')))
    sul == sul.sort()
    return sul


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"


print(find_common_participants(participants_first_group, participants_second_group, ','))
