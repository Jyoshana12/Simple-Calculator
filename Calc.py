
import tkinter as tk
import math

def click(btn):
    global expression
    if btn == "=":
        try:
            result = str(eval(expression))
            expression_label.config(text=expression)
            result_label.config(text=result)
            expression = result
        except:
            expression_label.config(text="")
            result_label.config(text="Error")
            expression = ""
    elif btn == "C":
        expression = ""
        expression_label.config(text="")
        result_label.config(text="")
    elif btn == "⌫":  # Backspace
        expression = expression[:-1]
        result_label.config(text=expression)
    elif btn == "x²":
        try:
            result = str(float(expression) ** 2)
            expression_label.config(text=f"{expression}²")
            result_label.config(text=result)
            expression = result
        except:
            expression_label.config(text="")
            result_label.config(text="Error")
            expression = ""
    elif btn == "√":
        try:
            result = str(math.sqrt(float(expression)))
            expression_label.config(text=f"√({expression})")
            result_label.config(text=result)
            expression = result
        except:
            expression_label.config(text="")
            result_label.config(text="Error")
            expression = ""
    else:
        expression += str(btn)
        result_label.config(text=expression)

# Main window
window = tk.Tk()
window.title("Simple Calculator")
window.geometry("450x400")
window.resizable(False, False)

expression = ""

# Display Labels
expression_label = tk.Label(window, text="", anchor="e", font=("Arial", 14), 
                            bg="white", fg="grey", width=22, relief="sunken")
expression_label.grid(row=0, column=0, columnspan=4, pady=(8,0), padx=8)

result_label = tk.Label(window, text="", anchor="e", font=("Arial", 24, "bold"), 
                        bg="white", fg="black", width=22, relief="sunken")
result_label.grid(row=1, column=0, columnspan=4, pady=(0,12), padx=8)

# Corrected Button Layout
buttons = [
    ("x²",2,0), ("√",2,1), ("C",2,2), ("⌫",2,3),
    ("7",3,0), ("8",3,1), ("9",3,2), ("/",3,3),
    ("4",4,0), ("5",4,1), ("6",4,2), ("*",4,3),
    ("1",5,0), ("2",5,1), ("3",5,2), ("-",5,3),
    ("0",6,0), (".",6,1), ("+",6,2), ("=",6,3)
]

# Create Buttons
for (text, row, col) in buttons:
    btn = tk.Button(window, text=text, width=5, height=2, font=("Arial", 13),
                    command=lambda t=text: click(t))
    
    if text == "=":
        btn.grid(row=row, column=col, padx=2, pady=2, sticky="nswe")
    else:
        btn.grid(row=row, column=col, padx=2, pady=2)

window.mainloop()
