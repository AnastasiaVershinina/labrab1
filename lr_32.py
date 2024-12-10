sul = []
def find_common_participants(strr0, strr1,sep =','):
    for i in strr0.split("|"):
        if i in strr1:
            sul.append(i)
            sul == sul.sort()
    return sul


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"


print(find_common_participants(participants_first_group, participants_second_group, ','))
