import random
import webbrowser
from pathlib import Path

import folium

INTERSECTIONS = {
    "Intersection A - Delhi": (28.7041, 77.1025),
    "Intersection B - Noida": (28.5355, 77.3910),
    "Intersection C - Gurugram": (28.4595, 77.0266),
    "Intersection D - Faridabad": (28.4089, 77.3178),
}


def get_color(traffic_density: int) -> str:
    if traffic_density <= 5:
        return "green"
    if traffic_density <= 12:
        return "orange"
    return "red"


def simulate_traffic_map() -> Path:
    traffic_map = folium.Map(location=[28.6, 77.2], zoom_start=10)
    for name, coordinates in INTERSECTIONS.items():
        traffic_density = random.randint(0, 20)
        color = get_color(traffic_density)
        folium.CircleMarker(
            location=coordinates,
            radius=10,
            popup=f"{name}<br>Traffic: {traffic_density} vehicles",
            tooltip=name,
            color=color,
            fill=True,
            fill_color=color,
            fill_opacity=0.75,
        ).add_to(traffic_map)

    output_file = Path(__file__).resolve().parent / "smart_traffic_map.html"
    traffic_map.save(str(output_file))
    webbrowser.open(output_file.as_uri())
    print(f"Interactive map saved to: {output_file}")
    print("Note: traffic values are randomly simulated, not live traffic data.")
    return output_file


if __name__ == "__main__":
    simulate_traffic_map()
