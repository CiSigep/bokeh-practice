from bokeh.plotting import figure
from bokeh.io import output_file, show
import pandas

df = pandas.read_excel("verlegenhuken.xlsx")

temp = [val / 10 for val in df["Temperature"]]
pres = [val / 10 for val in df["Pressure"]]

output_file("weather.html")

f = figure(plot_width=500, plot_height=400)

f.title.text = "Temperature and Air Pressure"
f.xaxis.axis_label = "Temperature (°C)"
f.yaxis.axis_label = "Pressure (hPa)"

f.circle(temp, pres, size=0.5)

show(f)
