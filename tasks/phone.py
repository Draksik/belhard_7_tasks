"""
Создать класс Phone, у которого будут следующие атрибуты:

Определить атрибуты:

- brand - бренд
- model - модель
- issue_year - год выпуска

Определить методы:

- инициализатор __init__
- receive_call, который принимает имя звонящего и выводит на экран: Звонит {name}
- get_info, который будет возвращать кортеж (brand, model, issue_year)
- метод __str__, который выводит на экран информацию об устройстве:
Бренд: {}
Модель: {}
Год выпуска: {}
"""


class Phone:
    def __init__(self, brand: str, model: str, issue_year: int):
        self.brand = brand
        self.model = model
        self.issue_year = issue_year

    def receive_call(self, name: str):
        return f"Звонит {name}"

    def get_info(self):
        return self.brand, self.model, self.issue_year

    def __str__(self):
        return f"Бренд: {self.brand} \nМодель: {self.model} \nГод выпуска: {self.issue_year}"


device = Phone("Samsung", "S9plus", 2018)
device.__str__()
print(str(device))
device.get_info()
print(device.receive_call("FBI"))
