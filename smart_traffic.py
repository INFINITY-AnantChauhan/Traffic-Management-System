import random
import webbrowser
from pathlib import Path

import folium

# Coordinates of four intersections in the Delhi NCR region.
# Replace these coordinates to simulate traffic in another city.
INTERSECTIONS = {
    "Intersection A - Delhi": (28.7041, 77.1025),
    "Intersection B - Noida": (28.5355, 77.3910),
    "Intersection C - Gurugram": (28.4595, 77.0266),
    "Intersection D - Faridabad": (28.4089, 77.3178),
}


def get_color(traffic_density: int) -> str:
    """Return a marker color based on the simulated number of vehicles."""
    if traffic_density <= 5:
        return "green"
    if traffic_density <= 12:
        return "orange"
    return "red"


def simulate_traffic_map() -> Path:
    """Generate and save an interactive traffic map, then open it in a browser."""
    traffic_map = folium.Map(location=[28.6, 77.2], zoom_start=10)

    for name, coordinates in INTERSECTIONS.items():
        # Simulated traffic density; this is not live traffic data.
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

    # Add a simple legend.
    legend_html = """
    <div style="
        position: fixed; bottom: 30px; left: 30px; z-index: 9999;
        background: white; padding: 10px 12px; border: 1px solid #888;
        border-radius: 5px; font-size: 13px;">
        <b>Traffic Density (simulated)</b><br>
        <span style="color:green;">●</span> Low: 0–5 vehicles<br>
        <span style="color:orange;">●</span> Moderate: 6–12 vehicles<br>
        <span style="color:red;">●</span> High: 13–20 vehicles
    </div>
    """
    traffic_map.get_root().html.add_child(folium.Element(legend_html))

    output_file = Path(__file__).resolve().parent / "smart_traffic_map.html"
    traffic_map.save(str(output_file))
    webbrowser.open(output_file.as_uri())

    print(f"Interactive map saved to: {output_file}")
    print("Note: traffic values are randomly simulated, not live traffic data.")
    return output_file


if __name__ == "__main__":
    simulate_traffic_map()
