import data, random, math
from collections import Counter

class NeuralNetwork:
    def __init__(self, activation):
        self.weights = [random.random() * 2 - 1, random.random() * 2 - 1]
        self.activation = activation

    @staticmethod
    def step_activation(value):
        if value > 0:
            return 1
        else:
            return 0 

    @staticmethod
    def sigmoid_activation(value):
        return 1 / (1 + math.exp(-value))
    
    @staticmethod
    def scale_point(point):
        scaled = point / 100
        return scaled

    @staticmethod
    def normalise(values):
        total = sum(values)
        return [value / total for value in values]

    def feed_forward(self, point):
        scaled = NeuralNetwork.scale_point(point)
        output = scaled[0] * self.weights[0] + scaled[1] * self.weights[1]
        activation = self.activation(output)

        return activation

    def predict(self, points):
        guesses = []
        for point in points:
            activation = self.feed_forward(point)
            guesses.append([*point[:2], activation])
        return guesses

    def train(self, training_data, LEARNING_RATE=0.05):
        correct = True
        for point, guess in zip(training_data, self.guesses[-1]):
            error = point[2] - guess[2]
            scaled = NeuralNetwork.scale_point(point)
            self.weights[0] += scaled[0] * error * LEARNING_RATE
            self.weights[1] += scaled[1] * error * LEARNING_RATE
            if guess[2] != point[2]:
                correct = False
        if not correct:
            new_guesses = self.predict(training_data)
            self.guesses.append(new_guesses)
            self.train(training_data)  
        else:
            return

    def begin_training(self, training_data, LEARNING_RATE=0.05):
        self.guesses = [self.predict(training_data)]
        try:
            self.train(training_data)
        except Exception as e:
            print("Exited with error:", e)


if __name__ == "__main__":
    # Creating the line and data for the points.
    line = data.create_line()
    training_data = data.label_points(data.create_points(1000), line)
    testing_data = data.create_points(1000)

    nn = NeuralNetwork(NeuralNetwork.sigmoid_activation)
    guesses = nn.predict(training_data) 
    data.display(guesses, line=line)

    nn.begin_training(training_data)
    data.display(*nn.guesses, line=line)