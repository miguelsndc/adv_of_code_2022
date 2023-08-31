def read_input():
    with open('input.txt') as f:
        return f.read()


input = read_input()


def detect_marker(string: str, step=4):
    for i in range(0, len(string)):
        substring = string[i: i + step]
        if len(set(substring)) == len(substring):
            return len(string[:i + step])

    return -1


def first_task(input: str):
    return detect_marker(input, step=4)


def second_task(input: str):
    return detect_marker(input, step=14)


print(first_task(input))