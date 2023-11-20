lines = int(input('请输入行数： '))

for line in range(1,lines + 1):
    print('*' * line)

print('')
print('')

for line in range(1, lines + 1):
    print(' ' * (lines - line) + '*' * line)

print('')
print('')

for line in range(1, lines + 1):
    print(' ' * (lines - line) + '*' * (2 * line - 1))
