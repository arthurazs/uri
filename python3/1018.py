value = int(input())


def minus(total, note, count=0):
    if total >= note:
        return minus(total - note, note, count + 1)
    else:
        return total, count


print(value)
value, hundred = minus(value, 100)
print('{} nota(s) de R$ 100,00'.format(hundred))
value, fifty = minus(value, 50)
print('{} nota(s) de R$ 50,00'.format(fifty))
value, twenty = minus(value, 20)
print('{} nota(s) de R$ 20,00'.format(twenty))
value, ten = minus(value, 10)
print('{} nota(s) de R$ 10,00'.format(ten))
value, five = minus(value, 5)
print('{} nota(s) de R$ 5,00'.format(five))
value, two = minus(value, 2)
print('{} nota(s) de R$ 2,00'.format(two))
value, one = minus(value, 1)
print('{} nota(s) de R$ 1,00'.format(one))
