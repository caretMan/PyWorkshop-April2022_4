sentence = 'Chess set is a chessboard and a set of chessmen.'
frequencies = {}

for i in sentence.split():
  frequencies.setdefault(i, 0)
  frequencies[i] += 1
print(frequencies)
