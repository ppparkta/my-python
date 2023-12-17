# 03-02 while

prompt = """
1. Add
2. Del
3. List
4. Quit

Enter Number: """

number = 0
while number != 4:
	print(prompt)
	number = int(input())

a = [1,2,3,4,5,6,7,8,9,10]
count = 0
while count != 10:
	
	if a[count] % 3 != 0:
		print(a[count])
	count+=1