# 각 행에서 가장 작은 수를 찾음 -> 이후 그 수 중에서 가장 큰 수를 찾기

n, m = map(int, input().split())

max_number = 0

for i in range(n):
    numbers = list(map(int, input().split()))
    min_number = min(numbers)
    max_number = max(min_number, max_number)

print(max_number)

# 이중 반복문으로 풀기

n, m = map(int, input().split())

result = 0

for i in range(n):
    data = list(map(int, input().split()))
    min_value = 10001
    for a in data:
        min_value = min(min_value, a)

    result = max(result, min_value)

print(result)