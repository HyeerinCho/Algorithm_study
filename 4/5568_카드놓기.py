from itertools import permutations

n = int(input())
k = int(input())

cards = []

for _ in range(n):
    card = input()
    cards.append(card)

res = set() 

#순열써야됨
for i in permutations(cards, k):
    res.add("".join(i))

print(len(res))