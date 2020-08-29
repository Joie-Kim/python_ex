# 외장함수 sys.argv를 사용해서 실행할 때 입력값을 모두 더하여 출력해 보자.

import sys

numbers = sys.argv[1:]# 파일 이름을 제외한 명령 행의 모든 입력
result = 0
for number in numbers:
    result += int(number)
print(result)

# ------------------------------------
# 처음엔 이렇게 짰는데. TypeError가 발생했다.
# 이유는 더하기 연산자(+)를 수행할 때, 산술 연산인지 (문자열)결합 연산인지 정해지지 않았기 때문이다.
# 따라서 꼭 자료형을 지정 해줘야 했다. 문제에서는 정수의 합이었기 때문에 int() 함수를 사용했다.
"""
result = 0
for values in sys.argv:
    result = result + values
print(result)
"""
# ------------------------------------
# int() 함수를 추가 했으나, 이번에는 ValueError가 발생했다.
# 이유는 바로 sys.argv 배열에 들어가는 값 때문이었다.
# sys.argv[0]은 항상 실행되는 파일의 이름(chap5_ex9.py)이 들어간다. 따라서 int() 함수에서 오류가 발생했다.
"""
result = 0
for values in sys.argv:
    result += int(values)
print(result)
"""
# ------------------------------------