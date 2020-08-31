# 1. 문자열 바꾸기
# split와 join 함수를 사용하여, 'a:b:c:d' 문자열을 'a#b#c#d'로 고쳐 보자.

a = 'a:b:c:d'
b = a.split(':')
a = '#'.join(b)
print(a)