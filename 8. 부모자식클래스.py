import random
import turtle
from abc import *

# Duck : super class (부모클래스)
class Duck:
    DUCK_SIZE = 30  # class 변수

    def __init__(self):
        self._x = random.randint(-300, 300)  # instance 변수 # protected 접급제어자 -> 자식만 접근가능
        self._y = random.randint(-300, 300)
        self._turtle = turtle

    # 형태만 있는 추상메서드 정의
    # 자식클래스는 반드시 부모클래스의 추상메서드를 재정의 해야함!
    @abstractmethod
    def display(self):
        pass

    def move(self):
        self._turtle.color('black')
        self._turtle.penup()
        self._turtle.goto(self._x - 70, self._y + 50)
        self._turtle.pendown()
        self._turtle.write("뒤뚱뒤뚱")  # print text

    def sound(self):
        self._turtle.penup()
        self._turtle.color('black')
        self._turtle.goto(self._x + 30, self._y + 50)
        self._turtle.pendown()
        self._turtle.write("꽥꽥")  # print text


# MallardDuck : sub class (자식클래스)
# Duck의 상속 받는 MallardDuck
# 자식클래스는 부모클래스를 컨트롤,참조 할 수 없다!
class MallardDuck(Duck):
    Kind = 'MallardDuck'
    Color = 'Blue'

    # 자식 바로 윗 부모의 정보는 참조 할 수 있다!
    # 자식의 생성자가 불리면, 무조건 부모 생성자 먼저 호출!
    # 부모클래스에서 변수를 self.x / self.y로 선언 했기 때문에 자식 클래스가 해당 변수 참조 가능!
    # 하지만, 부모클래스에서 self.__x / self.__y 처럼 private 으로 변수 선언 했으면, 자식이 해당 변수 참조 불가능!
    def __init__(self):
        super(MallardDuck, self).__init__()

    # Method's override
    # 부모클래스와 같은 함수이지만, 재정의! => 오버라이딩
    def display(self):
        self._turtle.speed(50)
        self._turtle.penup()
        self._turtle.setpos(self._x, self._y)
        self._turtle.pendown()
        self._turtle.color(MallardDuck.Color)
        self._turtle.begin_fill()
        self._turtle.circle(Duck.DUCK_SIZE)
        self._turtle.end_fill()

class RedDuck(Duck):
    Kind = 'RedDuck'
    Color = 'Red'

    def __init__(self):
        super(RedDuck, self).__init__()

    def display(self):
        self._turtle.speed(50)
        self._turtle.penup()
        self._turtle.setpos(self._x, self._y)
        self._turtle.pendown()
        self._turtle.color(RedDuck.Color)
        self._turtle.begin_fill()
        self._turtle.circle(Duck.DUCK_SIZE)
        self._turtle.end_fill()

class DuckManager:
    def __init__(self):
        self.__ducklist = []

    def appendduck(self):
        for i in range(5):
            self.__ducklist.append(MallardDuck())
            self.__ducklist.append(RedDuck())

    def displayAllDucks(self):
        for duck in self.__ducklist:
            duck.display()
            duck.move()
            duck.sound()

class reset(Duck):
    def display(self):
        self._turtle = turtle

    def screen_reset(self):
        self._turtle.reset()

# 화면 reset
d = reset()
d.display()
d.screen_reset()

M = DuckManager()
M.appendduck()
M.displayAllDucks()