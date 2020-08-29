# filter와 lambda를 사용하여 리스트 [1, -2, 3, -5, 8, -3]에서 음수를 모두 제거해 보자.

# 1. 아무것도 사용 x
"""
def is_positive(li):
    result = []
    for i in li:
        if i > 0:
            result.append(i)
    return result

print(is_positive([1, -2, 3, -5, 8, -3]))
"""

# 2. filter 사용
"""
def is_positive(x):
    return x > 0

print(list(filter(is_positive, [1, -2, 3, -5, 8, -3])))
"""

# 3. filter & lambda 사용
print(list(filter(lambda x: x > 0, [1, -2, 3, -5, 8, -3])))