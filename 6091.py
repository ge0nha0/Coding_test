# 최소 공배수 문제
a, b, c = map(int, input().split())

i = 0

while True:
    i += 1

    if (i%a==0) and (i%b==0) and (i%c==0):
        print(i)
        break