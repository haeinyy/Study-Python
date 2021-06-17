import random
from abc import *
import turtle

class Duck(metaclass=ABCMeta):

    DUCK_SIZE = 30

    def __init__(self):
        self._x = random.randint(-300,300)
        self._y = random.randint(-300,300)
        self._color = ''
        self._turtle = turtle

    @abstractmethod
    def display(self):
        pass

    def swim(self):
        self._turtle.color('black')
        self._turtle.penup()
        self._turtle.goto(self._x - 70, self._y + 50)
        self._turtle.pendown()
        self._turtle.write("어푸어푸")

class Quack(metaclass=ABCMeta):
    @abstractmethod
    def quack(self):
        pass

class Fly(metaclass=ABCMeta):
    @abstractmethod
    def fly(self):
        pass

class MallardDuck(Duck, Quack, Fly):
    def __init__(self):
        super(MallardDuck, self).__init__()
        self.__color = 'blue'

    def display(self):
        self._turtle.speed(50)
        self._turtle.penup()
        self._turtle.setpos(self._x, self._y)
        self._turtle.pendown()
        self._turtle.color(self.__color)
        self._turtle.begin_fill()
        self._turtle.circle(Duck.DUCK_SIZE)
        self._turtle.end_fill()
        self._turtle.penup()

    def quack(self):
        self._turtle.penup()
        self._turtle.color('black')
        self._turtle.goto(self._x + 30, self._y + 50)
        self._turtle.pendown()
        self._turtle.write("꽥꽥")

    def fly(self):
        self._turtle.color('black')
        self._turtle.penup()
        self._turtle.goto(self._x - 70, self._y - 10)
        self._turtle.pendown()
        self._turtle.write("파닥파닥")

class RedDuck(Duck, Quack, Fly):
    def __init__(self):
        super(RedDuck, self).__init__()
        self.__color = 'red'

    def display(self):
        self._turtle.speed(50)
        self._turtle.penup()
        self._turtle.setpos(self._x, self._y)
        self._turtle.pendown()
        self._turtle.color(self.__color)
        self._turtle.begin_fill()
        self._turtle.circle(Duck.DUCK_SIZE)
        self._turtle.end_fill()
        self._turtle.penup()

    def quack(self):
        self._turtle.penup()
        self._turtle.color('black')
        self._turtle.goto(self._x + 30, self._y + 50)
        self._turtle.pendown()
        self._turtle.write("꽥꽥")

    def fly(self):
        self._turtle.color('black')
        self._turtle.penup()
        self._turtle.goto(self._x - 70, self._y - 10)
        self._turtle.pendown()
        self._turtle.write("파닥파닥")


class RubberDuck(Duck, Quack):
    def __init__(self):
        super(RubberDuck, self).__init__()
        self.__color = 'orange'

    def display(self):
        self._turtle.speed(50)
        self._turtle.penup()
        self._turtle.setpos(self._x, self._y)
        self._turtle.pendown()
        self._turtle.color(self.__color)
        self._turtle.begin_fill()
        self._turtle.circle(Duck.DUCK_SIZE)
        self._turtle.end_fill()
        self._turtle.penup()

    def quack(self):
        self._turtle.penup()
        self._turtle.color('black')
        self._turtle.goto(self._x + 30, self._y + 50)
        self._turtle.pendown()
        self._turtle.write("삑삑")  # print text


class DecoyDuck(Duck):
    def __init__(self):
        super(DecoyDuck, self).__init__()
        self.__color = 'green'

    def display(self):
        self._turtle.speed(50)
        self._turtle.penup()
        self._turtle.setpos(self._x, self._y)
        self._turtle.pendown()
        self._turtle.color(self.__color)
        self._turtle.begin_fill()
        self._turtle.circle(Duck.DUCK_SIZE)
        self._turtle.end_fill()
        self._turtle.penup()

class DuckManager:
    __duck_list = []
    __instance = None

    def __init__(self):
        if not DuckManager.__instance:
            print('creation')
        else :
            print('already',  self.getInstance())

    @classmethod
    def getInstance(cls):
        if not cls.__instance:
            cls.__instance = DuckManager()
        return cls.__instance

    def makeDucks(self, num):
        duck_kind = [MallardDuck,RedDuck,RubberDuck,DecoyDuck]

        for i in range(num):
            DuckManager.__duck_list.append(duck_kind[random.randint(0,3)]())

    def displayAllDuck(self):
        if DuckManager.__duck_list != None:
            for duck in DuckManager.__duck_list:
                if duck != None:
                    duck.display()

    def quackAllDuck(self):
        if DuckManager.__duck_list != None:
            for duck in DuckManager.__duck_list:
                if duck != None:
                    if isinstance(duck, Quack):
                        duck.quack()

    def swimAllDuck(self):
        if DuckManager.__duck_list != None:
            for duck in DuckManager.__duck_list:
                if duck != None:
                    duck.swim()

    def flyAllDuck(self):
        if DuckManager.__duck_list != None:
            for duck in DuckManager.__duck_list:
                if duck != None:
                    if isinstance(duck, Fly):
                        duck.fly()

    def displayAllFuncDucks(self):
        if DuckManager.__duck_list != None:
            for duck in DuckManager.__duck_list:
                if duck != None: # 반드시 넣어야함!
                    duck.display()
                    duck.swim()
                if isinstance(duck, Quack):
                    duck.quack()
                if isinstance(duck, Fly):
                    duck.fly()

if __name__=="__main__":
    dm = DuckManager.getInstance()
    dm.makeDucks(15)
    dm.displayAllFuncDucks()
    # dm.displayAllDuck()
    # dm.flyAllDuck()
    # dm.swimAllDuck()
    # dm.quackAllDuck()