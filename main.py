from string import digits


class NotWordError(Exception):
  def __init__(self, x):
    self.message = f'"{x}" is not a word, sorry!'
    super().__init__(self.message)


def check_word(word):
  for i in range(len(digits)):
    if digits[i] in word:
      raise NotWordError(word)
  return word


def error_handling(word):
  try:
    check_word(word)
  except NotWordError as err:
    print(err)
  else:
    print(word)


word = input()
error_handling(word)