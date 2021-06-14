# 1
class Person:
    d = '아빠'

    def __init__(self):
        self.data = self.d

    # class안의 변수를 사용하는 class method
    # *** cls -> class 변수 ***
    @classmethod
    def class_person(cls):
        return cls()

    # class와 상관없이 전역변수를 사용하는 static method
    @staticmethod
    def static_person():
        return Person()

class WhatPerson(Person):
    d = '엄마'

person1 = WhatPerson.class_person()
person2 = WhatPerson.static_person()


# 2
class Person2:
    count = 0
    def __init__(self):
        self.name = ''
        Person2.count += 1

    @classmethod
    def display(cls):
        print('count =', Person2.count)

james = Person2()
kai = Person2()
hey = Person2()

Person2.display()


# 3
class Hello:

    # class method는 반드시 인수에 'cls' 입력
    # cls : 클래스에 대한 정보 리턴
    @classmethod
    def calc(cls, x):
        return x + 10

    # static method : main보다 먼저 메모리에 할당됨
    # method려면 클래스 안에 선언 되어야함
    # static method는 인수로 전달 받는 것이 없다!
    @staticmethod
    def calc2(x):
        return x + 40

    def display(self, x):
        print('display : ', x)


h = Hello()
h.display(10)

print(h.calc(20))
print(Hello.calc(20)) # class method는 클래스명 자체로 호출하는 것이 원칙!

print(Hello.calc2(20))


# 4
class Hello:
    t = '내가 상속해 줬어!'

    @classmethod
    def calc(cls): # (자식 혹은 새롭게 선언되는 클래스) 해당하는 class의 정보를 인수로 받음 => 동적
        return cls.t # 자식 class 변수 리턴

    @staticmethod
    def calc2(): # 전역에 머물러 있기 때문에 해당 static method가 선언된 클래스의 변수만 접근 => 정적
        return Hello.t # 부모 class 변수 리턴

class HelloChild(Hello):
    t = '나는 상속받았어'

print(HelloChild.calc()) # class method
print(HelloChild.calc2()) # static method