# 8. 역순 저장
# abc.txt 파일의 내용을 역순으로 바꾸어 저장해 보자.

# (1) 파일을 읽어온다.
f = open("./final_exercise/abc.txt", 'r')
list = f.readlines()
# print(list) # 리스트에 담긴 내용 확인 (개행 문자가 함께 있다.)
f.close()

# print(len(list)) # 리스트 길이 구하려면 len(list) 해야 됨!! 잊지 말자.

# (2) 파일을 역순으로 바꾼다.
list.reverse()

# (3) 파일에 다시 저장
f = open("./final_exercise/abc.txt", 'w')
for value in list:
    value = value.strip('\n') # strip() : 뮨저열의 양 옆에 특정 문자가 있다면 지운다.
    f.write(value)
    f.write('\n')
f.close()