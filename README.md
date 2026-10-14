# 🚦 Smart Traffic Management System

A beginner-friendly Python project that simulates traffic density at four intersections in Delhi NCR and visualizes the results on an interactive map using **Folium**.

> **Important:** This project uses randomly generated traffic values. It does not collect live vehicle counts, predict traffic, or control traffic signals.

## Features

- Interactive map with four locations: Delhi, Noida, Gurugram, and Faridabad.
- Randomly simulated density of 0–20 vehicles at each intersection.
- Color-coded markers:
  - 🟢 Green: low traffic (0–5 vehicles)
  - 🟠 Orange: moderate traffic (6–12 vehicles)
  - 🔴 Red: high traffic (13–20 vehicles)
- Marker popups and a map legend.
- Saves the map as an HTML file and attempts to open it in your default browser.

## Project structure

```text
Smart-Traffic-Management/
├── smart_traffic.py
├── requirements.txt
├── README.md
├── .gitignore
└── smart_traffic_map.html   # Generated after running the script
```

## Requirements

- Python 3.8 or newer
- Internet access to load OpenStreetMap tiles in the browser

## Setup

### 1. Open a terminal in this folder

### 2. (Optional) Create and activate a virtual environment

**Windows**
```bash
python -m venv .venv
.venv\Scripts\activate
```

**macOS / Linux**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

## Run the project

```bash
python smart_traffic.py
```

The script creates `smart_traffic_map.html` in the project folder and tries to open it in your default browser. If it does not open automatically, double-click the HTML file or open it in a browser.

Every run generates new random traffic values.

## Customize locations

Edit the `INTERSECTIONS` dictionary in `smart_traffic.py`:

```python
INTERSECTIONS = {
    "Intersection A": (28.7041, 77.1025),
    "Intersection B": (28.5355, 77.3910),
}
```

Each location is a `(latitude, longitude)` pair.

## How it works

1. Folium creates a map centered on Delhi NCR.
2. Python's `random.randint(0, 20)` simulates a vehicle count for each intersection.
3. `get_color()` maps each count to a traffic color.
4. Folium adds a circle marker and popup for each location.
5. The map is saved as an HTML file.

## Limitations

- Traffic counts are random simulations, not real observations.
- Values change each time the program runs.
- The project does not use machine learning, live traffic APIs, cameras, or sensors.
- The map background tiles generally require an internet connection.

## Possible future improvements

- Integrate a live traffic data API.
- Estimate vehicle counts from camera images using computer vision.
- Store historical counts in a database.
- Add congestion charts and an interactive dashboard.
- Explore adaptive signal timing after obtaining reliable traffic data.

## License

Provided for educational and learning purposes. Add a license file if you plan to distribute the project under specific reuse terms.
