# sub_dir_search.py 의 기능과 동일한 기능을 하지만, 좀 더 쉬운 방법
# os.walk를 사용해 보자.
# os.walk : 시작 디렉터리부터 그 하위 모든 디렉터리를 차례대로 방문하게 해주는 함수

import os

for (path, dir, files) in os.walk("/Users/kimhuiju/Desktop/python_ex/chap5/"):
    for filename in files:
        ext = os.path.splitext(filename)[-1]
        if ext == '.py':
            print("%s/%s" %(path, filename))