# 10505. 소득불균형, D3

t = int(input())

for tc in range(1 , t+1):
    N = int(input())
    incomes = list(map(int,input().split()))

    avg = sum(incomes) // N
    result = [x for x in incomes if avg >= x]
    print(f"#{tc} {len(result)}")
