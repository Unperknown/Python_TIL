class cup():
    def __init__(self, name): # 속성 초기화
        self.name = name
    def hello(self): # 메서드 초기화
        print("Hi, I'm ", self.name, "!")

class mug(cup): # 상속할 클래스를 전달인자에 넣음
    def hello(self): # 메서드 오버라이드(재정의)
        print("Hello, I'm", self.name, ". But more like mug.")
    def make_happy(self): # 메서드 추가
        print("Feel so happy")
