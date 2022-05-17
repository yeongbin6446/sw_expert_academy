# 10059. 유효기간, D3

t = int(input())

for tc in range(1, t+1):
    validity = input()

    front = int(validity[:2])
    back = int(validity[2:])

    print(f"#{tc}" ,end=' ')
    if 0 < front < 13 and 0 < back < 13:
        print("AMBIGUOUS")
    elif 0 < front < 13:
        print("MMYY")
    elif 0 < back < 13:
        print("YYMM")
    else:
        print("NA")