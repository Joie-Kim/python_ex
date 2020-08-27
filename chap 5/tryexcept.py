# try-except문 활용
try:
    4 / 0
except ZeroDivisionError as e:
    print(e)

# IndexError가 발생할 때 오류 메시지를 출력하는 소스 작성
a = [1, 2, 3]
try:
    print(a[4])
except IndexError as e:
    print(e)

# try-finally문 활용
"""
f = open('foo.txt', 'w')
try:
    # do something
finally:
    f.close()
"""

# 여러 개의 예외 처리
try:
    a = [1, 2, 3]
    print(a[4])
    4/0
except ZeroDivisionError as e:
    print(e)
except IndexError as e:
    print(e)

# 여러 개의 예외 처리 (2)
# ZeroDivisionError, IndexError 함께 처리
try:
    a = [1,2,3]
    print(a[4])
    4/0
except (ZeroDivisionError, IndexError) as e:
    print(e)

# 오류 회피 하기
try:
    f = open("blablabla", 'r')
except FileNotFoundError:
    pass