stack = ['#']

symbol_dict = {
    'S': 0,
    'X': 1,
    'Y': 2,
    'Z': 3,
    'A': 4,
    'B': 5,
    'C': 6,
    'a': 7,
    'b': 8,
    'c': 9,
    '#': 10
}

rules_dict = {
    'XYZ': 'S',
    'XZ': 'S',
    'aA': 'A',
    'a': 'A',
    'bB': 'B',
    'b': 'B',
    'cC': 'C',
    'c': 'C',
    'A': 'X',
    'B': 'Y',
    'C': 'Z'
}

precedence_matrix = [
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '>'],
    [' ', ' ', '=', '=', ' ', '<', '<', ' ', '<', '<', '>'],
    [' ', ' ', ' ', '=', ' ', ' ', '<', ' ', ' ', '<', '>'],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '>'],
    [' ', ' ', '>', '>', ' ', '>', '>', ' ', '>', '>', '>'],
    [' ', ' ', ' ', '>', ' ', ' ', '>', ' ', ' ', '>', '>'],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '>'],
    [' ', ' ', '>', '>', '=', '>', '>', '<', '>', '>', '>'],
    [' ', ' ', ' ', '>', ' ', '=', '>', ' ', '<', '>', '>'],
    [' ', ' ', ' ', ' ', ' ', ' ', '=', ' ', ' ', '<', '>'],
    ['<', '<', '<', '<', '<', '<', '<', '<', '<', '<', ' ']
]

lang_line = input('Enter line for validation: ')
lang_line += '#'
expr_stack = []
i = 0

while i < len(lang_line):
    cur_symb = lang_line[i]
    if stack == ['#', 'S']:
        print('Line is valid')
        break
    cur_relation = precedence_matrix[symbol_dict[stack[-1]]][symbol_dict[cur_symb]]
    if cur_relation == '<' or cur_relation == '=':
        stack.append(cur_symb)
        i += 1
        continue
    elif cur_relation == '>':
        while cur_relation != '<':
            expr_stack.append(stack.pop())
            cur_relation = precedence_matrix[symbol_dict[stack[-1]]][symbol_dict[expr_stack[-1]]]
        expr_stack.reverse()
        expr_str = ''.join(expr_stack)
        if expr_str not in rules_dict:
            print('Line is invalid')
            break
        else:
            stack.append(rules_dict[expr_str])
            expr_stack = []
    else:
        print('Line is invalid')
        break
