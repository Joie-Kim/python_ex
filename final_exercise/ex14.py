# 14. 문자열 압축하기
# 문자열을 입력받아 같은 문자가 연속적으로 반복되는 경우에 그 반복 횟수를 표시해 문자열을 압축하여 표시해 보자.

string = input()

_c = "" # 비교 문자
cnt = 0 # 반복 횟수
result = "" # 결과 저장할 변수
for c in string:
    if c != _c: # 비교 문자랑 현재 문자가 다르면
        _c = c # 비교 문자를 현재 문자로 바꾸고
        if cnt: # 반복 횟수가 0이 아니면
            result += str(cnt) # 결과 문자열에 추가 
        result += c # 결과 문자열에 문자 추가
        cnt = 1 # 반복 횟수 1로 변경
    else: # 비교 문자랑 현재 문자가 같으면
        cnt += 1 # 반복 횟수 1 증가

if cnt: # 반복문 종료 후, 반복 횟수가 0이 아니면
    result += str(cnt) # 결과 문자열에 추가

print(result)