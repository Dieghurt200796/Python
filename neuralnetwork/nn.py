import data, random

if __name__ == "__main__":
    # Creating the line and data for the points.
    line = data.create_line()
    training_data = data.label_points(data.create_points(500), line)
    testing_data = data.create_points(500)

    # Displaying all the data:
    # data.display(training_data, testing_data, line=line)º


    weights = [random.random() * 2 - 1, random.random() * 2 - 1]
    biases = [1, 1]

    def step_activation(value):
        if value > 0:
            return 1
        else:
            return 0 

    def feed_forward(point):
        output = point[0] * weights[0] * biases[0] + point[1] * weights[1] * biases[1]
        activation = step_activation(output)
        return activation

    guesses = []
    for point in testing_data:
        activation = feed_forward(point / 100)
        guesses.append([*point, activation])
    
    
    #data.display(guesses)
    data.display(guesses, line=line)
    data.display(training_data, line=line)