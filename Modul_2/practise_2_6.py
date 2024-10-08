#Install command - pip install opencv-python
# паттерн Наблюдатель
from abc import ABC, abstractmethod
import cv2

class Observer(ABC):
    @abstractmethod
    def update(self, message: str, image=None):
        pass

class Observable:
    def __init__(self):
        self._observers = []

    def add_observer(self, observer: Observer):
        self._observers.append(observer)

    def remove_observer(self, observer: Observer):
        self._observers.remove(observer)

    def notify_observers(self, message: str, image=None):
        for observer in self._observers:
            observer.update(message, image)

class DataLogger(Observer):
    def update(self, message: str, image=None):
        print(f"Система записи получила сообщение {message}")
        if image is not None:
            self.save_image(image)

    @staticmethod
    def save_image(image):
        filename = "camera.png"
        cv2.imwrite(filename, image)
        print(f"Снимок сделан!")

class AlertSystem(Observer):
    def update(self, message: str, image=None):
        print(f"Система предупреждений получила сообщение {message}")

class AnalysisSystem(Observer):
    def update(self, message: str, image=None):
        print(f"Система анализа получила сообщение {message}")

class Camera(Observable):
    def __init__(self):
        super().__init__()
        self._zoom_lvl = 1.0

    def set_zoom(self, zoom_lvl: float):
        self._zoom_lvl = zoom_lvl
        self.notify_observers(f"Изменен zoom на {self._zoom_lvl}")

    def take_image(self):
        try:
            caption = cv2.VideoCapture()
            ret, frame = caption.read()
            if ret:
                self.notify_observers("Захвачено изображение!", frame)
            caption.release()
        except:
            pass

if __name__ == "__main__":
    #Создаем наблюдателей
    data_logger = DataLogger()
    alert_system = AlertSystem()
    analysis_system = AnalysisSystem()
    #Создаем налюдаемого
    camera = Camera()

    camera.add_observer(data_logger)
    camera.add_observer(alert_system)
    camera.add_observer(analysis_system)

    camera.set_zoom(1.0)
    camera.take_image()