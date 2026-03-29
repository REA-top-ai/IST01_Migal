# task 1
class Facade:
    pass

# task 2
facade_1 = Facade()

# task 3
facade_1_type = type(facade_1)

# task 4
print(facade_1_type)

# task 5
class Grade:
    minimum_passing = 65

# task 6
class Rules:
    def washing_brushes(self):
        return "Point bristles towards the basin while washing your brushes."

# task 7
class Circle:
    pi = 3.14

    # task 8
    def __init__(self, diameter):
        # task 9
        print(f"New circle with diameter: {diameter}")
        # task 10
        self.radius = diameter / 2

    # task 11
    def area(self, radius):
        return self.pi * radius ** 2

    # task 12
    def circumference(self):
        return 2 * self.pi * self.radius

    # task 13
    def __repr__(self):
        return f"Circle with radius {self.radius}"

# task 14
medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)

# task 15
print(medium_pizza.circumference())
print(teaching_table.circumference())
print(round_room.circumference())

# task 16
print(medium_pizza)
print(teaching_table)
print(round_room)

# task 17
print(dir(5))

# task 18
def this_function_is_an_object():
    return "I am an object"

# task 19
print(dir(this_function_is_an_object))
