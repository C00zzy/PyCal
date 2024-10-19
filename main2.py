import tkinter as tk  # Import the tkinter library for GUI creation

# Create the root window
root_window = tk.Tk()
root_window.title("PyCal")  # Set the title of the window

# Define the function to handle button logic
def button_logic(button_text):
    if button_text == '=':  # If the '=' button is pressed
        try:
            # Evaluate the expression in entry1 and calculate the result
            result = eval(entry1.get())
            entry1.delete(0, tk.END)  # Clear the entry field
            entry1.insert(tk.END, str(result))  # Insert the result into the entry field
        except Exception:
            entry1.delete(0, tk.END)  # Clear the entry field on error
            entry1.insert(tk.END, "Error")  # Show "Error" in the entry field
    elif button_text == 'C':  # If the 'C' button is pressed
        entry1.delete(0, tk.END)  # Clear the entry field
    else:
        entry1.insert(tk.END, button_text)  # Append the pressed button's text to the entry field

# Create an entry widget for input
entry1 = tk.Entry(root_window, width=10, font=('Arial', 24))
entry1.grid(row=0, column=0, columnspan=3, padx=5, pady=5)  # Place the entry widget in the grid

# Define the labels for the buttons
button_labels = [
    ['7', '8', '9'],
    ['4', '5', '6'],
    ['1', '2', '3'],
    ['C', '0', '=']
]

# Create buttons for the calculator
for i, row in enumerate(button_labels):
    for j, label in enumerate(row):
        # Create a button and assign the button_logic function with the button's text
        button = tk.Button(root_window, text=label, width=5, height=2, 
                           command=lambda text=label: button_logic(text))
        button.grid(row=i + 1, column=j, padx=5, pady=5)  # Place the button in the grid

# Start the main event loop to run the application
root_window.mainloop()
