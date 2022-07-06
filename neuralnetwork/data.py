import matplotlib.pyplot as plt, numpy as np, random


def classify(point, line):
    above_line = 0
    line_gradient = line[1][1] / line[1][0]
    point_gradient = point[1] / point[0]
    if point_gradient > line_gradient:
        above_line = 1
    return above_line

def label_points(points, line):
    labelled = [] # Create a numpy array which will contain the coordinates of labelled points, and whether they are on top of the line or not
    for point in points:
        labelled.append((*point, classify(point, line))) # Add coordinates (asterisk separates them)
    labelled_array = np.array(labelled)
    return labelled_array

def create_points(amount=100):
    points = np.random.random(size = (amount, 2)) * 98 + 1 # Add 1000 different random coordinates
    return points

def create_line():
    line = np.array([(0,0), (100, random.random()* 80 + 20)]) # Start and end coordinates of the line. Line is always at x = 100 or y = 100, the other coordinate is 20 + a random number between 0 and 80 (20 is a lower bound buffer)
    if random.randint(0, 100) % 2: # Deciding whether the x or the y of the line's end is 100.
        line[1][::-1] # If y has been chosen, flipping the array's 1st index to make the end of y 100.
    return line

def draw(line):
    plt.style.use("ggplot") #Changing colour of points and line
    plt.figure(figsize=(5,5)) # Makes the graph a square, which is rectangular by default
    while True:
        points = yield
        if points is None:
            break
        points_array = np.array(points)
        if points_array.shape[1] == 3: # If each tuple in the array has 3 values, it will be the training data. If not, it will be unlabeled and therefore testing data.
            colours = [("blue" if label == 1 else "green") for label in points_array[:, 2]]
        else:
            colours = "red"
        plt.scatter(points_array[:,0], points_array[:,1], s=1, c = colours) # Plotting the points
    plt.plot(line[:,0],line[:,1]) # Plotting the line
    plt.show() # Displaying the graph

def display(*points, line):
    try:
        # Initialising the generator:
        displayer = draw(line)

        next(displayer)
        # Sending the data to the generator:
        for p in points:
            displayer.send(p)

        # Avoiding an error:
        next(displayer)
    except StopIteration:
        pass
