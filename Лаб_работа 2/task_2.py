# TODO Напишите функцию find_common_participants
def find_common_participants(participants_group_one,participants_group_two):
    participants_group_one = participants_group_one.split('|')
    participants_group_two = participants_group_two.split('|')
    participants = set(participants_group_one).intersection(participants_group_two)
    participants = sorted(participants)
    return participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group,participants_second_group))