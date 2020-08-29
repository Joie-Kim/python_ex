# adddata.py

f = open("new_file.txt", 'a')
for i in range(11,21):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()