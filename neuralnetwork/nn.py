import data, random, math
from collections import Counter

class NeuralNetwork:
    def __init__(self, activation):
        self.weights = [random.random() * 2 - 1, random.random() * 2 - 1]
        self.input_weights = [random.random() * 2 - 1, random.random() * 2 - 1]
        self.hidden_weights = [random.random() * 2 - 1, random.random() * 2 - 1]
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
    def sigmoid_derivative(value):
        return math.exp(value) / (1 + math.exp(value)) ** 2
    
    @staticmethod
    def scale_point(point):
        scaled = point / 100
        return scaled

    @staticmethod
    def normalise(values):
        total = sum(values)
        return [value / total for value in values]

    def feed_forward(self, inputs):
        iw, hw = self.input_weights, self.hidden_weights
        scaled = NeuralNetwork.scale_point(inputs)

        hidden = [
        scaled[0] * iw[0] + scaled[1] + iw[0],
        scaled[0] * iw[1] + scaled[1] * iw[1]
        ]
        # print(scaled)
        hidden_activations = [self.activation(hidden[i]) for i in range(len(hidden))]

        output = hidden_activations[0] * hw[0] + hidden_activations[1] * hw[1]
        output_activation = self.activation(output)

        # print(f"{inputs = }\n{scaled = }\n{hidden = }\n{hidden_activations = }\n{output = }\n{output_activation = }")

        return output_activation

    def predict(self, points):
        guesses = []
        for point in points:
            activation = self.feed_forward(point)
            guesses.append([*point[:2], activation])
        return guesses

    def backpropagate(self, point, label, LEARNING_RATE=0.05):
        guess = self.feed_forward(point)
        error = label - guess
        error_derivative = NeuralNetwork.sigmoid_derivative(error)
        scaled = NeuralNetwork.scale_point(point)
        deltas = [[0, 0], [0, 0]]
        deltas[0][0] += point[0] * error_derivative
        deltas[0][1] += point[1] * error_derivative
        norm_weight = NeuralNetwork.normalise(self.input_weights)

        deltas[1][0] = deltas[0][0] * norm_weight[0] + deltas[0][1] * norm_weight[0] 
        deltas[1][1] = deltas[0][0] * norm_weight[1] + deltas[0][1] * norm_weight[1] 

        self.input_weights[0] += deltas[1][0] * LEARNING_RATE
        self.input_weights[1] += deltas[1][1] * LEARNING_RATE
        self.input_weights[0] += deltas[0][0] * LEARNING_RATE
        self.input_weights[1] += deltas[0][1] * LEARNING_RATE


    def train(self, training_data, LEARNING_RATE=0.05):
        correct = True
        for point, guess in zip(training_data, self.guesses[-1]):
            self.backpropagate(point[:2], point[2])

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