import tkinter as tk
# First draft
# Took some code from chatgpt and just added on top of it
# Let me commit

# Create the root window
root = tk.Tk()
root.title("Simple Calculator")



def create_result_window(result):
    new_window = tk.Toplevel(root)
    new_window.title("Result")
    new_window.geometry("100x50")
    result_label = tk.Label(new_window, text="Result:" + str(result))
    result_label.pack(pady=10)

# Function to perform addition
def add_numbers():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    result = num1 + num2
    create_result_window(result)

# Create entry widgets for two numbers
entry1 = tk.Entry(root)
entry1.pack(pady=2)

entry2 = tk.Entry(root)
entry2.pack(pady=2)

# Create a button to perform the addition
add_button = tk.Button(root, text="Add", command=add_numbers)
add_button.pack(pady=10)


 


# Create a label to display the result



# Start the Tkinter event loop
root.mainloop()

