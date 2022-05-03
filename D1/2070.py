# 2070. 큰 놈, 작은 놈, 같은 놈  D1

t = int(input())

for i in range(t):
    result = ''
    n1, n2 = map(int, input().split())
    if n1 > n2:
        result = '>'
    elif n1 == n2:
        result = '='
    else:
        result = '<'

    print(f"#{i+1} {result}")