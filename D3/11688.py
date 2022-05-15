# 11688. Calkin-Wilf tree 1, D3

t = int(input())

for test_case in range(1, t+1):
    s = input()
    a = 1
    b = 1
    for i in s:
        if i == 'L':
            a = a
            b = a + b
        if i == 'R':
            a = a + b
            b = b
    print(f"#{test_case} {a} {b}")