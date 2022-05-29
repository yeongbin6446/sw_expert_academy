# 5986. 새샘이와 세 소수, D3
def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

t = int(input())

for tc in range(1, t+1):
    N = int(input())

    n = []
    for i in range(2,N):
        if is_prime(i):
            n.append(i)
    l = len(n)
    cnt = 0
    for i in range(l):
        for j in range(i,l):
            for k in range(j,l):
                if n[i] + n[j] + n[k] == N:
                    cnt += 1

    print(cnt)