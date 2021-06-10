# 클래스가 선언 순서
# 1. class 먼저 선언 -> 2. heap에 메모리 공간 먼저 할당 -> 3. 변수 초기화 -> 4. getter/setter 선언

import random2

# 1. class 먼저 선언 - 메모리에 올림
class StudentInfo:

    # 파이썬에서 'new'가 없기떄문에 명시! 모르고 있어도 됨...!!
    # 2. (원래 디폴트로 지정되어 있으므로 따로 명시하지 않음)
    # class 자체를 초기화
    def __new__(cls):
        # print('new')
        obj = super().__new__(cls)
        return obj

    # 3. 변수 초기화
    # __ : 외부에서 접근할수 없게 'private' 하는 기능
    def __init__(self):
        self.__number = random2.randint(1, 10)
        self.__kor = random2.randint(1, 100)
        self.__math = random2.randint(1, 100)
        self.__eng = random2.randint(1, 100)
        self.__total = self.__kor + self.__math + self.__eng

    # 4. getter/setter 선언
    # getter/setter : 클래스의 정보은닉을 위해 사용
    # 그냥 실행하면 아래있는 setter가 getter 덮어씀....
    # 따라서, @ 로 decorator 표시 해주어야함
    @property
    def kor(self):  # kor의 getter -> read
        return self.__kor

    @kor.setter
    def kor(self, score):  # kor의 setter -> write
        if score >= 0:
            self.__kor = score

    @property
    def math(self):  # getter
        return self.__math

    @math.setter
    def math(self, score):  # setter
        if score >= 0:
            self.__math = score

    @property
    def eng(self):  # getter
        return self.__eng

    @eng.setter
    def eng(self, score):  # setter
        if score >= 0:
            self.__eng = score

    def display(self):
        print('학번 :', self.__number, ', 국어 :', self.__kor,', 수학 :',self.__math, ', 영어 :',self.__eng,
              '\n총점 :', self.__kor, '+', self.__math, '+', self.__eng, '=', self.__total,'\n')

# 2. heap에 메모리 공간 먼저 할당
# => 해당 haep 메모리 공간을 stack에 저장되어있는 s1이 가리키고 있음
# 원래는 s1 = new StudentInfo()
# new : heaep 영역 생성
s1 = StudentInfo()
s2 = StudentInfo()
s3 = StudentInfo()

# 인스턴스의 getter/setter 설정 시, 변수 입력 방식과 비슷!
# 학생1
print('[학생1]')
s1.kor = 5
s1.math = 20
s1.display()

# 학생2
print('[학생2]')
s2.eng = 45
s2.display()

# 학생3
print('[학생3]')
s3.kor = 30
s3.math = 67
s3.eng = 100
s3.display()