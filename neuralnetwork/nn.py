import data, random, math
from collections import Counter

class NeuralNetwork:
    def __init__(self, activation):
        self.weights = [random.random() * 2 - 1, random.random() * 2 - 1]
        self.input_weights = [random.random() * 2 - 1, random.random() * 2 - 1]
        self.hidden_weights = [random.random() * 2 - 1, random.random() * 2 - 1]

        self.hidden_biases = [0, 0]

        self.activation = activation

    @staticmethod
    def step_activation(value):
        if value > 0:
            return 1
        else:
            return -1

    @staticmethod
    def sigmoid_activation(value):
        return 2 / (1 + math.exp(-value)) - 1 # Sigmoid function, only multiplied by 2 and subtracted 1, as values too close to 0 were giving errors.

    @staticmethod
    def sigmoid_derivative(value):
        return math.exp(value) / (1 + math.exp(value)) ** 2
    
    @staticmethod
    def scale_point(point):
        scaled = point / 100
        return scaled

    @staticmethod
    def normalise(values):
        offset = abs(min(values))
        total = sum(values) + offset * len(values)
        return [(value + offset) / total for value in values]

    def feed_forward(self, inputs):
        iw, hw = self.input_weights, self.hidden_weights
        scaled = NeuralNetwork.scale_point(inputs)

        self.hidden = [
        scaled[0] * iw[0] + scaled[1] * iw[0] + self.hidden_biases[0],
        scaled[0] * iw[1] + scaled[1] * iw[1] + self.hidden_biases[1]
        ]
        
        hidden_activations = [self.activation(self.hidden[i]) for i in range(len(self.hidden))]

        output = hidden_activations[0] * hw[0] + hidden_activations[1] * hw[1]
        output_activation = self.activation(output)

        
        return output_activation

    def predict(self, points):
        guesses = []
        for point in points:
            activation = self.feed_forward(point)
            guesses.append([*point[:2], activation])
        return guesses

    def backpropagate(self, point, label, learning_rate=0.05):
        guess = self.feed_forward(point)
        error = label - guess
        gradient = NeuralNetwork.sigmoid_derivative(guess)
        error_derivative = error * gradient

        scaled = NeuralNetwork.scale_point(point)
        deltas = [[0, 0], [0, 0]]

        hw_normalised = NeuralNetwork.normalise(self.input_weights)

        deltas[0][0] += hw_normalised[0] * error_derivative
        deltas[0][1] += hw_normalised[1] * error_derivative
        iw_normalised = NeuralNetwork.normalise(self.input_weights)
        hidden_normalised = NeuralNetwork.normalise(self.hidden)

        gradients = [
            NeuralNetwork.sigmoid_derivative(hidden_normalised[0]),
            NeuralNetwork.sigmoid_derivative(hidden_normalised[1])
        ]


        deltas[1][0] = gradients[0] * iw_normalised[0] * deltas[0][0] + gradients[1] * iw_normalised[0] 
        deltas[1][1] = gradients[0] * iw_normalised[1] * deltas[0][1] + gradients[1] * iw_normalised[1] 

        self.input_weights[0] += deltas[1][0] * learning_rate * scaled[0]
        self.input_weights[1] += deltas[1][1] * learning_rate * scaled[1]
        self.hidden_weights[0] += deltas[0][0] * learning_rate * scaled[0]
        self.hidden_weights[1] += deltas[0][1] * learning_rate * scaled[1]

        self.hidden_biases[0] += deltas[0][0]
        self.hidden_biases[1] += deltas[0][1]

    def train(self, training_data, learning_rate=0.05, file=None):
        correct = True
        for point, guess in zip(training_data, self.guesses[-1]):
            self.backpropagate(point[:2], point[2])

            error = point[2] - guess[2]
            scaled = NeuralNetwork.scale_point(point)
            self.weights[0] += scaled[0] * error * learning_rate
            self.weights[1] += scaled[1] * error * learning_rate
            if guess[2] != point[2]:
                correct = False
        if not correct:
            try:
                new_guesses = self.predict(training_data)
                self.guesses.append(new_guesses)
                if file:
                    file.write(str(self))
                self.train(training_data, learning_rate = learning_rate, file = file)
            except:
                pass
        else:
            return

    def begin_training(self, training_data, learning_rate=0.05):
        file = open("neuralnetwork/nndata.txt", "w")
        self.guesses = [self.predict(training_data)]
        try:
            self.train(training_data, learning_rate=learning_rate, file=file)
        except Exception as e:
            print("Exited with error:", e)
        file.close()

    def __str__(self):
        return f""" 
Weights: {self.input_weights}, {self.hidden_weights}
Biases: {self.hidden_biases}"""


if __name__ == "__main__":
    # Creating the line and data for the points.
    line = data.create_line()
    training_data = data.label_points(data.create_points(1000), line)
    testing_data = data.create_points(1000)

    nn = NeuralNetwork(NeuralNetwork.sigmoid_activation)

    nn.begin_training(training_data)

    guesses = nn.predict(training_data) 
    data.display(guesses, line=line)

    data.display(*nn.guesses, line=line)
