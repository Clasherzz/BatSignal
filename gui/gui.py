import tkinter as tk
from tkinter import messagebox
import threading


import winsound
import time


from services.config import load_config, save_config
from services.battery_checker import monitor_battery
def launch_gui():
    config = load_config()
    def update_repeat():
        """Update the config dictionary when the radio button is selected"""
        config["repeat"] = repeat_var.get()
        print("Repeat value updated to:", config["repeat"])
    def start_monitor():
        try:
            low = int(low_entry.get())
            high = int(high_entry.get())
            duration = int(duration_entry.get())

            if not (0 < low < 100 and 0 < high <= 100 and low < high):
                raise ValueError

            config = {
                "low_threshold": low,
                "high_threshold": high,
                "beep_duration": duration,
                "repeat": repeat_var.get()
            }
            save_config(config)
            messagebox.showinfo("Saved", "Settings saved! Monitoring started.")
            threading.Thread(target=monitor_battery, args=(config,), daemon=True).start()

        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter valid numeric values.")

    root = tk.Tk()
    root.title("Battery Alert Settings")

    tk.Label(root, text="Low Battery Threshold (%)").grid(row=0, column=0)
    low_entry = tk.Entry(root)
    low_entry.insert(0, config["low_threshold"])
    low_entry.grid(row=0, column=1)

    tk.Label(root, text="High Battery Threshold (%)").grid(row=1, column=0)
    high_entry = tk.Entry(root)
    high_entry.insert(0, config["high_threshold"])
    high_entry.grid(row=1, column=1)

    tk.Label(root, text="Beep Duration (ms)").grid(row=2, column=0)
    duration_entry = tk.Entry(root)
    duration_entry.insert(0, config["beep_duration"])
    duration_entry.grid(row=2, column=1)

    tk.Label(root, text="Repeatation of alert sound").grid(row=3, column=0)
#    repeat_var = tk.IntVar(value=config["repeat"])  # Set initial value from config
    repeat_var = tk.StringVar(value=config["repeat"])  # Set initial value from config
    # Radiobuttons for "Yes" and "No"
    tk.Radiobutton(root, text="Yes", variable=repeat_var, value="Yes", command=update_repeat).grid(row=3, column=1)
    tk.Radiobutton(root, text="No", variable=repeat_var, value="No", command=update_repeat).grid(row=3, column=2)
# Radiobuttons for "Yes" and "No"
    tk.Radiobutton(root, text="Yes", variable=repeat_var, value="Yes", command=update_repeat).grid(row=3, column=1)
    tk.Radiobutton(root, text="No", variable=repeat_var, value="No", command=update_repeat).grid(row=3, column=2)

    start_btn = tk.Button(root, text="Start Monitoring", command=start_monitor)
    start_btn.grid(row=4, column=0, columnspan=2, pady=10)

    root.mainloop()


if __name__ == "__main__":
    launch_gui()