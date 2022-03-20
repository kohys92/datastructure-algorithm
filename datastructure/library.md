# 주요 라이브러리의 문법과 주의점
- 내장함수: print(), input() 과 같은 기본 입출력 기능부터 sorted() 와 같은 정렬 기능을 포함하고 있는 기본 내장 라이브러리이다. 파이썬 프로그램을 작성할 때 없어서는 안 되는 필수적인 기능을 포함하고 있다.
- itertools: 파이썬에서 반복되는 형태의 데이터를 처리하는 기능을 제공하는 라이브러리이다. 순열과 조합 라이브러리를 제공한다.
- heapq: 힙(Heap) 기능을 제공하는 라이브러리이다. 우선순위 큐 기능을 구현하기 위해 사용한다.
- bisect: 이진 탐색 (Binary Search) 기능을 제공하는 라이브러리이다.
- collections: 덱(deque), 카운터(Counter) 등의 유용한 자료구조를 포함하고 있는 라이브러리이다.
- math: 필수적인 수학적 기능을 제공하는 라이브러리이다. 팩토리얼, 제곱근, 최대공약수(GCD), 삼각함수 관련 함수부터 파이(pi)와 같은 상수를 포함하고 있다.

### 내장함수

대표적인 `print()` `input()` 을 제외하고 `sum()` 함수는 리스트와 같은 iterable 객체가 입력으로 주어졌을 때, 모든 원소의 합을 반환한다. 

```python
result = sum([1,2,3,4,5])
print(result)

>>> 15 
```

`min()` `max()` 

```python
result = min(7,3,5,2])
print(result)

>>> 2 

result = max(7,3,5,2])
print(result)

>>> 7
```

`eval()` 함수는 수학 수식이 문자열 형식으로 들어오면 해당 수식을 계산한 결과를 반환한다. 예를들어 문자열 형태로 주어진 수식 `(3+5) * 7` 을 계산하는 소스코드는 다음과 같다.

```python
result = eval("(3 + 5) * 7")
print(result)

>>> 56
```

`sorted()` 함수는 iterable 객체가 들어왔을 때, 정렬된 결과를 반환한다. key 속성으로 정렬 기준을 명시할 수 있으며, reverse 속성으로 정렬된 결과 리스트를 뒤집을지의 여부를 설정할 수 있다. 

```python
result = sorted([9,1,8,5,4])
print(result)

>>> [1,4,5,8,9]

result = sorted([9,1,8,5,4], reverse = True)
print(result)

>>> [9,8,5,4,1]
```

파이썬에서는 리스트의 원소로 리스트나 튜플이 존재할 때 특정한 기준에 따라서 정렬을 수행할 수 있다. 정렬 기준은 key 속성을 이용해 명시할 수 있다. 예를 들어 리스트 `[('홍길동',35), ('이순신',75), ('아무개', 50)]` 이 있을 때, 원소를 튜플의 두 번째 원소(수)를 기준으로 내림차순으로 정렬하고자 한다면 다음과 같이 사용할 수 있다.

```python
result = sorted([('홍길동',35), ('이순신',75), ('아무개', 50)], 
												key = lambda x: x[1], reverse = True))
print(result)

>>> [('이순신',75), ('아무개', 50), ('홍길동',35)]
```

- 리스트와 같은 `iterable` 객체는 기본으로 `sort()` 함수를 내장하고 있어서 굳이 `sorted()` 함수를 사용하지 않고도 `sort()` 함수를 사용해서 정렬할 수 있다.

## itertools

`itertools` 는 파이썬에서 반복되는 데이터를 처리하는 기능을 포함하고 있는 라이브러리이다. 코딩 테스트에서 가장 유용하게 사용할 수 있는 클래스는 `permutations`  , `combinations`이다. 

### permutations

`permutations` 는 리스트와 같은 `iterable` 객체에서 r 개의 데이터를 뽑아 일렬로 나열하는 모든 경우(순열)를 계산해준다. `permutations` 는 클래스이므로 객체 초기화 이후에는 리스트 자료형으로 변환하여 사용한다. 리스트 `['A', 'B', 'C']` 에서 3개(r = 3)를 뽑아 나열하는 모든 경우를 출력하는 예시는 다음과 같다.

```python
from itertools import permutations

data = ['A', 'B', 'C'] # 데이터 준비
result = list(permutations(data,3)) # 모든 순열 구하기

print(result)

>>> [('A', 'B', 'C'), ('A', 'C', 'B'), ('B', 'A', 'C'), ('B', 'C', 'A'), ('C', 'A', 'B'), ('C', 'B', 'A')]
```

### combinations

