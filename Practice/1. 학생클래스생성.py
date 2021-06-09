class Student():
    def __init__(self, number, name, korean, english, math):
        self.number = number
        self.name = name
        self.korean = korean
        self.english = english
        self.math = math
        self.total = korean + english + math

    def display(self):
        print('학번 :',self.number,', 이름 :',self.name,', 국어 :',self.korean,', 영어 :',self.english,', 수학 :',self.math,', 총점 :',self.total)

student1 = Student(1,'홍길동',25,34,56)
student2 = Student(2,'김길동',55,78,34)
student3 = Student(3,'이길동',78,56,78)

student1.display()
student2.display()
student3.display()