# ===============================
# list
print(f'{"02-03: List":=^50}')

odd = [1,3,5,7,9]
a=[]
b=[1,2,3]
c=['life','is','too','short']
d=[1,2,'life','is']
e=[1,2,['life','is']]

print(b[0]+b[2])
print(b[-1])
print(e[2][0])
print(b[:-2])

# ===============================

a = [1,2,3,4,5]
b=a[:2]
c=a[2:]
print(b)
print(c)
print(a[1:3])

# ===============================
print(f'{"02-03: 리스트 연산하기":=^50}')
a=[1,2,3]
b=[4,5,6]
print(a+b)
print(a*3)
print(len(a),'\n')

del a[0]
print(a)

# ===============================
print(f'{"02-03: 리스트 관련 함수":=^50}')

a.append(4)
print(a)
a.append([5,6])
print(a)

a=[1,4,3,2]
a.sort()
print(a)
a.reverse()
print(a)


a = int(input())
for i in range(a):
    print(f'{" "*(a-i-1)}{"*"*(i*2+1)}')
b = a-1
for i in range(b):
    print(f'{" "*(1+i)}{"*"*((b-i)*2-1)}')