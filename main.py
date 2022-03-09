print(f"|{0}|{1}|{2}|\n_______\n|{3}|{4}|{5}|\n_______\n|{6}|{7}|{8}|")

game_numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
game_board_nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
player_one_choice = []
player_two_choice = []


def compare(player):
    if all(x in player for x in ['0', '1', '2']):
        return True
    elif all(x in player for x in ['5', '4', '3']):
        return True
    elif all(x in player for x in ['8', '7', '6']):
        return True
    elif all(x in player for x in ['0', '4', '8']):
        return True
    elif all(x in player for x in ['6', '4', '2']):
        return True
    elif all(x in player for x in ['8', '5', '2']):
        return True
    elif all(x in player for x in ['7', '1', '4']):
        return True
    elif all(x in player for x in ['0', '6', '3']):
        return True


game_on = True


def player_one_func():
    global game_on
    player_one = input("Your turn player one:")
    player_one_int = int(player_one)
    if player_one in game_board_nums:
        player_one_choice.append(player_one)
        game_board_nums.remove(player_one)
        game_numbers[player_one_int] = 'X'
        a = f"|{game_numbers[0]}|{game_numbers[1]}|{game_numbers[2]}|\n_______\n|{game_numbers[3]}|{game_numbers[4]}|{game_numbers[5]}|\n_______\n|{game_numbers[6]}|{game_numbers[7]}|{game_numbers[8]}|"
        print(a)
        print(player_one_choice)
        if compare(player=player_one_choice):
            print('player one wins')
            game_on = False


def player_two_func():
    global game_on
    if game_on:
        player_two = input("Your turn player Two:")
        player_two_int = int(player_two)
        if player_two in game_board_nums:
            player_two_choice.append(player_two)
            game_board_nums.remove(player_two)
            player_two_int = int(player_two)
            game_numbers[player_two_int] = 'O'
            a = f"|{game_numbers[0]}|{game_numbers[1]}|{game_numbers[2]}|\n_______\n|{game_numbers[3]}|{game_numbers[4]}|{game_numbers[5]}|\n_______\n|{game_numbers[6]}|{game_numbers[7]}|{game_numbers[8]}|"
            print(a)
            print(player_two_choice)
            if compare(player=player_two_choice):
                print('player two wins')
                game_on = False


while game_on:

    player_one_func()
    player_two_func()

