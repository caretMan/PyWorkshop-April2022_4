import random

Set = []
while len(Set) < 28:
    Set.append([random.randint(0, 6), random.randint(0, 6)])
    for i in range(len(Set) - 1):
        if Set[-1] == Set[i] or Set[-1][-1::-1] == Set[i]:
            Set.pop(-1)
            break
