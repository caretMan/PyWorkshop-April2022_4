from random import randint


class IllegalMoveError(Exception):
  pass


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
  if len(Snake) > 6:
    print(f'\n{"".join(list(map(str, Snake[:3])))}...{"".join(list(map(str, Snake[-3:])))}\n\nYour pieces:')
  else:
    print(f'\n{"".join(list(map(str, Snake)))}\n\nYour pieces:')
  for i, piece in enumerate(Player, start=1):
    print(f'{i}:{piece}')

  if (Snake[0][0] == Snake[-1][-1] and Snake_Elements[Snake[0][0]] >= 8) or len(Player) == 0 or len(Computer) == 0:
    MovePossibility = False
    break

  if Status == 'computer_turn':
    Move = len(Computer)
    MovePossibility = False
    if len(Stock) > 0:
      MovePossibility = True
    else:
      while Move > 0:
        if Computer[Move - 1][0] == Snake[-1][1] or Computer[Move - 1][1] == Snake[-1][1] or Computer[Move - 1][1] == Snake[0][0] or Computer[Move - 1][0] == Snake[0][0]:
          MovePossibility = True
          break
        Move -= 1
    if not MovePossibility:
      break
    print(f"\nStatus: Computer is about to make a move. Press Enter to continue...")
    Move = input()
    while True:
      Move = randint(- len(Computer), len(Computer))
      try:
        if Move > 0:
          if Computer[Move - 1][0] == Snake[-1][1]:
            Snake.insert(len(Snake), Computer[Move - 1])
            Snake_Elements[Computer[Move - 1][0]] += 1
            Snake_Elements[Computer[Move - 1][1]] += 1
            Computer.pop(Move - 1)
            break
          elif Computer[Move - 1][1] == Snake[-1][1]:
            Computer[Move - 1][0], Computer[Move - 1][1] = Computer[Move - 1][1], Computer[Move - 1][0]
            Snake.insert(len(Snake), Computer[Move - 1])
            Snake_Elements[Computer[Move - 1][0]] += 1
            Snake_Elements[Computer[Move - 1][1]] += 1
            Computer.pop(Move - 1)
            break
          else:
            raise IllegalMoveError
        elif Move == 0:
          if len(Stock) > 0:
            Taken_piece = randint(0, len(Stock) - 1)
            Computer.append(Stock[Taken_piece])
            Stock.pop(Taken_piece)
            break
          else:
            raise IllegalMoveError
        else:
          if Computer[- Move - 1][1] == Snake[0][0]:
            Snake.insert(0, Computer[- Move - 1])
            Snake_Elements[Computer[- Move - 1][0]] += 1
            Snake_Elements[Computer[- Move - 1][1]] += 1
            Computer.pop(- Move - 1)
            break
          elif Computer[- Move - 1][0] == Snake[0][0]:
            Computer[- Move - 1][0], Computer[- Move - 1][1] = Computer[- Move - 1][1], Computer[- Move - 1][0]
            Snake.insert(0, Computer[- Move - 1])
            Snake_Elements[Computer[- Move - 1][0]] += 1
            Snake_Elements[Computer[- Move - 1][1]] += 1
            Computer.pop(- Move - 1)
            break
          else:
            raise IllegalMoveError
      except IllegalMoveError:
        continue
    Status = 'player_turn'

  elif Status == 'player_turn':
    Move = len(Player)
    MovePossibility = False
    if len(Stock) > 0:
      MovePossibility = True
    else:
      while Move > 0:
        if Player[Move - 1][0] == Snake[-1][1] or Player[Move - 1][1] == Snake[-1][1] or Player[Move - 1][1] == Snake[0][0] or Player[Move - 1][0] == Snake[0][0]:
          MovePossibility = True
          break
        Move -= 1
    if not MovePossibility:
      break
    print(f"\nStatus: It's your turn to make a move. Enter your command.")
    while True:
      try:
        Move = int(input())
        if Move > 0:
          if Player[Move - 1][0] == Snake[-1][1]:
            Snake.insert(len(Snake), Player[Move - 1])
            Snake_Elements[Player[Move - 1][0]] += 1
            Snake_Elements[Player[Move - 1][1]] += 1
            Player.pop(Move - 1)
            break
          elif Player[Move - 1][1] == Snake[-1][1]:
            Player[Move - 1][0], Player[Move - 1][1] = Player[Move - 1][1], Player[Move - 1][0]
            Snake.insert(len(Snake), Player[Move - 1])
            Snake_Elements[Player[Move - 1][0]] += 1
            Snake_Elements[Player[Move - 1][1]] += 1
            Player.pop(Move - 1)
            break
          else:
            raise IllegalMoveError
        elif Move == 0:
          if len(Stock) > 0:
            Taken_piece = randint(0, len(Stock) - 1)
            Player.append(Stock[Taken_piece])
            Stock.pop(Taken_piece)
            break
          else:
            raise IllegalMoveError
        else:
          if Player[- Move - 1][1] == Snake[0][0]:
            Snake.insert(0, Player[- Move - 1])
            Snake_Elements[Player[- Move - 1][0]] += 1
            Snake_Elements[Player[- Move - 1][1]] += 1
            Player.pop(- Move - 1)
            break
          elif Player[- Move - 1][0] == Snake[0][0]:
            Player[- Move - 1][0], Player[- Move - 1][1] = Player[- Move - 1][1], Player[- Move - 1][0]
            Snake.insert(0, Player[- Move - 1])
            Snake_Elements[Player[- Move - 1][0]] += 1
            Snake_Elements[Player[- Move - 1][1]] += 1
            Player.pop(- Move - 1)
            break
          else:
            raise IllegalMoveError
      except (ValueError, IndexError):
        print('Invalid input. Please try again')
      except IllegalMoveError:
        print('Illegal move. Please try again.')
    Status = 'computer_turn'

if len(Player) == len(Computer):
  print(f"\nStatus: The game is over. It's a draw")
elif len(Player) < len(Computer):
  print(f"\nStatus: The game is over. You won!")
else:
  print(f"\nStatus: The game is over. The computer won!")
