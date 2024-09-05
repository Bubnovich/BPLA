#Бубнович Антон Владимирович
#No БПЛА_256-1
from flask import Flask, request, jsonify

app = Flask(__name__)

# Модель данных
class UAVModel
    def __init__(self)
        self.height = 0  # Высота полета
        self.velocity = 0  # Скорость движения
        self.coordinates = (0, 0)  # Текущие координаты
        self.battery = 100  # Заряд батареи в процентах

    def update_coordinates(self, new_coordinates)
        self.coordinates = new_coordinates

    def update_height(self, new_height)
        self.height = new_height

    def update_velocity(self, new_velocity)
        self.velocity = new_velocity

    def consume_battery(self, consumption)
        self.battery -= consumption

# Представление
class UAVView
    def show_status(self, model)
        return {
            height model.height,
            velocity model.velocity,
            coordinates model.coordinates,
            battery model.battery
        }

    def warning(self, message)
        return {warning message}

# Контроллер
class UAVController
    def __init__(self, model, view)
        self.model = model
        self.view = view

    def adjust_position(self, new_coordinates)
        self.model.update_coordinates(new_coordinates)
        return self.view.show_status(self.model)

    def adjust_height(self, new_height)
        self.model.update_height(new_height)
        return self.view.show_status(self.model)

    def adjust_velocity(self, new_velocity)
        self.model.update_velocity(new_velocity)
        return self.view.show_status(self.model)

    def check_battery(self)
        if self.model.battery  20
            return self.view.warning(Battery low! Initiating return to base.)
        return {battery_level self.model.battery}

    def return_to_base(self)
        self.model.update_coordinates((0, 0))
        self.model.update_height(0)
        self.model.update_velocity(0)
        return self.view.warning(UAV has returned to base.)

# Создание экземпляров модели и контроллера
uav_model = UAVModel()
uav_view = UAVView()
uav_controller = UAVController(uav_model, uav_view)

# API для управления дроном
@app.route('status', methods=['GET'])
def get_status()
    return jsonify(uav_view.show_status(uav_model))

@app.route('position', methods=['POST'])
def update_position()
    data = request.get_json()
    new_coordinates = data.get('coordinates', (0, 0))
    return jsonify(uav_controller.adjust_position(new_coordinates))

@app.route('height', methods=['POST'])
def update_height()
    data = request.get_json()
    new_height = data.get('height', 0)
    return jsonify(uav_controller.adjust_height(new_height))

@app.route('velocity', methods=['POST'])
def update_velocity()
    data = request.get_json()
    new_velocity = data.get('velocity', 0)
    return jsonify(uav_controller.adjust_velocity(new_velocity))

@app.route('battery', methods=['GET'])
def check_battery()
    return jsonify(uav_controller.check_battery())

@app.route('return_to_base', methods=['POST'])
def return_to_base()
    return jsonify(uav_controller.return_to_base())

if __name__ == '__main__'
    app.run(debug=True)
