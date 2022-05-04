# 1936. 1대1 가위바위보, D1

A , B = map(int, input().split())
winner = ''
if A == 1:
    if B == 2:
        winner = 'B'
    else:
        winner = 'A'
elif A == 2:
    if B == 1:
        winner = 'A'
    else:
        winner = 'B'
else:
    if B == 1:
        winner = 'B'
    else:
        winner = 'A'

print(winner)