`combinations` 는 리스트와 같은 `iterable` 객체에서 r 개의 데이터를 뽑아 순서를 고려하지 않고 나열하는 모든 경우 (조합)를 계산한다. `combinations` 는 클래스이므로 객체 초기화 이후에는 리스트 자료형으로 변화하여 사용한다. 리스트 `['A', 'B', 'C']` 에서 2개(r=2)를 뽑아 순서에 상관없이 나열하는 모든 경우를 출력하는 예시는 다음과 같다. 

```python
from itertools import combinations

data = ['A', 'B', 'C'] # 데이터 준비
result = list(combinations(data,2))  # 2개를 뽑는 모든 조합 구하기

print(result)

>>> [('A', 'B'), ('A', 'C'), ('B', 'C')]
```

### product

`product` 는 `permutations` 와 같이 리스트와 같은 iterable 객체에서 r개의 데이터를 뽑아 일렬로 나열하는 모든 경우(순열)를 계산한다. `다만 원소를 중복하여 뽑는다`. `product` 객체를 초기화 할 때는 뽑고자 하는 데이터의 수를 repeat 속성값으로 넣어준다. `prodcut` 는 클래스이므로 객체 초기화 이후에는 리스트 자료형으로 변환하여 사용한다. 리스트 ['A', 'B', 'C'] 에서 중복을 포함하여 2개 (r=2)를 뽑아 나열하는 모든 경우를 출력하는 예시는 다음과 같다. 

```python
from itertools import product

data = ['A', 'B', 'C'] # 데이터 준비
result = list(product(data, repeat = 2))  # 2개를 뽑는 모든 순열 구하기 (중복 허용)

print(result)

>>> [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'B'), ('B', 'C'), ('C', 'A'), ('C', 'B'), ('C', 'C')]
```

### heapq

파이썬에서는 힙 `heap` 기능을 위해 `heapq` 라이브러리를 제공한다. `heapq`는 `다익스트라` 최단 경로 알고리즘을 포함해 다양한 알고리즘에서 우선순위 큐 기능을 구현하고자 할 때 사용한다. 

파이썬의 `힙`은 최소 힙 `min heap` 으로 구성되어 있으므로 단순히 원소를 `힙`에 전부 넣었다가 빼는 것만으로도 시간 복잡도 `O(NlogN)` 에 `오름차순` 정렬이 완료된다. 보통 최소 힙 자료구조의 `최상단 원소는 항상 ‘가장 작은' 원소`이기 때문이다. 

힙에 원소를 삽입할 때는 `heapq.heappush()` 메서드를 이용하고, `힙`에서 원소를 꺼내고자 할 때는 `heapq.heappop()` 메서드를 이용한다. 힙 정렬 `heap sort`을 `heapq`로 구현하는 예제를 통해 `heapq`의 사용 방법을 알아보자. 

```python
import heapq

def heapsort(iterable):
    h = []
    result = []

    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, value)

    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for _ in range(len(h)):
        result.append(heapq.heappop(h))
    return result

if __name__ == '__main__':
    result = heapsort([1,3,5,7,9,2,4,6,8,0])
    print(result)

>>> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

파이썬에서는 최대 힙 `Max Heap` 을 제공하지 않는다. 따라서 `heapq 라이브러리`를 이용하여 최대 `힙`을 구현해야 할 때는 원소의 부호를 임시로 변경하는 방식을 사용한다. `힙`의 원소를 삽입하기 전에 잠시 부호를 반대로 바꾸었다가, `힙`에서 원소를 꺼낸 뒤에 다시 원소의 부호를 바꾸면 된다. 이러한 방식으로 최대 `힙`을 구현하여 `내림차순` 힙 정렬을 구현하는 예시는 다음과 같다. 

```python
import heapq

def heapsort(iterable):
    h = []
    result = []

    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, -value)  # 부호를 - 로 바꿔준다

    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for _ in range(len(h)):
        result.append(-heapq.heappop(h))  # 부호를 - 로 바꿔준다
    return result

if __name__ == '__main__':
    result = heapsort([1,3,5,7,9,2,4,6,8,0])
    print(result)

