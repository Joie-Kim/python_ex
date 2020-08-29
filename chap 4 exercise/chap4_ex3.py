# 다음은 두 개의 숫자를 입력받아 더하여 돌려주는 프로그램이다.
"""
input1 = input("first number: ")
input2 = input("second number: ")

total = input1 + input2
print("sum is %s.." % total)
"""
# 3과 6을 입력했을 때, 9가 아니라 36이라는 결과값을 돌려준다. 이 프로그램의 오류를 수정해 보자.

input1 = input("first number: ")
input2 = input("second number: ")

total = int(input1) + int(input2)
print("sum is %d.." % total)