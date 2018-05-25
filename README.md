# arduino-data-collection

This repository holds a bunch of Arduino sketches as well as Python code for taking sensor information and writing it to files.
Other features are planned.

# Getting Started:
1. Start by figuring out what port your Arduino is communicating on
    1. The port can be found by accessing the Arduino IDE and looking in the bottom right corner.
2. In the `dev_info.py` file, change `DEVICE_PORT` to the port from above.
3. Feel free to edit the Arduino sketches in `/sketches/` to suit your project.

# Features:
1. Collecting data from Arduino
    1. Data can be read, collected, and stored in CSV files using the `collecting` module.
2. Visualizing data
    1. The `visualizing` module contains the scripts needed to visualize data.
    2. Using the `Plotly` module, CSV files can be turned into graphs and charts.