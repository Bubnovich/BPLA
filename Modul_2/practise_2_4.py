# Паттерн Декоратор
from abc import ABC, abstractmethod
class Notifier(ABC):
    @abstractmethod
    def send(self, message: str):
        pass

class SMSNotifier(Notifier):
    def __init__(self, phone: str):
        self.phone = phone

    def send(self, message: str):
        print(f"Отправлено sms на номер: {self.phone}, сообщение: {message}")

class NotifierDecorator(Notifier):
    def __init__(self, wrapper: Notifier):
        self._wrapper = wrapper

    def send(self, message: str):
        self._wrapper.send(message)

class WhatsappNotifierDecorator(NotifierDecorator):
    def __init__(self, wrapper: Notifier, whatsapp_id: str):
        super().__init__(wrapper)
        self.whatsapp_id = whatsapp_id

    def send(self, message: str):
        super().send(message)
        print(f"Отправлено сообщение на whatsapp: {self.whatsapp_id}, сообщение: {message}")

class TelegramNotifierDecorator(NotifierDecorator):
    def __init__(self, wrapper: Notifier, telegram_id: str):
        super().__init__(wrapper)
        self.telegram_id = telegram_id

    def send(self, message: str):
        super().send(message)
        print(f"Отправлено сообщение на telegram: {self.telegram_id}, сообщение: {message}")

class RocketNotifierDecorator(NotifierDecorator):
    def __init__(self, wrapper: Notifier, number_rocket: int):
        super().__init__(wrapper)
        self.number_rocket = number_rocket

    def send(self, message: str):
        super().send(message)
        print(f"Запустить ракету №: {self.number_rocket}")

if __name__ == "__main__":
    notifier = SMSNotifier(phone="+754654654645")
    notifier = WhatsappNotifierDecorator(notifier,whatsapp_id="+754654654654")
    notifier = TelegramNotifierDecorator(notifier, telegram_id="@Egor")
    notifier = RocketNotifierDecorator(notifier, number_rocket=1)
    notifier.send(message="Найдена потеряшка")
