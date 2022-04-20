from collections import Counter


text = ("all I want is a proper cup of coffee made in a proper copper coffee pot. "
        "I may be off my dot but I want a cup of coffee from a proper coffee pot.")

n = int(input())
List_C = Counter(text.split())
for i in range(n):
  print(List_C.most_common(n)[i][0], List_C.most_common(n)[i][1])
