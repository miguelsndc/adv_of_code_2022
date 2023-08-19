# def read_input():
#     with open("./input.txt") as file:
#         return file.read().strip().split('\n')
#
#
# data = read_input()
# both = []
#
# for s in data:
#     mid = len(s) // 2
#     first_half, second_half = (s[:mid], s[mid:])
#     result = set(first_half).intersection(second_half)
#     both.append(*result)
#
#
# def get_priority(s: str):
#     return 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'.find(s) + 1
#
#
# priority_list = map(get_priority, both)
# p_sum = sum(priority_list)
# print(p_sum)


# ______--- PART TWO _____________

def read_input():
    with open("./input.txt") as file:
        return file.read().strip().split('\n')


def get_priority(s: str):
    return 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'.find(s) + 1


data = read_input()
subgroups_size = 3
priority_list = []

for i in range(0, len(data), subgroups_size):
    group = data[i: i + subgroups_size]
    common = set(group[0]) & set(group[1]) & set(group[2])
    priority = get_priority(*common)
    priority_list.append(priority)

print(sum(priority_list))



