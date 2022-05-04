# 1926. 간단한 369게임, D2

N = int(input())

for i in range(1,N+1):
    if '3' in str(i) or '6' in str(i) or '9' in str(i):
        cnt = 0
        for j in str(i):
            if j == '3' or j == '6' or j == '9':
                cnt += 1
        print('-' * cnt, end=' ')
    else:
        print(i, end=' ')
