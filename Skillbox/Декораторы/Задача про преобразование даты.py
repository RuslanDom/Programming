class Date:
    def __init__(self, day: int = 0, month: int = 0, year: int = 0) -> None:
        self.day = day
        self.month = month
        self.year = year

    def __str__(self) -> str:
        return 'День: {day} Месяц: {month} Год: {year}'.format(
            day=self.day,
            month=self.month,
            year=self.year
        )

    @classmethod
    def valid_is_date(cls, date: str) -> bool:
        day, month, year = map(int, date.split('-', 3))
        return 0 < day <= 31 and 0 < month <= 12 and 0 < year <= 3000

    @classmethod
    def from_in_string(cls, date: str) -> 'Date':
        # При помощи map() разбили строку на список list() и присвоили переменным преобразованные в integer значения
        day, month, year = map(int, date.split('-', 3))

        # Создал экземпляр класса прямо в @classmethod передал ему атрибуты и вернул return экземпляр класса
        date_object = cls(day, month, year)
        return date_object


my_date = Date.from_in_string('18-01-1990')
print(my_date)
print(Date.valid_is_date('22-02-2010'))
print(Date.valid_is_date('32-02-2010'))
