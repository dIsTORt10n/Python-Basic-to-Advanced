import tkinter as tk
from tkinter import ttk


def calculate_weights():
    try:
        earth_weight = float(entry_weight.get())
        # Gravity relative to Earth (Earth = 1.0)
        planets = {
            "Mercury": 0.38, "Venus": 0.91, "The Moon": 0.166,
            "Mars": 0.38, "Jupiter": 2.34, "Saturn": 1.06,
            "Uranus": 0.92, "Neptune": 1.19
        }

        # Clear previous results
        for item in tree.get_children():
            tree.delete(item)

        # Add new calculations
        for planet, factor in planets.items():
            weight = round(earth_weight * factor, 2)
            tree.insert("", tk.END, values=(planet, f"{weight} kg"))

    except ValueError:
        pass  # Ignore non-numeric input


# Initialize Main Window
root = tk.Tk()
root.title("Space Weight Calculator")
root.geometry("400x450")

# Input Section
frame_top = tk.Frame(root, pady=20)
frame_top.pack()

tk.Label(frame_top, text="Enter Weight on Earth:", font=("Arial", 10)).pack()
entry_weight = tk.Entry(frame_top, font=("Arial", 12), justify='center')
entry_weight.pack(pady=5)
entry_weight.bind("<KeyRelease>", lambda e: calculate_weights())  # Auto-update

# Results Table
columns = ("Planet", "Weight")
tree = ttk.Treeview(root, columns=columns, show="headings", height=9)
tree.heading("Planet", text="Celestial Body")
tree.heading("Weight", text="Your Weight")
tree.column("Planet", anchor="center")
tree.column("Weight", anchor="center")
tree.pack(pady=10, padx=20, fill="both", expand=True)

root.mainloop()
