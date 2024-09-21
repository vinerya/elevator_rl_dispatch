# Elevator Dispatch System with Reinforcement Learning

This project implements an elevator dispatch system using reinforcement learning techniques. The system simulates a building with multiple elevators and floors, and uses the PPO (Proximal Policy Optimization) algorithm from Stable Baselines3 to optimize elevator dispatching.

## Project Structure

- `main.py`: Entry point of the application, handles training, evaluation, and GUI simulation.
- `elevator_env.py`: Defines the OpenAI Gym environment for the elevator system.
- `building.py`: Defines the `Building` class, which represents the environment.
- `elevator.py`: Defines the `Elevator` class.
- `gui.py`: Implements a graphical user interface for the simulation using tkinter.
- `test_elevator_system.py`: Contains unit tests for the core components.

## Features

- Simulated building with configurable number of floors and elevators
- OpenAI Gym environment for standardized RL training
- PPO algorithm from Stable Baselines3 for elevator dispatching
- GUI for visual representation of the elevator system
- Options for training, evaluating, and visualizing the RL agent's performance

## Setup and Running

1. Ensure you have Python 3.7+ installed.
2. Install the required libraries:
   ```
   pip install gym stable-baselines3 tkinter
   ```
3. Run the simulation:

   - To train the RL agent:
     ```
     python main.py --train --floors 15 --elevators 4 --timesteps 200000
     ```

   - To evaluate the trained agent:
     ```
     python main.py --evaluate --episodes 20
     ```

   - To run the GUI simulation:
     ```
     python main.py --gui
     ```

   - You can also customize the simulation parameters:
     ```
     python main.py --train --floors 20 --elevators 5 --timesteps 500000
     ```

4. To run the unit tests:
   ```
   python -m unittest test_elevator_system.py
   ```

## How it Works

1. The `ElevatorEnv` class defines an OpenAI Gym environment that simulates the elevator system.
2. The PPO algorithm from Stable Baselines3 is used to train an RL agent to optimize elevator dispatching.
3. During training, the agent learns to make decisions on which elevator to move and where, based on the current state of the building.
4. The trained model can be evaluated to assess its performance in managing the elevator system.
5. The GUI provides a visual representation of the elevator system's behavior, allowing users to step through the simulation and observe the agent's decisions.

## Current State and Limitations

The current implementation provides a robust framework for an elevator dispatch system using reinforcement learning, leveraging OpenAI Gym and Stable Baselines3. However, it still has some limitations:

1. The passenger generation is simplistic and may not reflect real-world patterns.
2. The reward function may need further refinement to optimize for various objectives (e.g., minimizing wait times, energy efficiency).
3. The current implementation uses a single RL algorithm (PPO). Other algorithms might perform differently.

## Future Improvements

To enhance the project further, consider the following improvements:

1. Implement more realistic passenger generation patterns, possibly based on real-world data.
2. Enhance the GUI with real-time performance graphs and more interactive features.
3. Experiment with different RL algorithms available in Stable Baselines3 (e.g., A2C, DQN, SAC).
4. Implement more sophisticated reward functions that consider factors like energy efficiency and passenger waiting times.
5. Add more comprehensive unit tests and integration tests to ensure robustness.
6. Optimize the Gym environment for better performance, especially for larger simulations.
7. Implement additional performance metrics and data analysis tools to gain deeper insights into the system's behavior.
8. Add support for different elevator types (e.g., express elevators, service elevators) with varying capacities and speeds.

Feel free to contribute to this project by submitting pull requests or opening issues for suggestions and bug reports.