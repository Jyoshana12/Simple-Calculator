
import tkinter as tk

def click(button_text):
    current = entry.get()
    if button_text == "=":
        try:
            result = str(eval(current))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif button_text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, button_text)

# Create window
window = tk.Tk()
window.title("Simple Calculator")
window.geometry("350x400")
window.resizable(False, False)

# Entry field
entry = tk.Entry(window, width=20, font=("Arial", 18), bd=5, relief="ridge", justify="right")
entry.grid(row=0, column=0, columnspan=4, pady=10, padx=10)

# Buttons layout
buttons = [
    ("7",1,0), ("8",1,1), ("9",1,2), ("/",1,3),
    ("4",2,0), ("5",2,1), ("6",2,2), ("*",2,3),
    ("1",3,0), ("2",3,1), ("3",3,2), ("-",3,3),
    ("0",4,0), (".",4,1), ("=",4,2), ("+",4,3),
    ("C",5,0)
]

# Create buttons dynamically
for (text, row, col) in buttons:
    button = tk.Button(window, text=text, width=6, height=2, font=("Arial", 14),
                       command=lambda t=text: click(t))
    button.grid(row=row, column=col, padx=5, pady=5)

# Run application
window.mainloop()

