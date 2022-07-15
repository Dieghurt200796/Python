import matplotlib.pyplot as plt, numpy as np, random, itertools
from matplotlib.animation import FuncAnimation


def classify(point, line):
    dx = line[1][0] - line[0][0]
    dy = line[1][1] - line[0][1]
    gradient = dy / dx
    c = line[0][1] - gradient * line[0][0]
    line_y = gradient * point[0] + c
    if point[1] > line_y:
        return 1
    else:
        return 0

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
    fixed_start = random.choice([-100,100])
    fixed_end = random.choice([-100, 100])
    line = np.array([(fixed_start, random.random() * 200 - 100), (fixed_end, random.random()* 200 - 100)]) # Start and end coordinates of the line. Line is always at x = 100 or y = 100, the other coordinate is 20 + a random number between 0 and 80 (20 is a lower bound buffer)
    for i in range(2):
        if random.randint(0, 100) % 2:
            line[i][::-1] # If y has been chosen, flipping the array's 1st index
    if line[0][0] == line[1][0] or line [0][1] == line[1][1]:
        print("Failed:", line)
        return create_line()
    else:
        print("Succeeded:", line)
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
            colours = [((0, 0, 1, confidence) if confidence > 0.5 else (0, 1, 0, (1 - confidence))) for confidence in points_array[:, 2]]
        else:
            colours = [(1, 0, 0, confidence) for confidence in points_array[:, 2]]
        gathered_points.append(points_array)
        all_colours.append(colours)

    gathered_points = np.array(gathered_points)


    figure, axes = plt.subplots(figsize=(5,5))
    axes.set_xlim((-105, 105))
    axes.set_ylim((-105, 105))
    sct = axes.scatter([], [])

    def step(index):
        sct.set_offsets(gathered_points[index, :, :2])
        sct.set_color(all_colours[index])
        axes.set_title(index)
        return sct
    
    animation = FuncAnimation(figure, step, frames=len(gathered_points), interval=50, repeat=False, init_func=lambda *args, **kwargs : None)

    if line is not None:
        plt.plot(line[:,0],line[:,1]) # Plotting the line

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
