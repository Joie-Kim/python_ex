# 주어진 자연수가 홀수인지 짝수인지 판별해 주는 함수(is_odd)를 작성해 보자.

def if_odd(num):
    if num % 2 == 1:
        return True
    else:
        return False

test = if_odd(6)
print(test)