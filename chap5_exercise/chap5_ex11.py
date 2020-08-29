# glob 모듈을 사용하여 python_ex/chap5 디렉터리의 파일 중 확장자가 .py인 파일만 출력하는 프로그램을 작성해 보자.

import glob

print(glob.glob("/Users/kimhuiju/Desktop/python_ex/chap5/*.py")) # glob.glob(pathname)는 파일을 리스트로만 만들어주기 때문에 print를 해줘야 함.