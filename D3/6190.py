# 6190. 정곤이의 단조 증가하는 수, D3
def check(num):
    s_num = str(num)
    for i in range(len(s_num)-1):
        if s_num[i] <= s_num[i+1]:
            pass
        else:
            return False
    return True

t = int(input())

for tc in range(1, t+1):
    N = int(input())
    A = list(map(int,input().split()))

    nums = []
    for i in range(N-1):
        for j in range(i+1,N):
            nums.append(A[i] * A[j])
    nums.sort(reverse=True)
    for num in nums:
        if check(num):
            result = num
            break
        else:
            result = -1

    print(f"#{tc} {result}")