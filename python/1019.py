seconds = int(input())

hours = seconds // 60 // 60
seconds = seconds - (hours * 60 * 60)
minutes = seconds // 60
seconds = seconds - (minutes * 60)

print('{}:{}:{}'.format(hours, minutes, seconds))
