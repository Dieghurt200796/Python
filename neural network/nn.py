import matplotlib.pyplot as plt, numpy as np, random


def classify(point):
    above_line = 0
    line_gradient = line[1][1] / line[1][0]
    point_gradient = point[1] / point[0]
    if point_gradient > line_gradient:
        above_line = 1
    return above_line

def label_points(points):
    labelled = [] # Create a numpy array which will contain the coordinates of labelled points, and whether they are on top of the line or not
    for point in points:
        labelled.append((*point, classify(point))) # Add coordinates (asterisk separates them)
    labelled_array = np.array(labelled)
    return labelled_array

def create_points():
    points = np.random.random(size = (1000, 2)) * 100 # Add 1000 different random coordinates
    return points

def create_line():
    line = np.array([(0,0), (100, random.random()* 80 + 20)]) # Start and end coordinates of the line. Line is always at x = 100 or y = 100, the other coordinate is 20 + a random number between 0 and 80 (20 is a lower bound buffer)
    if random.randint(0, 100) % 2: # Deciding whether the x or the y of the line's end is 100.
        line[1][::-1] # If y has been chosen, flipping the array's 1st index to make the end of y 100.
    return line

def display(labelled_points, line):
    plt.style.use("ggplot") #Changing colour of points and line
    plt.figure(figsize=(5,5)) # Makes the graph a square, which is rectangular by default
    for labelled_point in labelled_points:
        if labelled_point[2] == 1:
            plt.scatter(labelled_point[0], labelled_point[1], s=1, c = "b") # Plotting the points above the line in blue
        else:
            plt.scatter(labelled_point[0], labelled_point[1], s=1, c = "g") # Plotting the points below the line in green
    plt.plot(line[:,0],line[:,1]) # Plotting the line

points = create_points()
line = create_line()
labelled = label_points(points[:500])

display(labelled, line)

plt.show() # Displaying the graph
