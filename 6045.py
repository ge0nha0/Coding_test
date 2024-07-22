# map -> 리스트의 요소를 지정된 함수로 처리해주는 함수 -> 원본 리스트를 변경하지 않고 새 리스트를 생성함
# list(map(함수, 리스트)) # tuple(map(함수, 튜플))

a, b, c = map(int, input().split())

avg = (a+b+c) / 3

print(a+b+c)
print(format(avg, ".2f"))