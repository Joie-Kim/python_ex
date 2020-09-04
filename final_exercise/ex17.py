# 17. 기초 메타 문자
# 정규식 a[.]{3,}b 와 매치되는 문자열을 찾아 보자.

import re # 정규식 사용을 위한 모듈

p = re.compile('a[.]{3,}b') # 정규식 컴파일

print(p.match('acccb')) # p.match() : 정규식 매치 결과 확인
print(p.match('a..b'))
print(p.match('a...b'))
print(p.match('a....b'))
print(p.match('aaab'))
print(p.match('a.cccb'))

# a[.]b : 'a' + '.' + 'b'
# a.b : a와 b 사이에 어떤 문자가 와도 상관 없음
# a{3}b : a를 반드시 3번 반복 / aaab
# a{3,5}b : a를 3 ~ 5번 반복 / aaab, aaaab, aaaaab
# a{3,}b : a를 3번 이상 반복