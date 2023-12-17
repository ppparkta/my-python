print(f'{"03-03: for문":=^50}')
marks=[90,25,67,45,80]
for i in range(len(marks)):
	if marks[i] >= 60:
		print("합격")
	else:
		print("불합격")

# 
number = 0
for mark in marks:
	number+=1
	if mark < 60:
		continue
	print("축하합니다. %d번 학생 합격입니다." %number)

add = 0
for i in range(1,11):
	add += i

print(add)

# range 활용
result=0
for i in range(1, 101):
	result+=i
print(result)

for i in range(1,11):
	for j in range(1,11):
		print(i*j,end=' ')
	print('')

# 리스트 컴프리헨션
# [표현식 for 항목 in 반복_가능_객체 if 조건문]
a = [1,2,3,4]
result=[]
for i in a:
	result.append(i*3)
print(result)

result2=[num*3 for num in a]
print(result2)

