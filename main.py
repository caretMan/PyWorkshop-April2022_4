with open('passwords.txt', 'r', encoding='utf-8') as file:
  letters = []
  freqs = []
  total = 0
  for line in file:
    password = line.strip()
    for i in range(len(password)):
      if password[i] not in letters:
        letters.append(password[i])
        freqs.append(1)
      else:
        freqs[letters.index(password[i])] += 1
      total += 1
  fl = []
  for freq, letter in zip(freqs, letters):
    fl.append([freq, letter])
  freqs_sorted = []
  letters_sorted = []
  fl.sort
  for i in fl:
    freqs_sorted.append(i[0])
    letters_sorted.append(i[1])
  print('Most common:')
  for freq, letter in zip(freqs_sorted[:5], letters_sorted[:5]):
    t = '%.3f' % (freq / total * 100)
    print(f'{letter} - {t}%')
  print('\nMost rare:')
  for freq, letter in zip(freqs_sorted[-5:], letters_sorted[-5:]):
    t = '%.3f' % (freq / total * 100)
    print(f'{letter} - {t}%')
