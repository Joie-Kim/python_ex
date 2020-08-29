# random 모듈을 사용하여 로또 번호(1~45 사이의 숫자 6개)를 생성해 보자.

import random

result = []
for i in range(0,6):
    number = random.randint(1, 45) # 1 ~ 45 사이의 난수 발생
    result.append(number) # 리스트에 값 넣을 때는 list.append()를 사용하자!

print(result)

# ------------------------------------
# 처음엔 이렇게 코드를 짰는데..
# 배열에 숫자가 들어가지 않았다. 리스트에 값을 이렇게 넣으면 안 되는 군!
# IndexError: list assignment index out of range
"""
result = []
for i in range(0,6):
    result[i] = random.randint(1, 45)

print(result)
"""
# ------------------------------------
# 풀이에서는 for 문이 아니라, while 문을 사용했다.
"""
result = []
while len(result) < 6:
    number = random.randint(1, 45)
    result.append(number)

print(result)
"""