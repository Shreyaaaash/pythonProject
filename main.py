import tkinter as tk
import time
import threading
import random


class TySpeedGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Typing Speed Calculator")
        self.root.geometry("800x600")
#this is the code that allows you to display caracters that are supposed to be typed on the test

        self.text = self.load_text_from_file('t.txt')

        self.frame = tk.Frame(self.root)

        # Initialize sample text
        self.current_text = random.choice(self.text)
        self.sample_label = tk.Label(self.frame, text=self.current_text, font=("Helvetica", 10))
        self.sample_label.grid(row=0, column=0, columnspan=2, padx=5, pady=10)
#yeh toh sabb font wont ka hai so that ke button ka sabb tujhe padding mile
        #padding and all toh HTML types hi hai
        self.input_entry = tk.Entry(self.frame, width=50, font=("Helvetica", 10))
        self.input_entry.grid(row=1, column=0, columnspan=2, padx=5, pady=10)
        self.input_entry.bind("<KeyPress>", self.start)

        self.speed_label = tk.Label(self.frame, text="Speed: \n0.00 CPS\n0.00 CPM", font=("Helvetica", 20))
        self.speed_label.grid(row=2, column=0, columnspan=2, padx=5, pady=10)

        self.reset_button = tk.Button(self.frame, text="Reset", command=self.reset)
        self.reset_button.grid(row=3, column=0, columnspan=2, padx=8, pady=10)
        self.frame.pack(expand=True)
#this allows you to stop the clock that you had once started when you started typing the thing

        self.counter = 0
        self.started = False
        self.running = False

        self.root.mainloop()

    def load_text_from_file(self, filename):
        try:
            with open(filename, 'r') as file:
                return file.read().split('\n')
        except FileNotFoundError:
            print(f"File not found: {filename}")
            return []
#this function below tells the timer to stop when ya stop typing
    def start(self, event):
        if not self.running:
            if not event.keycode in [16, 17, 18]:
                self.running = True
                t = threading.Thread(target=self.time_thread)
                t.start()
        if not self.current_text == self.input_entry.get():
            self.input_entry.config(fg="red")
        else:
            self.input_entry.config(fg="black")
        if self.input_entry.get() == self.current_text:
            self.running = False
            self.input_entry.config(fg="green")
#0.1 sirf voh delay time diya hai ke agar tu itne time ke bich mai koi charachter type karega then the timer keeps running
    def time_thread(self):
        while self.running:
            time.sleep(0.1)
            self.counter += 0.1
            cps = len(self.input_entry.get()) / self.counter
            cpm = cps * 60
            self.speed_label.config(text=f"Speed: \n{cps:.2f} CPS\n{cpm:.2f} CPM")

    def reset(self):
        self.input_entry.delete(0, tk.END)  # Clear the input field
        self.current_text = random.choice(self.text)  # order vise tera inputs display hoga
        self.sample_label.config(text=self.current_text)  # Update karega
        self.input_entry.config(fg="black")


TySpeedGUI()

#again edited by puWun
