import tkinter as tk
# First draft
# Took some code from chatgpt and just added on top of it
# Let me commit

# Create the root window
root_window = tk.Tk()
root_window.title("Simple Calculator")
def insert_1():
    entry.insert(0, tk.END)
    entry.insert(0, 1) # type: ignore

def insert_2():
    entry.delete(0, tk.END)
    entry.insert(0, 2)

entry = tk.Entry(root_window, width=40)
entry.pack(padx=10, pady=10)

number1_button = tk.Button(root_window, text='1', command=insert_1)
number1_button.pack(padx=10, pady=20)

number2_button = tk.Button(root_window, text='2', command=insert_2)
number2_button.pack(padx=10, pady=20)

# Create entry widgets for two numbers

# Create a button to perform the addition

root_window.mainloop()

