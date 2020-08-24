# writedata.py

f = open("new_file.txt", 'w')
for i in range(1, 11): #1부터 10까지 i에 대입
    data = "%d번째 줄입니다.\n" %i
    f.write(data) #파일에 data를 씀
f.close()
