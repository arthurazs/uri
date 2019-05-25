def maior(x, y):
    return (x + y + abs(x - y)) // 2


a, b, c = map(int, input().split())

ab = maior(a, b)
abc = maior(ab, c)

print('{} eh o maior'.format(abc))
