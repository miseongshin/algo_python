class Person:
    def __init__(self, param_name):  # 생성자
        print("I am created!", self)
        self.name = param_name

    def talk(self):
        print("안뇽하세요 제 이름은", self.name, "입니다.")

person_1 = Person("홍길동")
print(person_1.name)
print(person_1.talk())
person_2 = Person("봐봐봐")
print(person_2.name)
print(person_2.talk())
