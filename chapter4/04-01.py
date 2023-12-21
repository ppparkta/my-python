# 입출력
def add(a,b):
	return a+b

a=3
b=5
print(add(a,b))

def say():
	return "Hi"

print(say())

def new_add(a,b):
	print('%d, %d의 합은 %d입니다.' %(a,b,a+b))

new_add(a,b)
	
# 입력값이 몇 개가 될지 모를 때는 어떻게 해야 할까? 
def add_many(*args):
	result = 0
	for i in args:
		result += i
	return result

print(add_many(1,5,7,8,12,20))