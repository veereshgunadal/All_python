a = [' ' for _ in range(9)]
print(a)

a = []
for i in range(9):
    a.append(" ")

print(a)

board = [' ' for _ in range(9)]
for row in [board[i*3:(i+1)*3] for i in range(3)]:
    print('| ' + ' | '.join(row) + ' |')


board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

l= []
for i in range(3):
    l.append(board[i*3: (i+1)*3])
    print(l)
for row in l:
    print('| ' + ' | '.join(row) + ' |')







