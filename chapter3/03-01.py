print(f'{"03-01: it문":=^50}')

money = True
if money:
	print("택시 타고 가세요.")
else:
	print("버스 타고 가세요.")

pocket = ["none"]
if "card" in pocket:
	print("bus")
elif "card" not in pocket:
	print("walk")

# 조건부 표현식
# 변수 = 조건문이_참인_경우의_값 if 조건문 else 조건문이_거짓일때_값
socre = 10
message = "success" if socre > 60 else "failure" 
print(message)