# Task 18 - Creating an "Traffic Light Simulator" using tkinter in python program

import tkinter as tk
import time
import threading

class TrafficSimulator:
    def __init__(self, root):
        self.root = root
        self.root.title("🚦 Simple Traffic Light Simulation")
        self.root.configure(bg="#1e1e1e")
        self.root.geometry("1000x700")
        self.root.resizable(True, True)
        self.running = False
        self.lights = {}
        self.create_ui()
        self.root.bind("<Configure>", lambda e: self.draw_scene())

    def create_ui(self):
        top_frame = tk.Frame(self.root, bg="#1e1e1e")
        top_frame.pack(side="top", pady=10)
        title = tk.Label(top_frame, text="🚗 Traffic Light Simulation 🚦",
                         font=("Segoe UI", 18, "bold"), bg="#1e1e1e", fg="#00ffcc")
        title.pack()
        button_frame = tk.Frame(self.root, bg="#1e1e1e")
        button_frame.pack(pady=10)
        self.start_btn = tk.Button(button_frame, text="▶ Start", font=("Arial", 12, "bold"),
                                   bg="#00ff88", fg="black", width=10, command=self.start)
        self.start_btn.grid(row=0, column=0, padx=10)
        self.stop_btn = tk.Button(button_frame, text="⏸ Stop", font=("Arial", 12, "bold"),
                                  bg="#ff5555", fg="white", width=10, command=self.stop)
        self.stop_btn.grid(row=0, column=1, padx=10)
        self.status_label = tk.Label(self.root, text="Status: Idle", font=("Consolas", 12),
                                     fg="#ffffff", bg="#1e1e1e")
        self.status_label.pack()
        self.canvas = tk.Canvas(self.root, bg="#2b2b2b", highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

    def draw_scene(self):
        self.canvas.delete("all")
        w, h = self.canvas.winfo_width(), self.canvas.winfo_height()
        cx, cy = w // 2, h // 2
        road_w = 180

        self.canvas.create_rectangle(0, cy - road_w//2, w, cy + road_w//2, fill="#404040", outline="")
        self.canvas.create_rectangle(cx - road_w//2, 0, cx + road_w//2, h, fill="#404040", outline="")

        for i in range(0, w, 60):
            self.canvas.create_rectangle(i, cy - 3, i + 30, cy + 3, fill="white", outline="")
        for i in range(0, h, 60):
            self.canvas.create_rectangle(cx - 3, i, cx + 3, i + 30, fill="white", outline="")

        self.lights = {
            "North": self.create_light(cx - 100, cy - 220, "↓"),
            "South": self.create_light(cx + 100, cy + 220, "↑"),
            "East":  self.create_light(cx + 220, cy - 100, "←"),
            "West":  self.create_light(cx - 220, cy + 100, "→"),
        }

    def create_light(self, x, y, arrow):
        box = self.canvas.create_rectangle(x - 25, y - 65, x + 25, y + 65, fill="#111", outline="#00ffaa", width=2)
        r = self.canvas.create_oval(x - 15, y - 50, x + 15, y - 20, fill="gray")
        yel = self.canvas.create_oval(x - 15, y - 5, x + 15, y + 25, fill="gray")
        g = self.canvas.create_oval(x - 15, y + 40, x + 15, y + 70, fill="gray")
        self.canvas.create_text(x, y + 90, text=arrow, fill="#ffffff", font=("Arial", 16, "bold"))
        return {"red": r, "yellow": yel, "green": g}

    def start(self):
        if not self.running:
            self.running = True
            threading.Thread(target=self.run_cycle, daemon=True).start()
            self.status_label.config(text="Status: Running...")

    def stop(self):
        self.running = False
        self.status_label.config(text="Status: Stopped")

    def run_cycle(self):
        order = ["North", "South", "East", "West"]
        while self.running:
            for active in order:
                if not self.running:
                    break
                opposite = "South" if active == "North" else "North" if active == "South" else \
                           "West" if active == "East" else "East"
                self.switch_light(active, "green")
                self.switch_light(opposite, "green")
                for d in order:
                    if d not in (active, opposite):
                        self.switch_light(d, "red")
                self.update_ui(3)
                self.switch_light(active, "yellow")
                self.switch_light(opposite, "yellow")
                self.update_ui(1)
                self.switch_light(active, "red")
                self.switch_light(opposite, "red")
                self.update_ui(0.5)

    def switch_light(self, direction, color):
        for c in ["red", "yellow", "green"]:
            self.canvas.itemconfig(self.lights[direction][c], fill="gray")
        if color != "off":
            self.canvas.itemconfig(self.lights[direction][color], fill=color)

    def update_ui(self, seconds):
        for _ in range(int(seconds * 10)):
            time.sleep(0.1)
            if not self.running:
                break
            self.root.update_idletasks()
            self.root.update()

if __name__ == "__main__":
    root = tk.Tk()
    app = TrafficSimulator(root)
    root.mainloop()
