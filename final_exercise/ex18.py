# 18. 문자열 검색
# 다음 코드의 결과값이 무엇인지 알아 보자.

import re

p = re.compile('[a-z]+')
m = p.search('5 python')

result = m.start() + m.end()
print(result)