class Elevator:
    def __init__(self, id, num_floors):
        self.id = id
        self.current_floor = 0
        self.destination = None
        self.passengers = []
        self.num_floors = num_floors

    def move(self):
        if self.destination is not None:
            if self.current_floor < self.destination:
                self.current_floor += 1
            elif self.current_floor > self.destination:
                self.current_floor -= 1
            else:
                self.destination = None

    def add_passenger(self, passenger):
        self.passengers.append(passenger)

    def remove_passengers(self):
        remaining_passengers = []
        for passenger in self.passengers:
            if passenger.destination == self.current_floor:
                # Passenger has reached their destination
                pass
            else:
                remaining_passengers.append(passenger)
        self.passengers = remaining_passengers

    def is_empty(self):
        return len(self.passengers) == 0

    def __str__(self):
        return f"Elevator {self.id} at floor {self.current_floor}"