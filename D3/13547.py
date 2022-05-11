# 13547. 팔씨름, D3

T = int(input())

for test_case in range(1, T + 1):
    print(f'#{test_case}', end=' ')
    c = 8
    result = input()
    for i in result:
        if i == 'o':
            c -= 1
    if c <= 0 or 15 - len(result) >= c:
        print('YES')
    else:
        print('NO')