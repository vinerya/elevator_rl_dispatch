import tkinter as tk
from elevator_env import ElevatorEnv
from stable_baselines3 import PPO

class ElevatorGUI:
    def __init__(self, master, env, model):
        self.master = master
        self.env = env
        self.model = model
        self.master.title("Elevator Dispatch System")

        self.canvas = tk.Canvas(self.master, width=400, height=600)
        self.canvas.pack()

        self.info_label = tk.Label(self.master, text="")
        self.info_label.pack()

        self.step_button = tk.Button(self.master, text="Step", command=self.step)
        self.step_button.pack()

        self.reset_button = tk.Button(self.master, text="Reset", command=self.reset)
        self.reset_button.pack()

        self.obs = self.env.reset()

    def draw_building(self):
        self.canvas.delete("all")
        floor_height = 550 / self.env.building.num_floors
        elevator_width = 30

        # Draw floors
        for i in range(self.env.building.num_floors):
            y = 550 - i * floor_height
            self.canvas.create_line(50, y, 350, y)
            self.canvas.create_text(30, y, text=str(i))

        # Draw elevators
        for i, elevator in enumerate(self.env.building.elevators):
            x = 100 + i * 100
            y = 550 - elevator.current_floor * floor_height
            self.canvas.create_rectangle(x, y - floor_height, x + elevator_width, y, fill="gray")
            self.canvas.create_text(x + elevator_width / 2, y - floor_height / 2, text=str(len(elevator.passengers)))

        # Draw waiting passengers
        for floor, passengers in self.env.building.waiting_passengers.items():
            y = 550 - floor * floor_height
            self.canvas.create_text(370, y - floor_height / 2, text=str(len(passengers)))

    def step(self):
        action, _ = self.model.predict(self.obs, deterministic=True)
        self.obs, reward, done, _ = self.env.step(action)
        self.draw_building()
        self.info_label.config(text=f"Reward: {reward:.2f}")

        if done:
            self.obs = self.env.reset()

    def reset(self):
        self.obs = self.env.reset()
        self.draw_building()
        self.info_label.config(text="Environment reset")

def run_gui():
    env = ElevatorEnv()
    model = PPO.load("elevator_ppo_model")

    root = tk.Tk()
    gui = ElevatorGUI(root, env, model)
    gui.draw_building()
    root.mainloop()

if __name__ == "__main__":
    run_gui()