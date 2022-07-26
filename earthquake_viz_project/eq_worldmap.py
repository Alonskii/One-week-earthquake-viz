import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# Get a JSON file.
filename = 'earthquake_data/seven_days_earthquake.json'
with open(filename, encoding='utf-8') as f:
    eq_data = json.load(f)

# Create a readable file from the loaded json file above.

readable_file = 'earthquake_data/readable_eq_data.json'
with open(readable_file, 'w') as f:
    json.dump(eq_data, f, indent=4)

# Exploring the structure of the data.
title = eq_data["metadata"]["title"]
all_eq_dicts = eq_data["features"]

mags, lons, = [], []
lats, hover_texts = [], []

for eq_dict in all_eq_dicts:
    mag = eq_dict["properties"]["mag"]
    if mag > 0:
        mags.append(eq_dict["properties"]["mag"])
        lons.append(eq_dict["geometry"]["coordinates"][0])
        lats.append(eq_dict["geometry"]["coordinates"][1])
        hover_texts.append(eq_dict["properties"]["title"])

# Map the earthquakes.
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_texts,

    # Outline marks in the map
    'marker': {
        'size': [5*mag for mag in mags],
        'color': mags,
        'colorscale': 'Ylorrd',
        'reversescale': True,
        'colorbar': {'title': 'Magnitude'},
    },
}]

# One-week Earthquake data output.
my_layout = Layout(title = f'{title}')
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='sevenday_quakes.html')
