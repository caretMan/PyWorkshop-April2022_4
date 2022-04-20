from collections import Counter

List = input().split()
List_C = Counter(List)
print(List_C.most_common(1)[0][0])
