# 0610 Assignment1 solution
# Duck 클래스 설계

# super class -> sub class (Top - Down 방식)
# 다중상속! -> 부모가 여러개

import random
import turtle

class Duck:

    color_list = ['yellow', 'orange', 'green', 'skyblue', 'purple']

    def __init__(self):
        self.x = random.randint(-400,400)
        self.y = random.randint(-400,400)
        self.size = 10
        self.__turtle = None # 아직 실체는 없지만 변수로 공간 확보
        self.__color = random.randint(0,5)
        self.__r = random.random()
        self.__g = random.random()
        self.__b = random.random()

        
    def display(self, turtle):
        self.__turtle = turtle
        self.__turtle.bgcolor("black")
        self.__turtle.penup()
        self.__turtle.setpos(self.x, self.y)
        self.__turtle.pendown()

        self.__turtle.color((self.__r, self.__g, self.__b))
        self.__turtle.begin_fill()
        self.__turtle.circle(self.size)
        self.__turtle.end_fill()

        self.__turtle.penup()
        self.__turtle.goto(self.x + 20, self.y + 20)
        self.__turtle.pendown()
        self.__turtle.write("quack~quack~")  # print text

        # print('(',self.x,',',self.y,') / size =',self.size)

    def screen_reset(self):
        self.__turtle.reset()

# duck 100마리 생성
duck_list = []
for i in range(10):
    duck_list.append(Duck())
    
for duck in duck_list:
    if duck != None:
        duck.display(turtle)