
# class Direction:
#     north = 1
#     east = 2
#     south = 3
#     west = 4


# if player.looking == Direction.east:
#     pass


class Restaurant:
    def __init__(self, y, x, z):
        self.employees = 15
        self.total_seats = x
        self.customers = 5

    def check_empty_seats(self):
        empties = self.total_seats - self.customers
        print("There are", empties, "available seats.")



london = Restaurant(None, 40, None)
london.employees = 10
london.total_seats = 40
london.customers = 4



madrid = Restaurant(None, 200, None)
madrid.employees = 50
madrid.total_seats = 200
madrid.customers = 180

madrid.check_empty_seats()
london.check_empty_seats()

print(hex(id(madrid)))
print(hex(id(london)))