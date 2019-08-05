bird, food, _ = map(int, input().split())
leaves = list(map(int, input().split()))

current = bird + food
first_leaf = leaves.pop(0)
lost = 0

if current > first_leaf:
    current = first_leaf

for leaf in leaves:
    if current > leaf:
        current = leaf
        if current < bird:
            break
        lost += 1

print(lost)
