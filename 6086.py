# 1,2,3,4,5 순서대로 계속 더해가다가 그 합이 입력된 정수보다 커지거나 같아지는 경우, 그때까지의 합을 출력

num = int(input())
sum = 0
cnt = 0

while True:
    sum += cnt 
    cnt += 1

    if sum >= num:
        break

print(sum)