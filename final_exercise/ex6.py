# 6. 숫자의 총합 구하기
# 사용자로부터 숫자를 입력받아 그것의 총합을 구하는 프로그램을 작성해 보자.
# 단, 숫자는 콤마로 구분하여 입력

str_numbers = input("숫자 입력 (콤마로 구분) : ")

numbers = str_numbers.split(",")

sum = 0
for number in numbers:
    sum += int(number)

print(sum)