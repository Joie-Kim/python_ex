# (06-1) 내가 프로그램을 만들 수 있을까?
# 구구단 프로그램을 만들어 보자.
# 책에 나온 예제는 GuGu()를 실행할 때 인수에 따라 달라지도록 했다.
# 인수값을 사용자에게 입력 받는 걸로 변경 했다.
# 계속 반복해서 실행되도록 변경 했다.

def GuGu(n):
    result = []
    for i in range(1, 10):
        value = n * i
        result.append(value)
    return result

while 1:
    number = int(input("구구단 중 몇 단? ")) # 사용자에게 입력 받기
    if number not in range(2, 10): break # 2 ~ 9 외의 숫자를 입력하면 프로그램 종료
    print(GuGu(number))
