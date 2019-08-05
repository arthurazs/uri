bits = int(input(), 2)

inputs = int(input())

divides = []

for _ in range(inputs):
    number = int(input())
    if bits % number == 0:
        divides.append(number)

if not divides:
    divides = 'Nenhum'
else:
    divides.sort()
    divides = ' '.join(map(str, divides))

print(divides)
