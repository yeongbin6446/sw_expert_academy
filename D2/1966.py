# 1966. 숫자를 정렬하자, D2

t = int(input())

for test_case in range(1, t+1):
    N = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    print(f"#{test_case}", end=' ')
    print(*arr)