# blueprints for objects
# start with uppercase


class Vehicle:
    def __init__(self, make, model):  # initializer function
        self.make = make
        self.model = model

    def moves(self):  # self is referring to itself
        print("Moves along...")

    def get_make_model(self):
        print(f"I'm a {self.make} {self.model}")


my_car = Vehicle("Tesla", "Model 3")
# print(my_car.make)
# print(my_car.model)
my_car.get_make_model()
my_car.moves()

your_car = Vehicle("Cadillac", "Escalade")
your_car.get_make_model()
your_car.moves()


# inheritance
class Airplane(Vehicle):
    def __init__(
        self, make, model, faa_id
    ):  # overwrites the entire init function from Vehicle
        super().__init__(make, model)
        self.faa_id = faa_id

    def moves(self):
        print("Flies along...")


class Truck(Vehicle):
    def moves(self):
        print("Rumbles along...")


class GolfCart(Vehicle):
    pass  # inherits everything as it is


cessna = Airplane("Cessna", "Skyhawk", "N-12345")
mac = Truck("Mac", "Pinnacle")
golfwagon = GolfCart("Yamaha", "GC100")

cessna.get_make_model()
cessna.moves()
mac.get_make_model()
mac.moves()
golfwagon.get_make_model()
golfwagon.moves()

print("\n\n")

# polymorphism - the ability to behave differently with the same input message
for v in (my_car, your_car, cessna, mac, golfwagon):
    v.get_make_model()
    v.moves()
