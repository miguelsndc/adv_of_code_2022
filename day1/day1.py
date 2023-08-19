def solve(data: list[str]):
    most_calories_elf = 0
    current_calories = 0
    rank = []

    for v in data:
        if v == '':
            if current_calories > most_calories_elf:
                most_calories_elf = current_calories
                rank.append(current_calories)

            current_calories = 0
            continue

        current_calories += int(v)

    top_three = 0

    for i in range(3):
        top_three += max(rank)
        rank.remove(max(rank))

    print(top_three)


with open('./input.txt') as file:
    values = file.read().split('\n')
    solve(values)



