import random
from abc import *

class Duck(metaclass=ABCMeta): # class 선언 부분에도 ABCMeta로 추상클래스 표시 해줘야함!

    DUCK_SIZE = 30

    def __init__(self):
        self._x = random.randint(-300,300) # protected 변수로 선언
        self._y = random.randint(-300,300) # protected 변수로 선언

    def move(self):
        self._x += 10
        self._y += 10
        print("뒤뚱뒤뚱")

    def sound(self):
        print("꽥꽥")

    @abstractmethod
    def display(self):
        pass


class MallardDuck(Duck):
    def __init__(self):
        super(MallardDuck, self).__init__()
        self.__myShape = "MallardDuck"

    def display(self):
        print('(', self._x, ",", self._y, ') :', self.__myShape)


class RedDuck(Duck):
    def __init__(self):
        super(RedDuck, self).__init__()
        self.__myShape = "RedDuck"

    def display(self):
        print('(', self._x, ",", self._y, ') :', self.__myShape)


# Manager 들은 대부분 Singleton 패턴
# 인스턴스를 외부에서 만들수 없고, 내부에서 만들어서 제공
# 만든 인스턴스를 외부에서 써야하므로, 클래스 변수로 선언
# 따라서, 외부가 인스턴스 생성자의 접근하지 못하게, getInstance() 인스턴스를 얻는 함수 따로 정의!
class DuckManager:

    __duck_list = [] # 클래스 변수 / 외부에서 접근 못하게 __ : private
    __instance = None # singleton 일 때, 인스턴스 변수 하나만 만들어서 공유!
                      # 외부에서 인스턴스 함부로 못 만듬!

    def __init__(self):
        # 인스턴스 만들어져 있나 없나 확인
        if not DuckManager.__instance: # 없다면 새로 인스턴스 생성
            print('creation')
        else : # 이미 있다면, 이미 존재하는 것 가져가라
            print('already',  self.getInstance())

    @classmethod
    def getInstance(cls):
        if not cls.__instance:
            cls.__instance = DuckManager()
            print("Dockmanager")
        return cls.__instance

    def makeDucks(self, num): # 랜덤 10마리
        randNum = []
        for i in range(num):
            randNum.append(random.randint(1,10))
        for j in randNum:
            if j%2 == 0:
                DuckManager.__duck_list.append(RedDuck())
                print('Red 생성')
            else:
                DuckManager.__duck_list.append(MallardDuck())
                print('Mallard 생성')

    def displayAllDucks(self):
        if DuckManager.__duck_list != None:

            for duck in DuckManager.__duck_list:
                if duck != None: # 반드시 넣어야함!
                    duck.display()

if __name__=="__main__":
    dm = DuckManager.getInstance() # getInstance로 인스턴스 얻어가야함
    dm2 = DuckManager.getInstance()