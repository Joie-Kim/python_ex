# (06-3) 게시판 페이징 하기
# 게시물의 총 건수와 한 페이지에 보여줄 게시물 수를 입력으로 받고, 총 페이지 수를 출력하는 프로그램을 만들어 보자.
# 함수 이름 : getTotalPage
# 입력 값 : 게시물의 총 건수(m), 한 페이지에 보여 줄 게시물 수(n)
# 출력 값 : 총 페이지 수

def getTotalPage(m,n):
    if m % n == 0:
        tPage = m // n # m을 n으로 나눌 때 소수점 아래 자리를 버리기 위해 '/' 대신에 '//' 사용
    else:
        tPage = m // n + 1
    return tPage

m = int(input("게시물의 총 건수 : "))
n = int(input("한 페이지에 보여 줄 게시물 수 : "))

print(getTotalPage(m,n))