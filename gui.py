import tkinter as tk
from tkinter import messagebox

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def calculate_factorial():
    try:
        num = int(entry.get())
        result = factorial(num)
        messagebox.showinfo("Result", f"Factorial of {num} is {result}")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid integer.")

root = tk.Tk()
root.title("Factorial Calculator")

tk.Label(root, text="Enter a number:").pack(pady=5)
entry = tk.Entry(root)
entry.pack(pady=5)

tk.Button(root, text="Calculate Factorial", command=calculate_factorial).pack(pady=10)

root.mainloop()
