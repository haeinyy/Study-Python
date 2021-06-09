class Player:
    # class 변수들을 초기화 하기 위한 생성자
    def __init__(self):
        self.x = 100 # 처음 값 지정
        self.y = 200 # 처음 heap의 주소값 지정

    def display(self):
        print(self.x, self.y)

    def moveLeft(self):
        self.x += 1
        print(self.x, self.y)

    def moveRight(self):
        self.x -= 1
        print(self.x, self.y)

class Enemy:
    def __init__(self):
        self.x = 0
        self.y = 0

    def display(self):
        print(self.x, self.y)

    def moveLeft(self):
        self.x += 1
        print(self.x, self.y)


    def moveRight(self):
        self.x -= 1
        print(self.x, self.y)

    def moveUp(self):
        self.y -= 1
        print(self.x, self.y)

    def moveDown(self):
        self.y += 1
        print(self.x, self.y)

pobj = Player() # 여기서 this는 pobj의 주소값
pobj2 = Player() # 여기서 this는 pobj2의 주소값

eobj = Enemy()
eobj2 = Enemy()

pobj.display()
pobj2.display()

pobj.moveLeft()
pobj.moveRight()

eobj.display()
eobj2.display()

eobj.moveUp()
eobj.moveUp()