# 다음은 "test.txt"라는 파일에 "Life is too short" 문자열을 저장한 후 다시 그 파일을 읽어서 출력하는 프로그램이다.
"""
f1 = open("test.txt", 'w')
f1.write("Life is too short")

f2 = open("test.txt", 'r')
print(f2.read())
"""
# 이 프로그램은 문자열을 출력하지 않는다. 출력할 수 있도록 프로그램을 수정해 보자.

f1 = open("test.txt", 'w')
f1.write("Life is too short")
f1.close() # 파일을 닫지 않고, 다시 열면 파일에 저장한 데이터를 읽을 수 없다.

f2 = open("test.txt", 'r')
print(f2.read())
f2.close()