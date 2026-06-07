import tkinter as tk

def avg_cal():
    num1=float(entry1.get())
    num2=float(entry2.get())
    num3=float(entry3.get())
    result=(num1 + num2 + num3) / 3
    result_label.config(text=f"result is : {result}")

window=tk.Tk()
window.title("average cal")
window.geometry("400x400")

tk.Label(window,text="enter first number :").pack()
entry1=tk.Entry(window)
entry1.pack()

tk.Label(window,text="enter second number : ").pack()
entry2=tk.Entry(window)
entry2.pack()

tk.Label(window,text="enter third number : ").pack()
entry3=tk.Entry(window)
entry3.pack()

add_button=tk.Button(window,text="calculate",command=avg_cal)
add_button.pack(pady=10)

result_label=tk.Label(window,text="result : ")
result_label.pack()
window.mainloop()