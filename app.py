from datetime import datetime
from random import randint
from threading import Lock

from flask import Flask, jsonify, render_template

app = Flask(__name__)
data_lock = Lock()

INTERSECTIONS = [
    {"id": "A", "name": "Delhi", "lat": 28.7041, "lng": 77.1025},
    {"id": "B", "name": "Noida", "lat": 28.5355, "lng": 77.3910},
    {"id": "C", "name": "Gurugram", "lat": 28.4595, "lng": 77.0266},
    {"id": "D", "name": "Faridabad", "lat": 28.4089, "lng": 77.3178},
]

traffic_state = {}


def traffic_level(count):
    if count <= 5:
        return "Low", "green"
    if count <= 12:
        return "Moderate", "orange"
    return "High", "red"


def refresh_traffic():
    """Generate a fresh simulated reading for each intersection."""
    with data_lock:
        now = datetime.now().astimezone().isoformat(timespec="seconds")
        for point in INTERSECTIONS:
            count = randint(0, 20)
            level, color = traffic_level(count)
            traffic_state[point["id"]] = {
                **point,
                "vehicles": count,
                "level": level,
                "color": color,
                "updated_at": now,
            }
        return list(traffic_state.values())


refresh_traffic()


@app.get("/")
def index():
    return render_template("index.html")


@app.get("/api/traffic")
def get_traffic():
    with data_lock:
        readings = list(traffic_state.values())
    return jsonify({"intersections": readings, "generated_at": datetime.now().astimezone().isoformat(timespec="seconds")})


@app.post("/api/refresh")
def refresh():
    readings = refresh_traffic()
    return jsonify({"intersections": readings, "generated_at": datetime.now().astimezone().isoformat(timespec="seconds")})


if __name__ == "__main__":
    # Open http://127.0.0.1:5000 in your browser after starting the app.
    app.run(debug=True, host="127.0.0.1", port=5000)
