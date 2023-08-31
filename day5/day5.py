def read_input():
    with open('input.txt') as f:
        return f.read()


data = read_input()


def first_solver(args: str):
    stack, movements = args.split('\n\n')
    raw_column, *instructions = stack.split('\n')[::-1]
    columns_amount = (len(raw_column) + 1) // 4
    stacks = [[] for _ in range(0, columns_amount + 1)]

    for line in instructions:
        for i, box in enumerate(line[1::4]):
            if box != ' ':
                stacks[i + 1] += box

    for line in movements.split('\n'):
        _, amount, _, src, _, dest = line.split(' ')
        amount = int(amount)
        src = int(src)
        dest = int(dest)
        for i in range(amount):
            val = stacks[src].pop()
            stacks[dest] += val

    result = "".join([stack[-1] for stack in stacks if len(stack)])

    return result


def second_solver(args: str):
    stack, movements = args.split('\n\n')
    raw_column, *instructions = stack.split('\n')[::-1]
    columns_amount = (len(raw_column) + 1) // 4
    stack_matrix = [[] for _ in range(0, columns_amount + 1)]

    for line in reversed(instructions):
        for i, box in enumerate(line[1::4]):
            if box != ' ':
                stack_matrix[i + 1] += box

    for line in movements.split('\n'):
        _, amount, _, src, _, dest = line.split(' ')
        amount = int(amount)
        src = int(src)
        dest = int(dest)

        part, stack_matrix[src] = stack_matrix[src][:amount], stack_matrix[src][amount:]
        stack_matrix[dest] = [*part, *stack_matrix[dest]]

    result = "".join([stack[0] for stack in stack_matrix if len(stack)])

    return result


def first_task(input: str):
    return first_solver(input)


def second_task(input: str):
    return second_solver(input)


print(second_solver(data))
