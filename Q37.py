''' Develop a Python GUI application using Tkinter to perform addition of two numbers entered 
by the user. Analyze how Tkinter handles events (like button clicks) to display the result in 
the window.'''

import tkinter as tk

def add_numbers():
  num1 = float(entry1.get())
  num2 = float(entry2.get())
  result = num1+num2
  result_label.config(text=f"result: {result}")
    

window = tk.Tk()
window.title("Addition of Two Numbers")
window.geometry("300x200")

tk.Label(window,text="enter first number :").pack()
entry1 = tk.Entry(window)
entry1.pack()

tk.Label(window,text="enter second number :").pack()
entry2 = tk.Entry(window)
entry2.pack()

add_button = tk.Button(window,text="add",command=add_numbers)
add_button.pack(pady=10)

result_label = tk.Label(window,text="result:")
result_label.pack()
window.mainloop()