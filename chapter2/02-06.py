print(f'{"02-06: 집합":=^50}')

# 집합 자료형
s1 = set([1,2,3])
print(s1)
s2=set((1,2,3))
print(s2)

l1 = list(s1)
print(l1)

s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])

print(s1&s2)
print(s1|s2)
print(s1-s2)