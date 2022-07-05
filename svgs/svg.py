import svgwrite as svg
import math

def line(start, stop):
    dx = (stop[0] - start[0]) / 3
    dy = (stop[1] - start[1]) / 3
    h = math.sqrt(dx**2 + dy**2)
    angle = math.asin(dy/h)
    one = (start[0] + dx, start[1] + dy)
    two = (one[0] + dx, one[1] + dy)
    half = (one[0] + math.cos(math.radians(60)) + angle) * h, (one[1] + math.sin(math.radians(60)) * h)

    fractal.add(fractal.line(start, one, stroke = "white", stroke_linecap="round", stroke_width=4))
    fractal.add(fractal.line(two, stop, stroke = "white", stroke_linecap="round", stroke_width=4))

    fractal.add(fractal.line(one, half, stroke = "white", stroke_linecap="round", stroke_width=4))
    fractal.add(fractal.line(half, two, stroke = "white", stroke_linecap="round", stroke_width=4))

size = 800, 800
center = size[0] / 2, size[1] / 2
radius = size[0] * 0.25

fractal = svg.Drawing(filename="svgs/image.svg", size=size, profile="tiny")

fractal.add(fractal.rect((0,0), size, fill=svg.rgb(20,20,20)))
6
A = center[0] + math.cos(math.radians(150)) * radius, center[1] + math.sin(math.radians(150)) * radius
B = center[0] + math.cos(math.radians(30)) * radius, center[1] + math.sin(math.radians(30)) * radius
C = center[0] + math.cos(math.radians(270)) * radius, center[1] + math.sin(math.radians(270)) * radius

line(A,B)
line(B,C)
line(C,A)


fractal.save(pretty=True)