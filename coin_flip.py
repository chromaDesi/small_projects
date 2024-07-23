import tkinter as tk
import random

def result() -> None:
    x = random.randint(1,10)
    if x % 2 == 0:
        label["text"] = f"Heads"
        label["bg"] = "Pink"
    else:
        label["text"] = "Tails"
        label["bg"] = "Light Blue"


window = tk.Tk()
window.title("Coin Flip by Varun")
window.configure(bg="Black")
label = tk.Label(text="Result", )
button = tk.Button(text="Flip", width = 7, height = 3, command=result, bg="Beige")        
label.pack()
button.pack()

window.mainloop()
