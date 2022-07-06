import data

if __name__ == "__main__":
    # Creating the line and data for the points.
    line = data.create_line()
    training_data = data.label_points(data.create_points(500), line)
    testing_data = data.create_points(500)

    # Displaying all the data:
    data.display(training_data, testing_data, line=line)

