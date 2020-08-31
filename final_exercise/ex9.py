# 9. 평균값 구하기
# sample.txt 파일의 숫자 값을 모두 읽어 총합과 평균 값을 구한 후, 평균 값을 result.txt 파일에 쓰도록 하자.

# (1) 파일 읽기
f = open("./final_exercise/sample.txt", 'r')
list = f.readlines()
f.close()

# (2) 총합과 평균 값 구하기
total = 0
for value in list:
    score = int(value)
    total += score
avg = total / len(list)

# (3) 평균 값 파일에 쓰기
f = open("./final_exercise/result.txt", 'w')
# f.write(avg) # TypeError : 파일에 쓸 수 있는 데이터는 문자열! 
f.write(str(avg))
f.close()