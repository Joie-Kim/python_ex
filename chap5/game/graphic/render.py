# render.py

# from game.sound.echo import echo_test
from ..sound.echo import echo_test # ..는 부모 디렉토리를 의미. graphic과 sound는 동일한 깊이(deep)이기 때문에 부모 디렉토리 사용 가능
def render_test():
    print("render")
    echo_test()
