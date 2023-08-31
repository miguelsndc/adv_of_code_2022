import os
import sys
from textwrap import indent

_, *args = sys.argv


def parse(args: list[str]):
    name = args[0]
    parent_directory = os.getcwd()
    new_dir = os.path.join(parent_directory, name)

    try:
        os.mkdir(new_dir)
    except FileExistsError:
        print('A directory with the given name already exists.')
        while True:
            should_write = (input('Should generate new files in this directory ? (Will exclude all files) (y/n): ')
                            .strip().lower())

            if should_write == 'y':
                for file in os.scandir(new_dir):
                    os.remove(file.path)
                break
            elif should_write == 'n':
                exit(1)
            else:
                print("Please write a valid answer")
                continue

    def ind(text: str, level: int):
        return indent(text, ' ' * (level * 4))

    with open(os.path.join(new_dir, f"{name}.py"), 'w') as f:
        f.writelines([
            "def read_input():\n",
            ind("with open('input.txt') as f:\n", 1),
            ind("return f.read()\n", 2),
            '\n\n',
            'data = read_input()\n',
            '\n\n',
            'def solver(args):\n',
            ind("pass\n", 1),
            '\n\n',
            'def first_task(input: str):\n',
            ind('return solver(input)\n', 1),
            '\n\n',
            'def second_task(input: str):\n',
            ind('pass\n', 1),
            '\n\n',
        ])

    open(os.path.join(new_dir, "input.txt"), 'x')


parse(args)
