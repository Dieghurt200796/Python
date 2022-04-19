import csv, arcade, time

def map_value(value, min_in, max_in, min_out, max_out):
    range_in = max_in - min_in
    range_out = max_out - min_out

    return (value - min_in) / range_in *range_out + min_out

with open("meteors/data.csv", "r", encoding = "utf-8") as file:
    reader = csv.DictReader(file)
    data = list(reader)

class Display(arcade.Window):
    def __init__(self):
        super().__init__(1200, 600, "Meteor Landings", fullscreen=False)

        self.coordinates = []
        self.coord_filter = set()
        self.created = 0
        self.start_time = time.time()
        for meteor in data:
            try:
                lat = float(meteor["reclat"])
                long = float(meteor["reclong"])
                mass = float(meteor["mass (g)"])
                if lat != 0 and long != 0 and mass != 0:
                    x = (long + 180)/360 * self.width
                    y = (lat + 90)/180 * self.height
                    rounded = round(x, 2), round(y, 2), mass
                    self.coord_filter.add(rounded)
            except ValueError:
                continue
        self.coordinates = list(self.coord_filter)
        print(len(self.coordinates))
        
        # Initialise the generator
        self.shape_generator = self.create_shapes()
        self.graphics = []

    def create_shapes(self):
        for x, y, mass in self.coordinates:
            size = map_value(mass, 0.01, 60000000, 2, 100)
            vertex_buffer = arcade.create_ellipse_filled(x, y, size, size, (255,0,0,100))
            yield vertex_buffer

    def on_draw(self):
        arcade.start_render()
        for shapes in self.graphics:
            shapes.draw()
        arcade.draw_text("Frame Rate: " + str(self.last_update), 0, 0)

    def on_update(self, delta_time):
        self.last_update = round(1 / delta_time, 1)
        if self.created < len(self.coordinates):
            start = time.time()
            shapes = arcade.ShapeElementList()

            try:
                while time.time() - start <= 1/70:
                    vertex_buffer = next(self.shape_generator)
                    shapes.append(vertex_buffer)
                    self.created += 1
                self.graphics.append(shapes)
            except StopIteration:
                print("Stopped Displaying Meteors. Took " + str(round(time.time() - self.start_time, 3)))

display = Display()
arcade.run()

largest_mass = 0
smallest_mass = display.coordinates[1][2]

for coordinates in display.coordinates:
    if largest_mass < coordinates[2]:
        largest_mass = coordinates[2]

    if smallest_mass > coordinates[2]:
        smallest_mass = coordinates[2]

print("Largest mass =", largest_mass, "\nSmallest mass =", smallest_mass)