#READ

with open('passwords.txt', 'r', encoding='utf-8') as file:
  print(file.read(4)) #  read 4 bytes
  print(file.read())  #  read all/rest of bytes in fileif read before like above

with open('passwords.txt', 'r', encoding='utf-8') as file:
  print(file.readline(5)) #  read 5 bytes
  print(file.readline())  #  read all/rest of bytes in line if read before like above

with open('passwords.txt', 'r', encoding='utf-8') as file:
  print(file.readlines()) #  returns list
  
with open('passwords.txt', 'r', encoding='utf-8') as file:
  for line in file:
    print(line) #  returns line + \n
    print(line.strip()) #  returns line stripped from \s\n\t etc.


#WRITE
with open('checked.txt', 'w', encoding='utf-8') as file:
  file.write('new entry - check')
  file.write('NEW new entry - check')  # re-writes the line above

with open('checked.txt', 'a', encoding='utf-8') as file:
  file.write('new entry - check')
  file.write('NEW new entry - check')  # appends the line to existing contents

checked = ['this', 'that', 'that over there']
with open('checked.txt', 'w', encoding='utf-8') as file:
  for check in checked:
    file.write(check + '\n')  # writes all in the list each on new line

checked = ['this\n', 'that\n', 'that over there\n']
with open('checked.txt', 'w', encoding='utf-8') as file:
    file.writelines(checked)  # writes all in the list each on new line
