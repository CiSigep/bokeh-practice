from bokeh.plotting import figure
from bokeh.io import output_file, show

x = [3, 7.5, 10]
y = [3, 6, 9]

output_file("circle.html")


f1 = figure()

f1.circle(x, y)


show(f1)

f2 = figure()
output_file("triangle.html")
f2.triangle(x, y)
show(f2)
