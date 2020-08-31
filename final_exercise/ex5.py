# 5. 피보나치 함수
# 첫 번째 항의 값이 0이고, 두 번째 항의 값이 1일 때, 이후에 이어지는 항은 이전의 두 항을 더한 값으로 이루어지는 수열을 피보나치 수열이라고 한다.
# 입력을 정수 n으로 받았을 때, n 이하까지의 피보나치 수열을 출력하는 함수를 작성해 보자.

n = int(input("정수 입력 : "))

result = [] # 피보나치 수열 결과 저장할 리스트
result.append(0) # 첫 번째 항의 값은 0
result.append(1) # 두 번째 항의 값은 1
i = 1 # 항의 순서를 나타낼 변수

while True:
    temp = result[i-1] + result[i]
    if temp > n: break
    result.append(temp)
    i += 1

print(result)
     