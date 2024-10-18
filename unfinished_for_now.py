import tkinter as tk

from requests import delete
# First draft
# Took some code from chatgpt and just added on top of it
# Let me commit

# Create the root window
root_window = tk.Tk()
root_window.title("Simple Calculator")


def button_logic(button_labels):
    if button_text == '=':
        try:
            result = eval(entry1.get() entry2.get())
            entry1.delete(0, tk.END)
            entry1.insert(tk.END, str(result))
        except Exception as e:
            entry1.delete(0, TK.END)
            entry1.insert(tk.END, "Error")
        elif button_labels == 'C':
            entry1.delete(0, TK.END)
            entry2.delete(0, tk.END)
        else:
            entry2.insert(tk.END, button_labels)


entry1 = tk.entry1(root_window, width=10, font=('Arial', 24))
entry1.grid = (row=0, column=0, columnspan=3, padx=5, pady=5)

entry2 = tk.entry2(root_window, width=16, font=('Arial', 24))
entry2.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

rows = 3
cols = 3

button_labels = [
    ['7', '8', '9'],
    ['4', '5', '6'],
    ['1', '2', '3'],
    ['C', '0', '=']
]


for i, row in enumerate(button_labels):
    for j, label in enumerate(row):
        button = tk.button(root_window, text=label, width=5, height=2, command=lambda text=label: button_logic(button_labels))
        button.grid(row=i + 2, column=j, padx=5, pady=5)

# Create a button to perform the addition

root_window.mainloop()

