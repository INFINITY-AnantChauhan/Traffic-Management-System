# 🚦 Smart Traffic Management System

An interactive Python + Flask + Leaflet dashboard that simulates traffic density at four intersections across Delhi NCR.

## Features

- Dynamic dashboard with traffic summary cards and intersection status panels.
- Interactive Leaflet map with color-coded markers and popups.
- Automatic data refresh every 10 seconds.
- Manual **Refresh data** button that requests new simulated readings from the Python backend.
- Traffic-level filter and dynamic vehicle-density chart.
- Flask API endpoints connect the HTML dashboard to Python.
- Optional original Folium map generator remains available.

> **Important:** This is a simulation. Vehicle counts are randomly generated and are not live traffic data. No cameras, sensors, live traffic APIs, or traffic-signal controls are connected.

## Project structure

```text
Smart-Traffic-Management/
├── app.py                    # Flask server and traffic API
├── smart_traffic.py          # Standalone Folium map generator
├── index.html                # Main dashboard source copy
├── templates/
│   └── index.html            # HTML template served by Flask
├── static/
│   └── .gitkeep
├── requirements.txt
├── README.md
└── .gitignore
```

The Flask application renders `templates/index.html`. The root `index.html` is included as a convenient standalone source copy. To run the connected dashboard, use Flask as described below rather than opening the HTML file directly.

## Requirements

- Python 3.8 or newer
- Internet connection for Leaflet/OpenStreetMap map assets

## Run the connected dashboard

1. Extract the project ZIP and open the folder in VS Code.
2. Open a terminal in the project folder.
3. Install dependencies:

   ```bash
   python -m pip install -r requirements.txt
   ```

4. Start the backend:

   ```bash
   python app.py
   ```

5. Open this address in your browser:

   **http://127.0.0.1:5000**

Keep the terminal running while using the dashboard. Do not open `templates/index.html` directly: the page uses Flask API routes.

### Dashboard controls

- **Refresh data:** asks the backend to generate new simulated traffic readings.
- **Traffic level filter:** shows only low, moderate, or high traffic markers.
- **Auto-refresh:** the dashboard fetches the latest readings every 10 seconds.

## API endpoints

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/` | Serves the dashboard |
| `GET` | `/api/traffic` | Returns current intersection readings as JSON |
| `POST` | `/api/refresh` | Generates fresh simulated readings and returns JSON |

Example response shape:

```json
{
  "intersections": [
    {
      "id": "A",
      "name": "Delhi",
      "lat": 28.7041,
      "lng": 77.1025,
      "vehicles": 11,
      "level": "Moderate",
      "color": "orange",
      "updated_at": "2026-10-14T19:30:00+05:30"
    }
  ],
  "generated_at": "2026-10-14T19:30:00+05:30"
}
```

Values shown above are an example only.

## Run the standalone Folium version

To generate a separate HTML map using the original Python approach:

```bash
python smart_traffic.py
```

This creates `smart_traffic_map.html` and attempts to open it in your browser.

## Customize intersections

Update the `INTERSECTIONS` list in `app.py` and the `INTERSECTIONS` dictionary in `smart_traffic.py` if you want to change the displayed locations. In `app.py`, each location uses a latitude and longitude.

## Traffic classification

- **Low:** 0–5 simulated vehicles
- **Moderate:** 6–12 simulated vehicles
- **High:** 13–20 simulated vehicles

## Limitations and future work

Current readings are random demonstration data. Possible future work includes connecting a legitimate live traffic API, estimating vehicles from camera footage, persisting historical readings in a database, and evaluating traffic prediction models. These features are not implemented in this version.

## License

Educational demonstration project. Add an open-source license file if you intend to publish it under specific reuse terms.
