# 다음과 같은 내용을 지난 파일 test.txt가 있다. 이 파일의 내용 중 'java'라는 문자열을 'python'으로 바꾸어서 저장해 보자.
"""
< 내용 >
Life is too short
you need java
"""

# 주석 아닌 거 : 내가 한 거 / 주석인 거 : 답지
f = open("test.txt", 'r')
body = f.readlines()
#body = f.read()
f.close()

body = body[0] + body[1].replace('java','python')
#body = body.replace('java', 'python')

f = open("test.txt", 'w')
f.write(body)
f.close()