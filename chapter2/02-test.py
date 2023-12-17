# 되새김문제

# 01
a = 80 + 70 + 55
print(a/3)

# 02
b=13
if b % 2 == 0:
	print(True)
else:
	print(False)

# 03
pin='881120-1068234'
yyyymmdd=pin.split('-')
print(yyyymmdd[0])
print(yyyymmdd[1])

# 04
print(pin[-7])

# 05
a = "a:b:c:d"
b = a.replace(':', "#")
print(b)

# 06
a = [1,3,5,4,2]
a.sort()
a.reverse()
print(a)

# 07
a = ['life','is','too','short']
result = ' '.join(a)
print(result)

# 08
a = (1,2,3)
a= a + (4,)
print(a)

# 09
a = dict()
print(a)
# 딕셔너리의 키는 불변한다. 따라서 값이 변할 수 있는 리스트는 올 수 없다.

# 10
a = {'A':90, 'B':80, 'C':70}
result = a['B']
a.pop('B')
print(a)
print(result)

# 11
a = [1,1,1,2,2,3,3,3,4,4,5]
aSet = set(a)
b = list(aSet)
print(b)

# 12
a=b=[1,2,3]
a[1]=4
print(b)
# 파이썬에서 값에 대입연산자 사용 시 메모리주소까지 완전히 같은 변수를 생성한다.
# 이를 예방하기 위해서 [:] 혹은 copy함수를 사용한다.