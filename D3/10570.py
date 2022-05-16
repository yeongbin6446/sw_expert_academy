# 10570. 제곱 팰린드롭 수, D3
import math

def is_palindrome(num):
    num = list(str(num))
    num_rev = num.copy()
    num_rev.reverse()
    if num_rev == num:
        return True
    else:
        return False

t = int(input())

for tc in range(1, t+1):
    A, B = map(int, input().split())
    cnt = 0
    for i in range(math.ceil(math.sqrt(A)),math.ceil(math.sqrt(B+1))):
        if is_palindrome(i):
            if is_palindrome(i**2):
                cnt += 1

    print(cnt)

