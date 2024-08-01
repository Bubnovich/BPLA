from abc import ABC, abstractmethod
# Шаг 1.  Реализовать паттерн Итератор.
# Создать класс MyIterator, реализовать методы iter и next.


# Шаг 2. Реализовать паттерн Наблюдатель.
# Создать класс MyObserver с методом update.
# Создать класс MySubject, добавить метод register
# для подписки, метод notify для оповещения.

class MyObserver(ABC):
    @abstractmethod
    def update(self):
        pass

class MySubject():
    def __init__(self):
        self._observers = []
    def register(self, observer: MyObserver):
        self._observers.append(observer)

    def notify(self, message: str):
        for observer in self._observers:
            observer.update(message)

# Шаг 3.Реализовать паттерн Шаблонный метод.
# Создать абстрактный класс MyBase с шаблонным
# методом template_method. Создать классы MyClass1
# и MyClass2, переопределить методы из базового класса.
class MyBase(ABC):
    def template_method(self) -> None:
        self.get_date()
        self.change_date()
        self.set_date()

    def get_date(self ) -> None:
        print("Читаем данные из текстового файла")

    def change_date(self) ->None:
        print("Изменяем данные по сложному алгоритму")

    @abstractmethod
    def set_date(self) -> None:
        pass

class MyClass1(MyBase):
    def set_date(self) -> None:
        print("Записываем данные в реляционную базу данных")

class MyClass1(MyBase):
    def set_date(self) -> None:
        print("Записываем данные в графовую базу данных")



# Шаг 4. Протестировать Итератор, вызвав его в цикле for.
# Протестировать Наблюдатель - подписать наблюдателя, вызвать
# notify. Вызвать шаблонный метод в классах-наследниках.