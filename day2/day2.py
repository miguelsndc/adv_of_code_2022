# _______________ FIRST QUESTION ______________
# def read_input():
#     with open('./input.txt') as file:
#         return list(map(lambda x: x.split(' '), file.read().strip().split('\n')))
#
#
# data = read_input()
#
# opponent_possible_choices = {
#     'A': 'Rock',
#     'B': 'Paper',
#     'C': 'Scissors'
# }
#
# player_possible_choices = {
#     'X': 'Rock',
#     'Y': 'Paper',
#     'Z': 'Scissors'
# }
#
# score_per_choice = {
#     'Rock': 1,
#     'Paper': 2,
#     'Scissors': 3
# }
#
# points_per_outcome = {
#     'lost': 0,
#     'draw': 3,
#     'win': 6
# }
#
# win_conditions = {
#     'Rock': 'Scissors',
#     'Paper': 'Rock',
#     'Scissors': 'Paper'
# }
#
# final_score = 0
#
# for match in data:
#     opponent = opponent_possible_choices[match[0]]
#     player = player_possible_choices[match[1]]
#
#     if player == opponent:
#         final_score += points_per_outcome['draw'] + score_per_choice[player]
#         continue
#
#     if win_conditions[player] == opponent:
#         final_score += points_per_outcome['win'] + score_per_choice[player]
#     else:
#         final_score += points_per_outcome['lost'] + score_per_choice[player]
#
# print(final_score)


def read_input():
    with open('./input.txt') as file:
        return list(map(lambda x: x.split(' '), file.read().strip().split('\n')))


data = read_input()

map_input = {
    'A': 'Rock',
    'B': 'Paper',
    'C': 'Scissors',
    'X': 'lost',
    'Y': 'draw',
    'Z': 'win'
}

score_per_choice = {
    'Rock': 1,
    'Paper': 2,
    'Scissors': 3
}

points_per_outcome = {
    'lost': 0,
    'draw': 3,
    'win': 6
}

final_score = 0

for round in data:
    opponent = map_input[round[0]]
    goal = map_input[round[1]]

    if (opponent, goal) in [('Rock', 'draw'), ('Paper', 'lost'), ('Scissors', 'win')]:
        final_score += points_per_outcome[goal] + score_per_choice['Rock']
    elif (opponent, goal) in [('Rock', 'win'), ('Paper', 'draw'), ('Scissors', 'lost')]:
        final_score += points_per_outcome[goal] + score_per_choice['Paper']
    else:
        final_score += points_per_outcome[goal] + score_per_choice['Scissors']

print(final_score)