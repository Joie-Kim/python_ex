# (06-2) 3과 5의 배수 합하기
# 10 미만의 자연수에서 3과 5의 배수를 구하면 3, 5, 6, 9이다. 이들의 총합은 23이다.
# 1000 미만의 자연수에서 3의 배수와 5의 배수의 총합을 구하라.

result = [] # 3 또는 5의 배수를 저장할 리스트
sum = 0 # 3 또는 5의 배수의 합을 저장할 변수
for num in range(1, 1000):
    if num % 3 == 0 or num % 5 == 0:
        result.append(num)
        sum += num

print(result)
print(sum)