# (06-5) 탭을 4개의 공백으로 바꾸기
# 문서 파일을 읽어서 그 문서 파일 안에 있는 탭(tab)을 공백(space) 4개로 바꾸어 주는 스크립트를 작성해 보자.
# 필요한 기능 : 문서 파일 읽어 들이기, 문자열 변경하기
# 입력 값 : 탭을 포함한 문서 파일 (src)
# 출력 값 : 탭이 공백으로 수정된 문서 파일 (dst)

import sys

src = sys.argv[1]
dst = sys.argv[2]

f = open(src, 'r')
tab_content = f.read()
f.close()

space_content = tab_content.replace("\t", "-"*4) # 확인이 쉽도록 공백 대신 하이픈(-) 사용

f = open(dst, 'w')
f.write(space_content)
f.close()

print(space_content)