>>> [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
```

### bisect

파이썬에서는 이진탐색 쉽게 구현할 수 있도록 `bisect` 라이브러리를 제공한다. `bisect` 라이브러리는 `‘정렬된 배열'`에서 특정한 원소를 찾아야 할 때 매우 효과적으로 사용된다. `bisect 라이브러리`에서는 `bisect_left()` 함수와 `bisect_right()` 함수가 가장 중요하게 사용되며, 이 두 함수는 시간 복잡도 `O(logN)`에 동작한다. 

- `bisect_left(a, x)`: 정렬된 순서를 유지하면서 리스트 a 에 데이터 x 를 삽입할 가장 왼쪽 인덱스를 찾는 메서드
- `bisect_right(a, x)`: 정렬된 순서를 유지하도록 리스트 a 에 데이터 x 를 삽입할 가장 오른쪽 인덱스를 찾는 메서드

예를 들어 정렬된 리스트 `[1, 2, 4, 4, 8]`이 있을 때, 새롭게 데이터 4 를 삽입하려 한다고 가정하자. 이때 `bisect_left(a, 4)`와 `bisect_right(a, 4)` 는 각각 인덱스값으로 2 와 4 를 반환한다.

```python
from bisect import bisect_left, bisect_right

a = [1, 2, 4, 4, 8]
x = 4

print(bisect_left(a, x))
print(bisect_right(a, x))

# 결과 
2
4
```

또한 `bisect_left()` 함수와 `bisect_right()` 함수는 ‘정렬된 리스트’에서 `‘값이 특정 범위에 속하는 원소의 개수'`를 구하고자 할 때, 효과적으로 사용될 수 있다. 

아래의 `count_by_range(a, left_value, right_value)` 함수를 확인해보자. 이는 정렬된 리스트에서 값이 `[left_value, right_value]`에 속하는 데이터의 개수를 반환한다. 다시 말해 원소의 값을 x 라고 할 때, `left_value ≤ x ≤ right_value` 인 원소의 개수를 `O(logN)` 으로 빠르게 계산할 수 있다. 

```python
from bisect import bisect_left, bisect_right

# 값이 [left_value, right_value] 인 데이터의 개수를 반환하는 함수
def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index

if __name__ == '__main__':

    # 리스트 선언
    a = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]

    # 값이 4인 데이터 개수 출력
    print(count_by_range(a, 4, 4))

    # 값이 [-1, 3] 범위에 있는 데이터 개수 출력
    print(count_by_range(a, -1, 3))
```

### collections - deque

파이썬의 collections 라이브러리는 유용한 자료구조를 제공하는 표준 라이브러리다. collections 라이브러리의 기능 중에서 코딩 테스트에서 유용하게 사용되는 클래스는 deque 와 Counter이다. 

보통 파이썬에서는 deque 를 사용해 큐를 구현한다. 별도로 제공되는 Queue 라이브러리가 있는데 일반적인 큐 자료구조를 구현하는 라이브러리는 아니다. 따라서 deque 를 이용해 큐를 구현해야 한다는 점을 기억하자.

deque 에서는 리스트 자료형과 다르게 인덱싱, 슬라이싱 등의 기능은 사용할 수 없다. 다만, 연속적으로 나열된 데이터의 시작 부분이나 끝부분에 데이터를 삽입하거나 삭제할 때는 매우 효과적으로 사용될 수 있다. deque 는 스택이나 큐의 기능을 모두 포함한다고도 볼 수 있기 때문에 스택 혹은 큐 자료구조의 대용으로 사용될 수 있다. 

deque 는 첫 번째 원소를 제거할 때 popleft() 를 사용하며, 마지막 원소를 제거할 때 pop() 을 사용한다. 또한 첫 번째 인덱스에 원소 x 를 삽입할 때 appendleft(x) 를 사용하며, 마지막 인덱스에 원소를 삽입할 때 append(x) 를 사용한다.

따라서 deque 를 큐 자료구조로 이용할 때, 원소를 삽입할 때에는 append() 를 사용하고 원소를 삭제할 때에는 popleft() 를 사용하면 된다. 그러면 먼저 들어온 원소가 항상 먼저 나가게 된다. 리스트 [2, 3, 4] 의 가장 앞쪽과 뒤쪽에 원소를 삽입하는 예시는 다음과 같다. 

```python
from collections import deque

data = deque([2,3,4])
data.appendleft(1)
data.append(5)

print(data)
print(list(data))  # 리스트 자료형으로 변환
```

### collections - Counter

파이썬 collections 라이브러리의 Counter 는 등장 횟수를 세는 기능을 제공한다. 구체적으로 리스트와 같은 iterable 객체가 주어졌을 때, 해당 객체 내부의 원소가 몇 번씩 등장했는지를 알려준다. 따라서 원소별 등장 횟수를 세는 기능이 필요할 때 짧은 소스코드로 구현할 수 있다. 

```python
from collections import Counter

counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])

print(counter['blue'])  # 'blue'가 등장한 횟수 출력
print(counter['green']) # 'green'이 등장한 횟수 출력
print(dict(counter))    # 사전 자료형으로 변화
```