import data, random
from collections import Counter

if __name__ == "__main__":
    # Creating the line and data for the points.
    line = data.create_line()
    training_data = data.label_points(data.create_points(100), line)
    testing_data = data.create_points(100)

    # Displaying all the data:
    # data.display(training_data, testing_data, line=line)º


    weights = [random.random() * 2 - 1, random.random() * 2 - 1]
    print(weights)
    biases = [1, 1]

    def step_activation(value):
        if value > 0:
            return 1
        else:
            return 0 
        
    def normalise_point(point):
        normalised = point / 100
        return normalised

    def feed_forward(point):
        normalised = normalise_point(point)
        output = normalised[0] * weights[0] * biases[0] + normalised[1] * weights[1] * biases[1]
        activation = step_activation(output)
        return activation

    def predict(points):
        guesses = []
        for point in points:
            activation = feed_forward(point)
            guesses.append([*point[:2], activation])
        return guesses

    def train(LEARNING_RATE=0.05):
        correct = True
        wrong_guesses = 0
        for point, guess in zip(training_data, guesses[-1]):
            error = point[2] - guess[2]
            errors.append(error)
            normalised = normalise_point(point)
            weights[0] += normalised[0] * error * LEARNING_RATE
            weights[1] += normalised[1] * error * LEARNING_RATE
            # print(normalised[0] * error * LEARNING_RATE, normalised[1] * error * LEARNING_RATE)
            # print(weights)
            if guess[2] != point[2]:
                correct = False
                wrong_guesses += 1
        # exit()
        if not correct:
            new_guesses = predict(testing_data)
            guesses.append(new_guesses)
            train()
        else:
            return
            
    errors = []
    guesses = [predict(training_data)]
    try:
        train()
    except Exception as e:
        print("Exited with error:", e)
    counts = Counter(errors)
    print(counts)
    print(weights)
    data.display(*guesses, line=line)

    # data.display(guesses, line=line)