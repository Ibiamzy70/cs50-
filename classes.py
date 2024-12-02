class flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def add_passenger(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True

    def open_seats(self):
        return self.capacity - len(self.passengers)


flight = flight(3)

people = ["harry", "ron", "hermoine", "ginny"]

for person in people:
    success = flight.add_passenger(person)
    if success: 
        print(f"added {person} to flight successfully.")
    else:
        print(f"no available seats for {person}")