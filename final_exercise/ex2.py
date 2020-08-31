# 2. 딕셔너리 값 추출하기
# a 딕셔너리에 'C' key가 없기 때문에 KeyError가 발생한다.
# key 값을 'C'로 했을 때, 오류 대신 70을 출력해 보자.

a = {'A':90, 'B':80}

# print(a['C']) # KeyError
print(a.get('C', 'Error')) # get 함수 사용.