# 1859. 백만 장자 프로젝트, D2

t = int(input())

for i in range(t):
    N = int(input())
    result = 0
    prices = list(map(int, input().split()))
    max_price_idx = prices.index(max(prices))
    if max_price_idx == 0:
        pass
    elif max_price_idx == N-1:
        for i in range(N-1):
            result += prices[N-1] - prices[i]
    else:
        while prices:
            max_price_idx = prices.index(max(prices))
            for i in range(max_price_idx):
                result += prices[max_price_idx] - prices[i]
            prices = prices[max_price_idx+1:]
    print(f"{i+1} {result}")
