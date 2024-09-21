import unittest
import numpy as np
from elevator_env import ElevatorEnv
from building import Building, Passenger
from elevator import Elevator

class TestElevatorSystem(unittest.TestCase):
    def setUp(self):
        self.env = ElevatorEnv(num_floors=5, num_elevators=2)

    def test_env_initialization(self):
        self.assertEqual(self.env.building.num_floors, 5)
        self.assertEqual(len(self.env.building.elevators), 2)
        self.assertEqual(len(self.env.building.waiting_passengers), 5)

    def test_env_reset(self):
        initial_obs = self.env.reset()
        self.assertIsInstance(initial_obs, np.ndarray)
        self.assertEqual(initial_obs.shape, (12,))  # 2 elevators * 2 + 5 floors = 9

    def test_env_step(self):
        self.env.reset()
        action = 0  # Move first elevator to ground floor
        obs, reward, done, info = self.env.step(action)
        self.assertIsInstance(obs, np.ndarray)
        self.assertIsInstance(reward, float)
        self.assertIsInstance(done, bool)
        self.assertIsInstance(info, dict)

    def test_elevator_movement(self):
        elevator = self.env.building.elevators[0]
        initial_floor = elevator.current_floor
        self.env.building.take_action((0, 3))  # Move first elevator to floor 3
        self.env.building.step()
        self.assertNotEqual(elevator.current_floor, initial_floor)

    def test_passenger_generation(self):
        initial_passengers = sum(len(passengers) for passengers in self.env.building.waiting_passengers.values())
        self.env.building._generate_passengers()
        new_passengers = sum(len(passengers) for passengers in self.env.building.waiting_passengers.values())
        self.assertGreaterEqual(new_passengers, initial_passengers)

if __name__ == '__main__':
    unittest.main()