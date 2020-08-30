# (06-6) 하위 디렉터리 검색하기
# 특정 디렉터리부터 시작해서 그 하위 모든 파일 중 파이썬 파일(.py)만 출력해 주는 프로그램을 만들어 보자.

import os

def search(dirname):
    try:
        filenames = os.listdir(dirname) # 해당 디렉터리에 있는 파일들의 리스트를 구할 수 있다. (파일 이름만 포함)
        for filename in filenames:
            full_filename = os.path.join(dirname, filename) # 파일 경로를 포함한 파일 이름을 구하기 위해 입력 받은 dirname을 덧붙인다.
            if os.path.isdir(full_filename): # full_filename이 디렉터리라면 그 안으로 들어감 (재귀 호출)
                search(full_filename)
            else: # full_filename이 디렉터리가 아니라면 확장자 확인
                ext = os.path.splitext(full_filename)[-1] # 확장자를 기준으로 두 부분으로 나누어 준다. [-1]이기 때문에 가장 마지막 값인 확장자를 뜻한다.
                if ext == '.py':
                    print(full_filename)
    except PermissionError: pass # os.listdir를 수행할 때, 권한이 없는 디렉터리에 접근하더라도 프로그램이 오류로 종료되지 않도록
search("/Users/kimhuiju/Desktop/python_ex/chap5")