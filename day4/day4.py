# def read():
#     with open('./input.txt') as file:
#         return list(map(lambda x: x.split(','), file.read().strip().split('\n')))
#
#
# def gen_range(pair):
#     pair_int = tuple(map(lambda x: int(x), pair.split('-')))
#     return [i for i in range(pair_int[0], pair_int[1] + 1)]
#
#
# pairs = read()
#
# count = 0
# for pair in pairs:
#     first_range, second_range = gen_range(pair[0]), gen_range(pair[1])
#
#     if set(first_range).issuperset(second_range) or set(first_range).issubset(second_range):
#         count += 1
#
# print(count)


#_____ PART TWO _______


def read():
    with open('./input.txt') as file:
        return list(map(lambda x: x.split(','), file.read().strip().split('\n')))


def gen_range(pair):
    pair_int = tuple(map(lambda x: int(x), pair.split('-')))
    return [i for i in range(pair_int[0], pair_int[1] + 1)]


pairs = read()

count = 0
for pair in pairs:
    first_range, second_range = gen_range(pair[0]), gen_range(pair[1])

    if set(first_range) & set(second_range):
        count += 1

print(count)
