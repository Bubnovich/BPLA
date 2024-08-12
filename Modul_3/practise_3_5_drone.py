import requests
BASE_URL = 'http://127.0.0.1:5000/drones'

def register_drone(drone_id, drone_info):
    url = BASE_URL
    payload = {
        'drone_id': drone_id
        **drone_info
    }
    response = requests.post(url, json=payload)
    return response.json



if __name__ == "__main__":
    drone_id = 1007
    drone_info = {
        "model": "DJI Phantom",
        "battery": 100
    }
    response = register_drone(drone_id, drone_info)
    print(f"Регистрация дрона {response}")