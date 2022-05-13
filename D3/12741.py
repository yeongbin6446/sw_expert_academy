# 12741. 두 전구, D3

t = int(input())
results = []

for test_case in range(1, t+1):
    A, B, C, D = map(int, input().split())

    result = min(B,D) - max(A,C)
    if result < 0:
        result = 0

    results.append(result)

for test_case, result  in enumerate (results):
    print(f"#{test_case+1} {result}")