import argparse
from stable_baselines3 import PPO
from stable_baselines3.common.env_util import make_vec_env
from elevator_env import ElevatorEnv
from gui import run_gui

def train_agent(num_floors, num_elevators, total_timesteps):
    env = make_vec_env(lambda: ElevatorEnv(num_floors, num_elevators), n_envs=1)
    model = PPO("MlpPolicy", env, verbose=1)
    model.learn(total_timesteps=total_timesteps)
    model.save("elevator_ppo_model")
    return model

def evaluate_agent(model, num_episodes):
    env = ElevatorEnv()
    for episode in range(num_episodes):
        obs = env.reset()
        done = False
        total_reward = 0
        while not done:
            action, _ = model.predict(obs, deterministic=True)
            obs, reward, done, _ = env.step(action)
            total_reward += reward
        print(f"Episode {episode + 1}: Total Reward: {total_reward}")

def main():
    parser = argparse.ArgumentParser(description="Elevator Dispatch System Simulation")
    parser.add_argument("--gui", action="store_true", help="Run the simulation with GUI")
    parser.add_argument("--train", action="store_true", help="Train the RL agent")
    parser.add_argument("--evaluate", action="store_true", help="Evaluate the trained RL agent")
    parser.add_argument("--floors", type=int, default=10, help="Number of floors in the building")
    parser.add_argument("--elevators", type=int, default=3, help="Number of elevators in the building")
    parser.add_argument("--timesteps", type=int, default=100000, help="Total timesteps for training")
    parser.add_argument("--episodes", type=int, default=10, help="Number of episodes for evaluation")
    
    args = parser.parse_args()

    if args.train:
        model = train_agent(args.floors, args.elevators, args.timesteps)
        print("Training completed. Model saved as 'elevator_ppo_model'")
    
    if args.evaluate:
        model = PPO.load("elevator_ppo_model")
        evaluate_agent(model, args.episodes)
    
    if args.gui:
        run_gui()

if __name__ == "__main__":
    main()