from random import choices, randint


class EndOfFileError(Exception):
  pass


with open('passwords.txt', 'r', encoding='utf-8') as file:
  letters = []
  freqs = []
  while True:
    try:
      password = file.readline()
      if password == '':
        raise EndOfFileError
    except EndOfFileError:
      break
    else:
      for i in range(len(password)):
        if password[i] not in letters:
          letters.append(password[i])
          freqs.append(1)
        else:
          freqs[letters.index(password[i])] += 1
if '\n' in letters:
  freqs.pop(letters.index('\n'))
  letters.remove('\n')
print(''.join(list(map(str, [choices(letters, freqs)[0] for _ in range(randint(6, 10))]))))
