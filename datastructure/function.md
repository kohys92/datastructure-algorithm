
# 함수 function
### global 키워드

함수 안에서 함수 밖의 변수 데이터를 변경해야 하는 경우가 있다. 이때는 함수에서 `global` 키워드를 이용하면 된다. `global` 키워드로 변수를 지정하면, 해당 함수에서는 지역 변수를 만들지 않고, 함수 바깥에 선언된 변수를 바로 참조하게 된다. 

```python
a = 0

def func():
    global a  # 여기서 global 을 사용함으로써 함수밖의 a 를 참조하게 된다
    a += 1

for i in range(10):
    func()

print(a)

# 실행값
10
```

### 람다 Lambda Expression

파이썬에서는 람다 표현식을 사용할 수 있다. 람다 표현식을 이용하면 함수를 매우 간단하게 작성하여 적용할 수 있다. 특정한 기능을 수행하는 함수를 한 줄에 작성할 수 있다는 점이 특징이다. 

```python
def add(a, b):
    return a + b

# 일반적인 add() 메서드 사용
print(add(3, 7))

# 람다 표현식으로 구현한 add() 메서드
print((lambda a, b: a+b)(3, 7))

#실행값
10
10
```