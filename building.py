import random
from elevator import Elevator

class Passenger:
    def __init__(self, start_floor, destination_floor):
        self.start_floor = start_floor
        self.destination = destination_floor

class Building:
    def __init__(self, num_floors, num_elevators):
        self.num_floors = num_floors
        self.elevators = [Elevator(i, num_floors) for i in range(num_elevators)]
        self.waiting_passengers = {floor: [] for floor in range(num_floors)}
        self.state = self._get_state()
        self.next_state = None

    def step(self):
        # Move elevators
        for elevator in self.elevators:
            elevator.move()
            elevator.remove_passengers()

        # Generate new passengers
        self._generate_passengers()

        # Update state
        self.state = self.next_state if self.next_state else self._get_state()
        self.next_state = self._get_state()

    def take_action(self, action):
        # action is a tuple (elevator_id, destination_floor)
        elevator_id, destination_floor = action
        self.elevators[elevator_id].destination = destination_floor

        # Calculate reward based on waiting times, travel times, etc.
        reward = self._calculate_reward()

        return reward

    def _generate_passengers(self):
        # Randomly generate new passengers
        for floor in range(self.num_floors):
            if random.random() < 0.1:  # 10% chance of new passenger per floor
                destination = random.choice([f for f in range(self.num_floors) if f != floor])
                self.waiting_passengers[floor].append(Passenger(floor, destination))

    def _get_state(self):
        # Return a representation of the current state
        # This could include elevator positions, passenger waiting times, etc.
        return {
            'elevator_positions': [elevator.current_floor for elevator in self.elevators],
            'waiting_passengers': {floor: len(passengers) for floor, passengers in self.waiting_passengers.items()}
        }

    def _calculate_reward(self):
        # Calculate a reward based on the current state
        # This could consider factors like total waiting time, energy efficiency, etc.
        total_waiting_passengers = sum(len(passengers) for passengers in self.waiting_passengers.values())
        return -total_waiting_passengers  # Simple reward: negative of total waiting passengers

    def __str__(self):
        return f"Building with {self.num_floors} floors and {len(self.elevators)} elevators"