#opencv-python
from flask import Flask, request, jsonify, Response
import cv2
import numpy as np

app = Flask(__name__)

drone_state = {
    "status": "landed",
    "position": {
        "latitude": 0.0,
        "longitude": 0.0,
        "altitude": 0.0,
    },
    "telemetry_data": []
}

video_frame = None

@app.route("/drone/takeoff", methods=["POST"])
def takeoff():
    try:
        if drone_state["status"] == "flying":
            return jsonify({"error": "Дрон уже в воздухе"}), 400

        drone_state["status"] = "flying"
        drone_state["position"]["altitude"] = 10.0

        app.logger.info("Дрон взлетел")
        return jsonify({
            "message": "Взлет выполнен",
            "drone_state": drone_state
        }), 200
    except Exception as e:
        app.logger.error(f"Ошибка при взлете: {e}")
        return jsonify({"error": "Ошибка при взлете"}), 500

@app.route("/telemetry", methods=["POST"])
def receive_telemetry():
    data = request.json()
    drone_state["telemetry_data"].append(data)
    return jsonify({"status": "Получили"}), 200

@app.route("/display", method=["GET"])
def display_telemetry():
    return jsonify(drone_state["telemetry_data"]), 200

@app.route("/video", method=["POST"])
def receive_video():
    global video_frame
    np_array = np.frombuffer(request.data, dtype=np.uint8)
    video_frame = cv2.imdecode(np_array, cv2.IMREAD_COLOR)
    return "", 204

@app.route("/video_feed")
def video_feed():
    def generate():
        global video_frame
        while True:
            if video_frame is None:
                _, buffer = cv2.imencode('.jpg', video_frame)
                frame = buffer.tobytes()
                yield (b'--frame\r\n'
                       b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

    return Response(generate(), mimetype='multiprt/x-mixed-replace; boundary=frame')


if __name__ == "__main__":
    app.run(debug=True)
