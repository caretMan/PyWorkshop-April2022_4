class WordError(Exception):
    def __str__(self):
        return 'Error!'

def check_w_letter(word):
    if letter not in word:
        raise WordError
    else:
        return word

letter, word = input(), input()
print(check_w_letter(word))