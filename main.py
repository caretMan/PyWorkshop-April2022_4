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
else:
  Snake = [[5, 5]]
if Snake[0] in Player:
  Player.remove(Snake[0])
  Status = 'computer'
else:
  Computer.remove(Snake[0])
  Status = 'player'

# print(f'Stock pieces: {Stock}\nComputer pieces: {Computer}\nPlayer pieces: {Player}\nDomino snake: {Snake}\nStatus: {Status}')

print('================================================================================')

print(f'Stock size: {len(Stock)}')

print(f'Computer pieces: {len(Computer)}')

Snake_to_print = ''
for i, piece in enumerate(Snake, start = 1):
  Snake_to_print += str(piece)
  if i != len(Snake):
    Snake_to_print += ' '
print(f'\n{Snake_to_print}\n\nYour pieces:')

for i, piece in enumerate(Player, start = 1):
  print(f'{i}:{piece}')
  
if Status == 'player':
  print(f"\nStatus: It's your turn to make a move. Enter your command.")
else:
  print(f"\nStatus: Computer is about to make a move. Press Enter to continue...")