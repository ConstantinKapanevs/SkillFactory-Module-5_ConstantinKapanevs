import random

grid = [[' ', '1', '2', '3'],
        ['1', '-', '-', '-'],
        ['2', '-', '-', '-'],
        ['3', '-', '-', '-']]


def field_print(g):
    for i in g:
        print(i)


def move_announcement():
    if mark == 'X':
        print(f'Сейчас ходит {x_player} и использует {mark}')
    else:
        print(f'Сейчас ходит {o_player} и использует {mark}')


def move_request(g, m):
    while True:
        x = input('Введите колонку(x) от 1 до 3:')
        y = input('\tВведите ряд(y) от 1 до 3:')
        if x.isdigit() and y.isdigit():
            x = int(x)
            y = int(y)
        else:
            print('Некорректный ввод.Должны быть числа.Повторите')
            continue
        if x < 1 or x > 3 or y < 1 or y > 3:
            print('Некорректный ввод.Должны быть число от 1 до 3.Повторите')
            continue
        elif g[y][x] == '-':
            g[y][x] = m
            return g
        else:
            print('Это поле уже занято...Повторите ввод.')


def player_change(c_p):
    if c_p == x_player:
        c_p = o_player
    else:
        c_p = x_player
    return c_p


def mark_change(c_p):
    global mark
    if c_p == x_player:
        mark = 'X'
    else:
        mark = 'O'


def winner_check(g):
    winner = None
    if (g[1][1] == g[1][2] == g[1][3] == 'X') or \
            (g[2][1] == g[2][2] == g[2][3] == 'X') or \
            (g[3][1] == g[3][2] == g[3][3] == 'X') or \
            (g[1][1] == g[2][1] == g[3][1] == 'X') or \
            (g[1][2] == g[2][2] == g[3][2] == 'X') or \
            (g[1][3] == g[2][3] == g[3][3] == 'X') or \
            (g[1][1] == g[2][2] == g[3][3] == 'X') or \
            (g[3][1] == g[2][2] == g[1][3] == 'X'):
        winner = x_player

    if (g[1][1] == g[1][2] == g[1][3] == 'O') or \
            (g[2][1] == g[2][2] == g[2][3] == 'O') or \
            (g[3][1] == g[3][2] == g[3][3] == 'O') or \
            (g[1][1] == g[2][1] == g[3][1] == 'O') or \
            (g[1][2] == g[2][2] == g[3][2] == 'O') or \
            (g[1][3] == g[2][3] == g[3][3] == 'O') or \
            (g[1][1] == g[2][2] == g[3][3] == 'O') or \
            (g[3][1] == g[2][2] == g[1][3] == 'O'):
        winner = o_player

    if '-' not in g[1] and '-' not in g[2] and '-' not in g[3]:
        winner = 'Никто! Попробуйте еще раз.'

    return winner


first_player = input('Введите имя первого игрока:')
second_player = input('Введите имя второго игрока:')

first_move = random.randint(1, 3)

if first_move == 1:
    print(f'{first_player} ходит первым и использует X')
    x_player = first_player
    o_player = second_player
else:
    print(f'{second_player} ходит первым и использует X')
    x_player = second_player
    o_player = first_player

mark = 'X'
current_player = x_player

while True:
    field_print(grid)
    result = winner_check(grid)
    if result is not None:
        break
    move_announcement()
    move_request(grid, mark)
    current_player = player_change(current_player)
    mark_change(current_player)

print(f'Победитель --> {result}')
