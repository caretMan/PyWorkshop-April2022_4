from random import randint


while True:
    Stock = [[i, j] for i in range(7) for j in range(i, 7)]
    Player = []
    Computer = []
    for i in range(7):
        CurrentPiece = randint(0, len(Stock) - 1)
        Player.append(Stock[CurrentPiece])
        Stock.pop(CurrentPiece)
    for i in range(7):
        CurrentPiece = randint(0, len(Stock) - 1)
        Computer.append(Stock[CurrentPiece])
        Stock.pop(CurrentPiece)
    if [6, 6] not in Stock or [5, 5] not in Stock:
        break

if [6, 6] not in Stock:
    Snake = [[6, 6]]
    Snake_Elements = [0, 0, 0, 0, 0, 0, 2]
else:
    Snake = [[5, 5]]
    Snake_Elements = [0, 0, 0, 0, 0, 2, 0]
if Snake[0] in Player:
    Player.remove(Snake[0])
    Status = 'computer_turn'
else:
    Computer.remove(Snake[0])
    Status = 'player_turn'


while True:

    print('================================================================================')
    print(f'Stock size: {len(Stock)}')
    print(f'Computer pieces: {len(Computer)}')
    Snake_to_print = ''
    if len(Snake) > 6:
        Snake_to_print = f'{Snake[0]}{Snake[1]}{Snake[2]}...{Snake[-3]}{Snake[-2]}{Snake[-1]}'
    else:
        for piece in Snake:
            Snake_to_print += str(piece)
    print(f'\n{Snake_to_print}\n\nYour pieces:')
    for i, piece in enumerate(Player, start=1):
        print(f'{i}:{piece}')

    if Status == 'computer_turn':
        print(f"\nStatus: Computer is about to make a move. Press Enter to continue...")
        Move = input()
        Move = randint(- len(Computer), len(Computer))
        if Move > 0:
            Snake.insert(len(Snake), Computer[Move - 1])
            Snake_Elements[Computer[Move - 1][0]] += 1
            Snake_Elements[Computer[Move - 1][1]] += 1
            Computer.pop(Move - 1)
        elif Move == 0:
            Taken_piece = randint(0, len(Stock) - 1)
            Computer.append(Stock[Taken_piece])
            Stock.pop(Taken_piece)
        else:
            Snake.insert(0, Computer[- Move - 1])
            Snake_Elements[Computer[- Move - 1][0]] += 1
            Snake_Elements[Computer[- Move - 1][1]] += 1
            Computer.pop(- Move - 1)
        Status = 'player_turn'

    elif Status == 'player_turn':
        print(f"\nStatus: It's your turn to make a move. Enter your command.")
        while True:
            try:
                Move = int(input())
                if Move > 0:
                    Snake.insert(len(Snake), Player[Move - 1])
                    Snake_Elements[Player[Move - 1][0]] += 1
                    Snake_Elements[Player[Move - 1][1]] += 1
                    Player.pop(Move - 1)
                elif Move == 0:
                    Taken_piece = randint(0, len(Stock) - 1)
                    Player.append(Stock[Taken_piece])
                    Stock.pop(Taken_piece)
                else:
                    Snake.insert(0, Player[- Move - 1])
                    Snake_Elements[Player[- Move - 1][0]] += 1
                    Snake_Elements[Player[- Move - 1][1]] += 1
                    Player.pop(- Move - 1)
            except (ValueError, IndexError):
                print('Invalid input. Please try again')
            else:
                break
        Status = 'computer_turn'

    elif Status == 'player_won':
        print(f"\nStatus: The game is over. You won!")
        break
    elif Status == 'computer_won':
        print(f"\nStatus: The game is over. The computer won!")
        break
    else:
        print(f"\nStatus: The game is over. It's a draw")
        break

    if Snake[0][0] == Snake[-1][-1] and Snake_Elements[Snake[0][0]] >= 8:
        Status = 'draw'
    elif len(Player) == 0:
        Status = 'player_won'
    elif len(Computer) == 0:
        Status = 'computer_won'
