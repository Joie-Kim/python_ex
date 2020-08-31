# 10. 사칙연산 계산기
# 다음과 같이 동작하는 클래스 Calculator를 작성해 보자.
"""
cal1 = Calculator([1,2,3,4,5])
print(cal1.sum()) # 15
print(cal1.avg()) # 3.0
"""

class Calculator():
    def __init__(self, list):
        self.list = list
    def sum(self):
        result = 0
        for num in self.list:
            result += num
        return result
    def avg(self):
        total = self.sum()
        return total / len(self.list)

cal1 = Calculator([1,2,3,4,5])
print(cal1.sum())
print(cal1.avg())