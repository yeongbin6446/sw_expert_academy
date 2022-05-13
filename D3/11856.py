# 11856. 반반, D3

t = int(input())

for test_case in range(1, t+1):
    S = input()
    s = list(set(S))

    print(f"#{test_case}", end=' ')
    if len(s) == 2:
        print('Yes')
    else:
        print('No')

