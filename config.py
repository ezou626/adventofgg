from pathlib import Path
import os, re, sys

_ROOT_PATH = Path(__file__).parent
_INPUT_PATH = _ROOT_PATH / 'inputs'

def _get_problem() -> str:
    fname = os.path.basename(sys.argv[0])
    candidate_number = re.search(r'p\d+', fname)
    return candidate_number.group()

def get_input() -> list[str]:
    day = _get_problem()
    with open(_INPUT_PATH / f'{day}/input.txt', 'r') as f:
        return f.readlines()
    
def get_tc() -> list[str]:
    day = _get_problem()
    with open(_INPUT_PATH / f'{day}/tc.txt', 'r') as f:
        return f.readlines()
    
def run_solution(process_input, part1_solution, part2_solution, skip_actual = False) -> None:
    print(f'\nDay {_get_problem()[1:]}')
    cases = [('TEST', get_tc)]
    if not skip_actual:
        cases.append(('ACTUAL', get_input))
    for label, reader in cases:
        print(f'\n{label}:')
        processed_lines = None
        try:
            input = reader()
            if not input:
                raise EOFError()
            processed_lines = process_input(input)
        except FileNotFoundError:
            print(f'File not found for {label}')
            continue
        except EOFError:
            print(f'File is empty for {label}')
            continue
        except NotImplementedError:
            print('Input processing not implemented')
        if not processed_lines:
            print('Run failed')
            continue
        try:
            print('P1:', part1_solution(*processed_lines))
        except NotImplementedError:
            print('P1: Not implemented')
        try:
            print('P2:', part2_solution(*processed_lines))
        except NotImplementedError:
            print('P2: Not implemented')