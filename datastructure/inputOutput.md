# 입출력
### 데이터를 입력 받을 때

여러 개의 데이터를 입력받을 때는 데이터가 공백으로 구분되는 경우가 많다. 그래서 입력받은 문자열을 띄어쓰기로 구분하여 각각 정수 자료형의 데이터로 저장하는 코드의 사용 빈도가 매우 높다. 

이때는 `list(map(int, input().split()))` 을 이용하면 된다.

```python
n = int(input)

data = list(map(int, input().split()))

data.sort(reverse = True)
print(data)

# 입력 예시
5 
65 90 75 34 99
# 출력 예시
[99 90 75 65 34]
```

`list(map(int, input().split()))` 의 동작 과정을 알아보자. 가장 먼저 `input()` 으로 입력받은 문자열을 `split()` 을 이용해 공백으로 나눈 리스트로 바꾼 뒤에, `map` 을 이용하여 해당 리스트의 모든 원소에 `int()` 함수를 적용한다. 최종적으로 그 결과를 `list()` 로 다시 바꿈으로써 입력받은 문자열을 띄어쓰기로 구분하여 각각 숫자 자료형으로 저장하게 되는 것이다. **이 코드는 정말 많이 사용되므로, 반드시 외우고 있어야 한다.**

**공백을 기준으로 구분하여 적은 수의 데이터 입력**

```python
n, m, k = map(int, input().split())

print(n, m, k)

# 입력
3 5 7

# 실행 
3 5 7
```

입력의 개수가 많은 경우에는 단순히 `input()` 함수를 그대로 사용하지는 않는다. 파이썬의 기본 `input()` 함수는 동작 속도가 느려서 시간 초과로 오답 판정을 받을 수 있기 때문이다. 이 경우 파이썬의 sys 라이브러리에 정의되어 있는 `sys.stdin.readline()` 함수를 이용한다. sys 라이브러리는 다음과 같은 방식으로 사용하며 `input()` 함수와 같이 한 줄씩 입력받기 위해 사용한다.

```python
import sys
sys.stdin.readline().rstrip()
```

sys 라이브러리를 사용할 때는 한 줄 입력을 받고 나서 `rstrip()` 함수를 꼭 호출해야 한다. 

`readline()` 으로 입력하면 입력 후 엔터가 줄 바꿈 기호로 입력되는데, 이 공백 문자를 제거하려면 `rstrip()` 함수를 사용해야 한다. 

```python
# readline() 사용 소스코드 예시

import sys

data = sys.stdin.readline().rstrip()
print(data)

# 입력 예제
Hello World
# 출력
Hello World
```

**출력 시 오류가 발생하는 소스코드 예시**

```python
# 출력할 변수들 
answer = 7

print("정답은 " + answer + "입니다.")
```

```python
TypeError: can only concatenate str (not "int") to str
```

이 경우 두가지 해결 방법이 있다. `str()` 함수를 이용하여 출력하고자 하는 변수 데이터를 문자열로 바꾸어주거나, 혹은 각 자료형을 콤마(,) 를 기준으로 구분하여 출력하면 된다.

```python
answer = 7

# 해결방법 1
print("정답은 " + str(answer) + "입니다.")
# 해결방법 2
print("정답은 ", answer, "입니다.")

# 파이썬 3.6 이상의 버전: f-string 문법
print(f"정답은 {answer} 입니다.".format(answer))
```