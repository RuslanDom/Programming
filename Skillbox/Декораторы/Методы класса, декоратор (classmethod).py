class Pet:
    TOTAL_SOUNDS = 0

    def __init__(self) -> None:
        self.__legs = 4
        self.__has_tail = True

    def __str__(self) -> str:
        tail_status = 'да' if self.__has_tail else 'нет'
        return 'Всего ног: {legs}\nХвост присутствует - {tail}'.format(
            legs=self.__legs,
            tail=tail_status
        )


class Cat(Pet):
    @classmethod
    def sound(cls) -> None:
        cls.TOTAL_SOUNDS += 1
        print('Мяу!')


class Dog(Pet):
    @classmethod
    def sound(cls) -> None:
        print('Гав!')


cat = Cat()
cat.sound()
print(cat.TOTAL_SOUNDS)

cat.sound()
print(cat.TOTAL_SOUNDS)