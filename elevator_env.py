import gym
from gym import spaces
import numpy as np
from building import Building

class ElevatorEnv(gym.Env):
    def __init__(self, num_floors=10, num_elevators=3):
        super(ElevatorEnv, self).__init__()
        
        self.building = Building(num_floors, num_elevators)
        
        # Define action and observation space
        self.action_space = spaces.Discrete(num_floors * num_elevators)
        
        # Observation space: elevator positions, elevator passengers, waiting passengers
        self.observation_space = spaces.Box(
            low=0,
            high=max(num_floors, 10),  # Assume max 10 passengers per elevator or floor
            shape=(num_elevators * 2 + num_floors,),
            dtype=np.int32
        )

    def reset(self):
        self.building = Building(self.building.num_floors, len(self.building.elevators))
        return self._get_observation()

    def step(self, action):
        elevator_id = action % len(self.building.elevators)
        destination_floor = action // len(self.building.elevators)
        
        self.building.step()
        reward = self.building.take_action((elevator_id, destination_floor))
        
        done = False  # You might want to define an episode end condition
        info = {}
        
        return self._get_observation(), reward, done, info

    def _get_observation(self):
        obs = []
        for elevator in self.building.elevators:
            obs.append(elevator.current_floor)
            obs.append(len(elevator.passengers))
        for floor in range(self.building.num_floors):
            obs.append(len(self.building.waiting_passengers[floor]))
        return np.array(obs)

    def render(self, mode='human'):
        # Implement rendering if needed
        pass