 # 13. DashInsert
 # 숫자로 구성된 문자열을 입력받은 뒤 문자열 안에서 홀수가 연속되면 두 수 사이에 -를 추가하고,
 # 짝수가 연속되면 *를 추가하는 기능을 구현해 보자.

input_data = input()
try: # 예외처리 연습
    numbers = list(map(int, input_data)) # 각 문자를 정수로 변환. 리스트로 만듦
    print(numbers)
except ValueError as e:
    print(e)

result = [] # 결과 저장 리스트
for i, number in enumerate(numbers): # enumerate : 리스트의 인덱스와 값을 반환
    result.append(str(number)) # 나중에 join을 쓰기 위해
    if i < len(numbers)-1: # 마지막 숫자가 아닐 때
        if numbers[i] % 2 == 0 and numbers[i+1] % 2 == 0: # 연속 짝수
                result.append('*')
        elif numbers[i] % 2 != 0 and numbers[i+1] % 2 != 0: # 연속 홀수
                result.append('-')

print("".join(result)) # 문자열로 만듦 (정수형은 사용할 수 없음. 문자형만 됨.)
