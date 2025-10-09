# Task 17 - Arithmetic Operations Page using Tkinter
import tkinter as tk

def calculate(op):
    try:
        n1 = float(entry1.get())
        n2 = float(entry2.get())
        if op == '+':
            result.set(n1 + n2)
        elif op == '-':
            result.set(n1 - n2)
        elif op == '*':
            result.set(n1 * n2)
        elif op == '/':
            result.set(n1 / n2 if n2 != 0 else "Error: ÷0")
    except ValueError:
        result.set("Invalid Input")

root = tk.Tk()
root.title("Simple Calculator")
root.geometry("350x300")
root.configure(bg="#f0f8ff")  
tk.Label(root, text="Operations", font=("Comic Sans MS", 16, "bold"), bg="#f0f8ff", fg="#333").pack(pady=10)


tk.Label(root, text="Enter First Number:", bg="#f0f8ff", fg="#444").pack()
entry1 = tk.Entry(root, font=("Arial", 12))
entry1.pack(pady=5)

tk.Label(root, text="Enter Second Number:", bg="#f0f8ff", fg="#444").pack()
entry2 = tk.Entry(root, font=("Arial", 12))
entry2.pack(pady=5)

result = tk.StringVar()
tk.Label(root, text="Result:", bg="#f0f8ff", fg="#444").pack(pady=5)
tk.Label(root, textvariable=result, font=("Arial", 14, "bold"), bg="#f0f8ff", fg="green").pack(pady=5)

frame = tk.Frame(root, bg="#f0f8ff")
frame.pack(pady=10)

button_colors = ['#ff9999', '#99ff99', '#9999ff', '#ffcc99']  # Different colors for each operation
for i, symbol in enumerate(['+', '-', '*', '/']):
    tk.Button(frame, text=symbol, width=5, font=("Arial", 12, "bold"), 
              bg=button_colors[i], command=lambda s=symbol: calculate(s)).pack(side='left', padx=5)

tk.Button(root, text="Clear", font=("Arial", 12), bg="#ff6666", fg="white",
          command=lambda: [entry1.delete(0,'end'), entry2.delete(0,'end'), result.set('')]).pack(pady=10)

root.mainloop()