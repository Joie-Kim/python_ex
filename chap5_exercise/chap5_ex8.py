# 17/3 의 결과를 소수점 4자리까지만 반올림하여 표시해 보자.

result = 17 / 3
print(result)
print(round(result)) # 뒤에 인자가 없으면 실수를 정수로 변환
print(round(result, 4)) # 뒤에 인자가 있으면 그 만큼만 반올림 해서 표시