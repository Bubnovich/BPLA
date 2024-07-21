class MySingleton:
    __instance = None

    def __init__(self):
        if not MySingleton.__instance:
            print(" __init__ method called..")
        else:
            print("Instance already created:", self.get_instance())
    @classmethod
    def get_instance(cls):
        if not cls.__instance:
            cls.__instance = MySingleton()
        return cls.__instance

if __name__ == "__main__":
    s1 = MySingleton()
    s1.get_instance()
    s2 = MySingleton()
    s2.get_instance()

    print(f"{s1} is {s2}")

#Шаг 4. Создать класс MyClass с методом test. Создать класс MyClassAdapter,
# в нем вызвать метод test из экземпляра MyClass.
class MyClass:
    def test(self):
        print("функция из класса Myclass")

class MyClassAdapter(MyClass):
    def call_parent_def(self):
        MyClass().test()

if __name__ == "__main__":
    MyClassAdapter().call_parent_def()

#Шаг 5. Создать функцию my_function. Написать декоратор my_decorator,
# который будет выводить имя функции перед ее вызовом.

def my_decorator(func):
    print(func.__name__)

#Шаг 6. Применить декоратор к функции my_function и убедиться,
# что при вызове функции выводится ее имя.
@my_decorator
def my_function():
    pass