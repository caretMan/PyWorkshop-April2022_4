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
print(f'Stock pieces: {Stock}\nComputer pieces: {Computer}\nPlayer pieces: {Player}\nDomino snake: {Snake}\nStatus: {Status}')