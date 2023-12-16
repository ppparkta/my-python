print(f'{"02-05: 딕셔너리":=^50}')

dic = {'name': "pey", "phone": "010-1234-5678", "birth": "0715"}
print(dic)

dic["address"] = "경기도"
print(dic)

# ==============================
# list는 값이 변할 수 있으므로 key에 올 수 없음
# a={[1,2]:'hi'}

# tuple은 값이 변할 수 없으므로 key에 올 수 있음
a = {(1, 2): 'hi'}
print(a)

print(f'\n{"02-05: 딕셔너리 관련 함수":=^50}')

print(dic.keys())
for i in dic.keys():
    print(i)

print(dic.values())
for i in dic.values():
    print(i)

print(dic.items())
for i in dic.items():
    print(i)

print(dic.get('name'))
# 없는 key에 접근 시
print(dic.get('lol'))  # None반환
# print(dic['lol']) # 문법 오류

print(dic.get('lol', 'leagueOfLegend'))

# =============================================

n = int(input())
check = False
dic = {'BANANA':0, 'PLUM':0, 'STRAWBERRY':0, 'LIME':0}
for i in range(n):
	a, C = input().split(' ')
	c = int(C)
	dic[a] += c
for i in dic.values():
	if i == 5:
		print("YES")
		check = True
		break;
if check == False:
	print("NO")