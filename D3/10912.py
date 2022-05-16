# 10912. 외로운 문자, D3

t = int(input())

for test_case in range(1, t+1):
    str = input()
    k = set(list(str))
    s = {}
    for i in k:
        s[i] = 0

    for i in str:
        s[i] += 1
    result = []
    for i in s:
        if s[i] % 2 != 0:
            result.append(i)
    result.sort()
    print(f"#{test_case}", end=' ')
    if not result:
        print('Good')
    else:
        print(''.join(result))