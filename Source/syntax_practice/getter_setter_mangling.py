# Python은 클래스의 속성과 메서드가 public으로 설정됨


class square():
    def __init__(self, width, height):
        self.width = width
        self.height = height
    @property #getter 메서드 설정
    def area(self):
        return self.width * self.height
    @area.setter #setter 메서드 설정
    def area(self, width, height):
        self.width = width
        self.height = height
