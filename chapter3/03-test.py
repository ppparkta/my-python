# 03 반복문 테스트
# 01
# shirt\n need

# 02
result = 0
i = 1
while i <= 1000:
	if i %3 ==0:
		result+=i
	i+=1
print(result)

# 03
i=0
while True:
	i+=1
	if i > 5 : break
	print("*"*i)

# 04
for i in range(1, 101):
	print(i, end=" ")

# 05
students=[70,60,55,75,95,90,80,80,85,100]
total=0
for score in students:
	total+=score
total /= len(students)
print("\n",total)

# 06
numbers = [1,2,3,4,5]
result = [n*2 for n in numbers if n % 2 == 1]
print(result)

test = (n*2 for n in numbers if n * 2 ==1)
print (test)