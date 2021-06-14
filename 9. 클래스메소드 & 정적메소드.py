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