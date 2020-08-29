# map과 lambda를 사용하여 [1, 2, 3, 4] 리스트의 각 요솟값에 3이 곱해진 리스트 [3, 6, 9, 12]를 만들어 보자.

# 1. 아무것도 사용 x
"""
def three_times(li):
    result = []
    for i in li:
        result.append(i*3)
    return result

print(three_times([1, 2, 3, 4]))
"""

# 2. map 사용
"""
def three_times(x):
    return x * 3

print(list(map(three_times, [1, 2, 3, 4])))
"""

# 3. map & lambda 사용
print(list(map(lambda x: x * 3, [1, 2, 3, 4])))