# #1
# class Student:
#     def __init__(self, name, age, mark,home_address):
#         self.name = name
#         self.age = age
#         self.mark = mark
#         self.home_address = home_address
#
#     def get_name(self):
#         return f"ФИО = {self.name}"
#
#     def get_age(self):
#         return f'возраст = {self.age}'
#
#     def get_mark(self):
#         return f'средний балл = {round(sum(self.mark) / len(self.mark), 1)}'
#
#     def get_home_address(self):
#         return f'домашний адрес = {self.home_address}'
#
# student_1 = Student('Иванов Иван Иванович',15,[5,5,5,4,3,4,2],'улица Пушкина дом 37' )
# print(student_1.get_name())
# print(student_1.get_age())
# print(student_1.get_mark())
# print(student_1.get_home_address())
#2
# class rectangle:
#     def __init__(self,length,width):
#         self.length = length
#         self.width = width
#
#     def get_lenght(self):
#         return f'Плошадь = {self.length * self.width}'
#
#     def get_perimeter(self):
#         return f'Перемитр = {self.width + 2 * self.length}'
#
# Rectangle = rectangle(23,23)
# print(Rectangle.get_lenght())
# print(Rectangle.get_perimeter())

#3

# class Car:
#     def __init__(self,stamp,model,year_release,mileage):
#         self.stamp = stamp
#         self.model = model
#         self.year_release = year_release
#         self.mileage = mileage
#
#     def get_stamp(self):
#         return f'Марка = {self.stamp}'
#
#     def get_model(self):
#         return f'Модель = {self.model}'
#
#     def get_year_release(self):
#         return f'Год выпуска = {self.year_release}'
#
#     def get_mileage(self):
#         return f'Пробег = {self.mileage}'
#
# sport_car = Car('Porsche','911',1965,5000)
# print(sport_car.get_stamp())
# print(sport_car.get_model())
# print(sport_car.get_year_release())
# print(sport_car.get_mileage())

#4
class Bank_account:
    def __init__(self,name,age,number_score,balance):
        self.name = name
        self.age = age
        self.number_score = number_score
        self.__balance = balance
        self.__action = []

    def get_name(self):
        return f"ФИО = {self.name}"

    def get_age(self):
        return f'возраст = {self.age}'

    def get_number_score(self):
        return f'Номер счёта = {self.number_score}'

    def get_balance(self):
        return self.__balance

    def replenishment(self, money):
        self.__balance += money
        self.__action.append(f'Внесение наличных на счет: {money}')

    def withdrawal_money(self , money):
        if money <= self.__balance:
            self.__balance -= money
            self.__action.append(f'Снятие наличных: {money}')
        else:
            return 'Средств нет'

    def info_money(self):
        return self.__action


Bank = Bank_account('Иванов Иван Иванович',35,'GYYDGYVUVU8',30000)
print(Bank.get_name())
print(Bank.get_age())
print(Bank.get_number_score())
print(f'Баланс: {Bank.get_balance()} руб')

Bank.replenishment(400)
Bank.withdrawal_money(3000)


list_trans = Bank.info_money()

print()
print('История счёта:')
for i in range(0, len(list_trans)):
    print(list_trans[i])
print(f'Итоговый баланс {Bank.get_balance()}')

#5
# class Triangle:
#     def __init__(self, side_a, side_b, side_c):
#         self.side_a = side_a
#         self.side_b = side_b
#         self.side_c = side_c

#     def triangle_type(self):
#         if self.side_a == self.side_b == self.side_c:
#             return "Равносторонний"
#         elif self.side_a == self.side_b or self.side_b == self.side_c or self.side_a == self.side_c:
#             return "Равнобедренный"
#         else:
#             return "Разносторонний"
#
#     def calculate_area(self):
#         s = (self.side_a + self.side_b + self.side_c) / 2
#         return (s * (s - self.side_a) * (s - self.side_b) * (s - self.side_c))**0.5
#
# triangle = Triangle(5,5,5)
# print(triangle.triangle_type())
# print(triangle.calculate_area())


