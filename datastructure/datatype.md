# 자료형

### 배열 원소의 최대값을 구하는 함수 구현하기

```python
# 시퀀스 원소의 최댓값 출력하기

from typing import Any, Sequence

def max_of(a: Sequence) -> Any:
    """시퀀스형 a 원소의 최댓값을 반화"""
    maximum = a[0]
    for i in range(1, len(a)):
        if a[i] > maximum:
            maximum = a[i]
    return maximum

if __name__ == '__main__':
    print('배열의 쵀댓값을 구합니다.')
    num = int(input('원소 수를 입력하세요.: '))
    x = [None] * num # 원소 수가 num 인 리스트를 생성

    for i in range(num):
        x[i] = int(input(f'x[{i}]값을 입력하세요.: '))

    print(f'최댓값은 {max_of(x)}입니다.')
```

```python
실행결과: 

배열의 쵀댓값을 구합니다.
원소 수를 입력하세요.: 5
x[0]값을 입력하세요.: 2321
x[1]값을 입력하세요.: 1232
x[2]값을 입력하세요.: 3424
x[3]값을 입력하세요.: 2323
x[4]값을 입력하세요.: 1111
최댓값은 3424입니다.
```

```python
# 배열 원소의 최댓값을 구해서 출력하기 (원솟값을 입력받음)

from max import max_of  # max.py 에서 max_of() 을 임포트

print('배열의 최댓값을 구합니다.')
print('주의: "End"를 입력하면 종료합니다.')

number = 0
x= []

while True:
    s = input(f'x[{number}]값을 입력하세요.: ')
    if s == 'End':
        break
    x.append(int(s))
    number += 1

print(f'{number}개를 입력했습니다.')
print(f'최대값은 {max_of(x)}입니다.')
```

```python
배열의 최댓값을 구합니다.
주의: "End"를 입력하면 종료합니다.
x[0]값을 입력하세요.: 3
x[1]값을 입력하세요.: 4
x[2]값을 입력하세요.: 2
x[3]값을 입력하세요.: 7
x[4]값을 입력하세요.: 10
x[5]값을 입력하세요.: 21
x[6]값을 입력하세요.: End
6개를 입력했습니다.
최대값은 21입니다.
```

### 리스트 스캔

```python
# 리스트의 모든 원소를 enumerate 함수로 스캔하기

x = ['John', 'George', 'Paul', 'Ringo']

for i, name in enumerate(x):
    print(f'x[{i}] = {name}')
```

```python
# 리스트의 모든 요소를 enumerate 함수로 스캔(1부터 카운트)

x = ['John', 'George', 'Paul', 'Ringo']

for i, name in enumerate(x, 1):
    print(f'{i}번째 = {name}')
```

### 이터러블

문자열, 리스트, 튜플, 집합, 딕셔너리 등의 자료형 객체는 모두 이터러블 하다는 공통점이 있습니다. 이터러블 객체는 원소를 하나씩 꺼내는 구조이며, 이터러블 객체를 내장 함수 인 iter( )의 인수로 전달하면 그 객체에 대한 이터레이터를 반환합니다. 이터레이터는 데이터의 나열을 표현하는 객체입니다. 이터레이터의 _ _ next () _ _ 함수를 호출하거나 내장 함수인 next( ) 함수에 이터레이터를 전달하면 원소를 순차적으로 꺼낼 수 있습니다. 꺼낼 원소가 더 이상 없는 경우에는 StopIteration 으로 예외 발생을 시킵니다. 

### 리스트 컴프리헨션

```python
n = 3
m = 4

# 리스트 컴프리헨션으로 2차원 리스트 만들기
lc_array = [[0] * m for _ in range(n)]
lc_array[0][3] = 4
print(lc_array)

# 일반적인 2차원 리스트 만들기
array = [[0] * m] * n
array[0][3] = 4
print(array1)

# 서로 다른값이 나오기 때문에 **리스트를 초기화 할땐** 반드시 리스트 컴프리헨션을 사용해야한다.
```

```python
실행값: 

ls_array = [[0, 0, 0, 4], [0, 0, 0, 0], [0, 0, 0, 0]]

array = [[0, 0, 0, 4], [0, 0, 0, 4], [0, 0, 0, 4]]
```

### 특정한 값의 원소를 모두 제거하기

```python
a = [1,2,3,4,5,5,5]
remove_set = {3, 5} # 제거하고 싶은 숫자 세트

# remove_set 에 포함되지 않은 값만을 저장
result = [i for i in a if i not in remove_set]  # 리스트 a 에서 remove_set 요소를 모두 제거
print(result)
```

```python
>>> [1, 2, 4]
```

다른 프로그래밍 언어에서는 remove_all()과 같은 함수로 간단하게 특정한 값을 가지는 모든 원소를 제거할 수 있다. 하지만 파이썬의 경우 그러한 함수를 기본적으로 제공하지 않으므로 위 방법과 같이 이용하면 좋다.

### 문자열 연산

```python
a = "Hello"
b = "World"

print(a + " " + b)

>>> Hello World
```

```python
a = "String"

print(a * 3)

>>> StringStringString
```

```python
a = "ABCDEF"

print(a[2:4]) # 슬라이싱에서는 인덱스 2이상 4미만 이라고 외우면 쉽다

>>> CD 
```

### 사전 자료형 관련 함수

```python
data = dict()
data['사과'] = 'Apple'
data['바나나'] = 'Banana'
data['코코넛'] = 'Coconut'

# 키 데이터만 담은 리스트
key_list = data.keys()

# 값 데이터만 담은 리스트
value_list = data.values()

print(key_list)
print(value_list)

# 각 키에 따른 값을 하나씩 출력
for key in key_list:
    print(data[key])

# 실행값 
dict_keys(['사과', '바나나', '코코넛'])
dict_values(['Apple', 'Banana', 'Coconut'])
Apple
Banana
Coconut
```

### 집합 자료형의 연산

파이썬은 집합 자료형의 연산에 대해서 다루고 있다. 집합 자료형 데이터 사이에서 합집합을 계산할 때는 ‘|’ 를 이용한다. 또한 교집합은 ‘&’, 차집합은 ‘-’ 를 이용한다. 

```python
a = set([1, 2, 3, 4, 5])
b = set([3, 4, 5, 6, 7])

print(a | b)  # 합집합
print(a & b)  # 교집합
print(a - b)  # 차집합

# 실행값 
{1, 2, 3, 4, 5, 6, 7}
{3, 4, 5}
{1, 2}
```

### 집합 자료형 관련 함수

```python
data = set([1, 2, 3])
print(data)

# 새로운 원소 추가
data.add(4)
print(data)

# 새로운 원소 여러 개 추가
data.update([5,6])
print(data)

# 특정한 값을 갖는 원소 삭제
data.remove(3)
print(data)

# 실행값
{1, 2, 3}
{1, 2, 3, 4}
{1, 2, 3, 4, 5, 6}
{1, 2, 4, 5, 6}
```