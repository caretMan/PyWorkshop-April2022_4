with open('passwords.txt', 'r', encoding='utf-8') as file:
  letters = {}
  passwords = []
  for line in file:
    password = line.strip()
    passwords.append(password)
    for i in range(len(password)):
      letters.setdefault(password[i], 0)
      letters[password[i]] += 1
  score = []
  for password in passwords:
    score.append(0)
    for i in range(len(password)):
      score[-1] += letters[password[i]]

  print(passwords[score.index(min(score))])
