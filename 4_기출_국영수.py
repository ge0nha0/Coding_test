# 국어 점수가 감소하는 순서
# 국어 점수 = 영어 점수가 증가하는 순서
# 국어, 영어 = 수학 점수 감소하는 순서
# 모든 점수가 같으면 이름이 사전 순으로 증가하는 순서 
## 아스키코드에서 대문자는 소문자보다 작으므로 사전 순으로 아에 옴
### sort() 함수의 key속성에 값을 대입하여 내가 원하는 조겐에 맞게 튜플을 정렬시킬 수 있음

n = int(input())

students = []

for _ in range(n):
  students.append(input().split())

students.sort(key=lambda x: (-int(x[1]), int(x[2]),-int(x[3]), x[0]))

for student in students:
  print(student[0])