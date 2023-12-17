# Python 스터디
![image](https://github.com/ppparkta/my-python/assets/86940801/e7af9705-3e6c-4161-9328-3a4a51bd1659)

## 목차

1. [변수의 복사](02-8 자료형의 값을 저장하는 공간, 변수)
2. [리스트 컴프리핸션](03-3 리스트 컴프리헨션)


# 02-8 자료형의 값을 저장하는 공간, 변수
```python
a = [1, 2, 3]
id(a) # 430329896

b = a
id(b) # 430329896
```
변수를 대입연산자로 복사하게 되면 C와는 달리 동일한 메모리를 참조하게 된다. (reference) id 함수를 통해 이 사실을 확인할 수 있다.<br>
그렇다면 어떻게 다른 주소를 가리키는 변수를 만들까? 두가지 방법이 있다.
1. [:] 이용하기 
2. copy 모듈 이용하기
```python
a = [1, 2, 3]
b = a[:]
a[1] = 4

print(a)
print(b)
```
```python
from copy import copy

a = [1, 2, 3]
b = copy(a)
c = a.copy()
```

### 03-3 리스트 컴프리헨션
```python
a = [1, 2, 3, 4]
result = []
for num in a:
	result.append(num * 3)
```
```python
a = [1, 2, 3, 4]
result = [num * 3 for num in a]
```
리스트 안에 for문을 포함하는 리스트 컴프리헨션을 사용하면 편리하게 작성할 수 있다.