import requests  # Импорт библиотеки для выполнения HTTP-запросов
import cv2  # Импорт библиотеки для обработки изображений и видео
import time  # Импорт библиотеки для работы с временем

# Базовый URL для API сервера дрона
base_url = 'http://127.0.0.1:5000/'


# Функция для отправки телеметрических данных на сервер
def send_telemetry(latitude, longitude, altitude):
    # Формирование JSON данных с координатами и высотой
    json_data = {
        'latitude': latitude,
        'longitude': longitude,
        'altitude': altitude
    }
    # Отправка POST запроса на сервер с телеметрическими данными
    response = requests.post(f"{base_url}telemetry", json=json_data)
    # Печать ответа сервера в формате JSON
    print(response.json())


# Функция для отправки видео кадра на сервер
def send_video(video_frame):
    # Кодирование кадра в формат JPEG
    _, buffer = cv2.imencode('.jpg', video_frame)
    # Отправка POST запроса на сервер с видео данными
    response = requests.post(f"{base_url}video", data=buffer.tobytes())
    # Проверка статуса ответа сервера
    if response.status_code == 204:
        print("Кадр успешно отправлен")  # Успешная отправка кадра
    else:
        print("Ошибка при отправке кадра")  # Ошибка при отправке кадра

def takeoff():
    response = requests.post(f"{base_url}drone/takeoff")
    print(f"Взлет: {response.json}")

def land():
    response = requests.post(f"{base_url}drone/land")
    print(f"Посадка: {response.json}")

def update_position(latitude, longitude, altitude):
    data = {
        'latitude': latitude,
        'longitude': longitude,
        'altitude': altitude
    }
    response = requests.put(f"{base_url}update_position")
    print(f"Обновление позиции: {response.json}")

# Главная функция
if __name__ == '__main__':
    takeoff()
    time.sleep(2)
    update_position(55.7558, 37.6176, 100)
    time.sleep(2)
    update_position(56.1366, 40.3966, 50)
    time.sleep(2)

    land()