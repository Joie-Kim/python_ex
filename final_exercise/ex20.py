# 20. 전방 탐색
# 긍정형 전방 탐색 기법을 사용하여 .com, .net이 아닌 이메일 주소는 제외시키는 정규식을 작성해 보자.

import re

p = re.compile('.*[@].*[.](?=com$|net$).*$')
# a*b : a가 0번 이상 반복됨 / b, ab, aab, aaab, aaaab
# a+b : a가 1번 이상 반복 됨 / ab, aab, aaab, aaaab
# (?=...) : 긍정형 전반 탐색 기법 / ... 정규식에 해당되는 게 나오면 통과
# ab$ : ab가 문자열 끝에 있음

print(p.match('joie.huiju@gamil.com'))
print(p.match('huiju@daum.net'))
print(p.match('huijoo@kakao.co.kr'))

