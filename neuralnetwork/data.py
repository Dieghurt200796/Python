import matplotlib.pyplot as plt, numpy as np, random, itertools
from matplotlib.animation import FuncAnimation


def classify(point, line):
    c = 0
    above_line = 0
    line_gradient = line[1][1] / line[1][0]
    line_y = line_gradient * point[0] + c
    point_gradient = point[1] / point[0]
    if point[1] > line_y:
        above_line = 1
    return above_line

def label_points(points, line):
    labelled = [] # Create a numpy array which will contain the coordinates of labelled points, and whether they are on top of the line or not
    for point in points:
        labelled.append((*point, classify(point, line))) # Add coordinates (asterisk separates them)
    labelled_array = np.array(labelled)
    return labelled_array

def create_points(amount=100):
    points = np.random.random(size = (amount, 2)) * 200 - 100 # Add 1000 different random coordinates
    return points

def create_line():
    fixed = random.choice([-100,100])
    line = np.array([(0,0), (fixed, random.random()* 200 - 100)]) # Start and end coordinates of the line. Line is always at x = 100 or y = 100, the other coordinate is 20 + a random number between 0 and 80 (20 is a lower bound buffer)
    if random.randint(0, 100) % 2:
        line[1][::-1] # If y has been chosen, flipping the array's 1st index
    return line

def draw(line):
    plt.style.use("ggplot") #Changing colour of points and line
    gathered_points = []
    all_colours = []
    while True:
        points = yield
        if points is None:
            break
        points_array = np.array(points)
        if points_array.shape[1] == 3: # If each tuple in the array has 3 values, it will be the training data. If not, it will be unlabeled and therefore testing data.
            colours = [("blue" if label == 1 else "green") for label in points_array[:, 2]]
        else:
            colours = ["red"] * len(points_array)
        gathered_points.append(points_array)
        all_colours.append(colours)

    gathered_points = np.array(gathered_points)


    figure, axes = plt.subplots(figsize=(5,5))
    axes.set_xlim((-100, 100))
    axes.set_ylim((-100, 100))
    sct = axes.scatter([], [])

    def step(index):
        sct.set_offsets(gathered_points[index, :, :2])
        sct.set_color(all_colours[index])
        axes.set_title(index)
        return sct

    animation = FuncAnimation(figure, step, frames=len(gathered_points), interval=50, repeat=False, init_func=lambda *args, **kwargs : None)

    if line is not None:
        plt.plot(line[:,0],line[:,1]) # Plotting the line
        plt.plot(line[:,0] * -1, line[:,1] * -1, ls=':') # Plotting the dotted line  which continues the line

    plt.show() # Displaying the graph

def display(*points, line=None):
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
