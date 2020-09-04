# 15. Duplicate Numbers
# 0~9의 문자로 된 숫자를 입력받았을 때, 이 입력값이 0~9의 모든 숫자를 각각 한 번씩만 사용한 것인지 확인하는 함수를 작성해 보자.

def chkDupNum(s):
    result = []
    for num in s:
        if num not in result:
            result.append(num)
        else:
            return False # 중복되는 값이 있다면 False 반환
    return len(result) == 10 # 0~9 모두 있으면 True, 없으면 False

print(chkDupNum("0123456789"))
print(chkDupNum("01234"))