from collections import Counter

S = input()
S = S.lower()
List = S.split()
C = Counter(List)
print(sorted(C.elements()))
