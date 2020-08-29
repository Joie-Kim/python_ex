# 오류 일부러 발생시키기

class Bird:
    def fly(self):
        raise NotImplementedError

class Eagle(Bird):
    def fly(slef):
        print("very fast!!!!")

eagle = Eagle()
eagle.fly()

