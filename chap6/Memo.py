# (06-4) 간단한 메모장 만들기
# 원하는 메모를 파일에 저장하고 추가 및 조회가 가능한 간단한 메모장을 만들어 보자.
# 필요한 기능 : 메모 추가하기(a), 메모 조회하기(v)
# 입력 값 : 메모 내용, 프로그램 실행 옵션
# 출력 값 : memo.txt

import sys

option = sys.argv[1]

if option == '-a': # 메모 추가
    memo = sys.argv[2]
    f = open('memo.txt', 'a') # 덮어쓰기 해야 하기 때문에 'a'
    f.write(memo)
    f.write('\n')
    f.close()

elif option == '-v':
    f = open('memo.txt', 'r') # 읽기 모드
    memo = f.read()
    f.close()
    print(memo)
