import tkinter as tk
from datetime import datetime
def calculate_age():
    name = entry_name.get()
    bday = int(entry_bday.get())

    current_year = datetime.now().year
    age = current_year - bday
    result_label.config(text=f"Hi {name}!, your presest age is {age} years old.")

window = tk.Tk()
window.title("Age Calculator")

label_name = tk.Label(window, text="Name:")
label_name.pack()

entry_name = tk.Entry(window)
entry_name.pack()

label_bday = tk.Label(window, text="Bday Year:")
label_bday.pack()

entry_bday = tk.Entry(window)
entry_bday.pack()

calculate_button = tk.Button(window, text="Calculate Age", command=calculate_age)
calculate_button.pack()

result_label = tk.Label(window, text="")
result_label.pack()
window.mainloop()