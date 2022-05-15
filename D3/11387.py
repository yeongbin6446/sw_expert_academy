# 11387. 몬스터 사냥, D3

t = int(input())

for test_case in range(1, t+1):
    D, L, N = map(int, input().split())

    damage = D

    for i in range(1,N):
        damage += D + D * i * L //100

    print(f"#{test_case} {damage}")
