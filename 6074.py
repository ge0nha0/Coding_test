# 문자 1개 입력받아 알파벳 출력하기
# chr(정수값) -> 유니문자 코드 출력

start = ord("a") # a의 정수값
last = ord(input())

while start <= last:
    print(chr(start), end=' ')
    start += 1