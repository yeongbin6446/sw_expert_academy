# 1946. 간단한 압축 풀기, D2

t = int(input())

for test_case in range(1, t+1):
    N = int(input())
    zip = {}
    for i in range(N):
        al, num = input().split()
        num = int(num)

        zip[al] = num

    a = (sum(zip.values()) // 10) + 1
    s = ''
    for i in zip.keys():
        s += i * zip[i]

    s = list(s)
    cnt = 0
    print(f"#{test_case}")
    for i in range(len(s)):
        print(s[i], end= '')
        cnt += 1
        if cnt % 10 == 0:
            print()
    print()


