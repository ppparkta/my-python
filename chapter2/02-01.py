# ========================
a = 123
a = 10e10

print(a)

a = 3
b = 4
print(a+b)

print(10 * 18 ** 2 + 2 * 11)

print(b / a)

# =========================
c = 'hello'
d = "'hello'"
e = """
"hi!!"
"""
f = ''' hi! '''

print(c)

# =========================
print("="*20)
print("\"My Program\"")
print("="*20)

# ========================

b = '\"My Program\"'
#     012345678910/11

print(b[-5])

# =======================

c = b[1]+b[-3]+b[-2]

print(c)
print(b[4:-1])
print(b[-8:-1])
print(b[:18])
# =============================

d = "20231216"

year = d[:4]
month = d[4:-2]
day = d[-2:]

print(year+" "+month+" "+day)

phone = "010-4736-7769"

# =============================

r = 3.1111111111111111111
print("hello %s %10.3f" % ("dohun", r))

print(" %10s | %10s | %10s" % ("수빈", "도훈", "람강"))

print("eat {count} apples".format(count="five"))


# =============================

print(f'나의 이름은 {b:^20} 입니다.')

print(f'{"python":!^12}')
new = "010-4736-7769"
lst = new.split('-')
print(lst)

# ==============================
# string1 = input()

# a, b = string1.split(' ')
# print(int(a), int(b))

# a,b= input().split(' ')
# print(a-b)

print("""|\_/|
|q p|   /}
( 0 )"""
| "^"` |
| | _ /=\\__|
""")
