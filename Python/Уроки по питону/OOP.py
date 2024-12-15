# Объектно ориентированное программирование
# Создание класса и объекта
# Поле == переменная

class robots:
    name = None
    power = None
    side = None
    typ = None
    speed = None

    def data(self,t = None,p = None,s = None):
        self.typ = t
        self.power = p
        self.side = s

    def get_data(self):
        print("Name: ",self.name,"\nPower: ",self.power,"\nSide: ",self.side)

    # Конструктор
    def __init__(self,name,speed = None):
        self.name = name
        self.speed = speed

        self.get_data()




robot_1 = robots("Joptimus",150)
robot_1.typ = 'car'
robot_1.power = 50
robot_1.side = "Light"


robot_2 = robots("Stremscram",800)
robot_2.typ = "fly"
robot_2.power = 40
robot_2.side = 'Dark'

robot_3 = robots("Bublicgum",250)
robot_3.data("car", 35, "Light")

print(robot_2.name)
print(robot_3.name)

robot_1.get_data()

# Конструкторы и переопределение методов

robot_2.get_data()
robot_3.get_data()
print()
print()
# Наследование это класс наследует всё от класса родителя

class Build:
    year = None
    city = None

    def __init__(self,year,city):
        self.year = year
        self.city = city

    def get_info(self):
        print("Year: ", self.year,"\nCity: ", self.city)

class Munizipal(Build): # Дочерний класс в параметре указан родительский класс
    people = None
    def __init__(self,people,year,city):
        self.people = people
        # self.year = year
        # self.city = city
        super(Munizipal,self).__init__(year,city) # Заменяет верхние 2 строчки
    def get_info(self):
        super().get_info()
        print("People: ",self.people)


class Private(Build):
    residents = None
    def __init__(self,residents,year,city):
        self.residents = residents
        self.year = year
        self.city = city
        super(Private, self).__init__(self.year,self.city)




school = Build(2000, "Kalach")
school.get_info()

shop = None
house = None






