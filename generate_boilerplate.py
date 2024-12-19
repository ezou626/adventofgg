import os, shutil
from config import _ROOT_PATH, _INPUT_PATH

def generate_day(day: int):
    formatted_day = str(day).zfill(2)
    # inputs
    if not os.path.exists(_INPUT_PATH):
        os.mkdir(_INPUT_PATH)
    if not os.path.exists(_INPUT_PATH / f'p{formatted_day}'):
        os.mkdir(_INPUT_PATH / f'p{formatted_day}')
    if not os.path.exists(_INPUT_PATH / f'p{formatted_day}/input.txt'):
        with open(_INPUT_PATH / f'p{formatted_day}/input.txt', 'w') as f:
            f.write('')
    if not os.path.exists(_INPUT_PATH / f'p{formatted_day}/tc.txt'):
        with open(_INPUT_PATH / f'p{formatted_day}/tc.txt', 'w') as f:
            f.write('')

    # code
    if not os.path.exists(_ROOT_PATH / f'p{formatted_day}.py'):
        shutil.copy(_ROOT_PATH / 'template.py', _ROOT_PATH / f'p{formatted_day}.py')

if __name__ == '__main__':
    for i in range(1, 32):
        generate_day(i)
