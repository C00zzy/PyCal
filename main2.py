import tkinter as tk
# Created some code then just debugged with AI
# Create the root window
root_window = tk.Tk()
root_window.title("PyCal")

def button_logic(button_text):
    if button_text == '=':
        try:
            # Assuming you want to evaluate the expression in entry1
            result = eval(entry1.get())
            entry1.delete(0, tk.END)
            entry1.insert(tk.END, str(result))
        except Exception:
            entry1.delete(0, tk.END)
            entry1.insert(tk.END, "Error")
    elif button_text == 'C':
        entry1.delete(0, tk.END)
    else:
        entry1.insert(tk.END, button_text)

entry1 = tk.Entry(root_window, width=10, font=('Arial', 24))
entry1.grid(row=0, column=0, columnspan=3, padx=5, pady=5)

button_labels = [
    ['7', '8', '9'],
    ['4', '5', '6'],
    ['1', '2', '3'],
    ['C', '0', '=']
]

for i, row in enumerate(button_labels):
    for j, label in enumerate(row):
        button = tk.Button(root_window, text=label, width=5, height=2, command=lambda text=label: button_logic(text))
        button.grid(row=i + 1, column=j, padx=5, pady=5)

root_window.mainloop()
