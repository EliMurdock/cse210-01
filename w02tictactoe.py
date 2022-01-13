'''
Eli Murdock
W02 develop
CSE210-01 Winter 2022
1/12/22
'''

def main():
    gameboard_values = [1,2,3,4,5,6,7,8,9]
    round = 0
    while game_end(gameboard_values) == False:
        round += 1
        print(f'''
    {gameboard_values[0]}|{gameboard_values[1]}|{gameboard_values[2]}
    -+-+-
    {gameboard_values[3]}|{gameboard_values[4]}|{gameboard_values[5]}
    -+-+-
    {gameboard_values[6]}|{gameboard_values[7]}|{gameboard_values[8]}
        ''')
        if round % 2 == 1:
            player = 'x'
        else:
            player = 'y'
        spot_picked = int(input(f'{player}\'s turn to choose a square (1-9): '))
        gameboard_values.insert(spot_picked, player)
        gameboard_values.remove(spot_picked)
    print('Good game. Thanks for playing!')

def game_end(gameboard_values):
    v =gameboard_values
    if (v[0] == v[1] == v[2] or 
        v[3] == v[4] == v[5] or 
        v[6] == v[7] == v[8] or 
        v[0] == v[3] == v[6] or 
        v[1] == v[4] == v[7] or 
        v[2] == v[5] == v[8] or 
        v[0] == v[4] == v[8] or 
        v[2] == v[4] == v[6]):
        return True
    else:
        return False


if __name__ == '__main__':
    main()