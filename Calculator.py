import tkinter as tk

def on_button_click(event):
    current_text = result_display.get()
    button_text = event.widget.cget("text")

    if button_text == "=":
        try:
            result = eval(current_text)
            result_display.set(result)
        except Exception as e:
            result_display.set("Error")
    elif button_text == "C":
        result_display.set("")
    else:
        result_display.set(current_text + button_text)

# Create the main application window
root = tk.Tk()
root.title("Calculator")

# Variable to store the display text
result_display = tk.StringVar()

# Frame to hold the display
display_frame = tk.Frame(root, bd=10, relief=tk.SUNKEN)
display_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

# Entry widget to display the result
result_entry = tk.Entry(display_frame, font=("Helvetica", 20), textvar=result_display, justify="right")
result_entry.pack(fill=tk.BOTH, expand=True)

# Frame to hold the buttons
button_frame = tk.Frame(root, bd=5, relief=tk.GROOVE)
button_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

# List of buttons
buttons = [
    ("7", "8", "9", "/"),
    ("4", "5", "6", "*"),
    ("1", "2", "3", "-"),
    ("C", "0", "=", "+")
]

# Create and place buttons in the button frame
for row_index, row in enumerate(buttons):
    for col_index, button_text in enumerate(row):
        button = tk.Button(button_frame, text=button_text, font=("Helvetica", 20), relief=tk.RIDGE)
        button.grid(row=row_index, column=col_index, sticky="nsew")
        button.bind("<Button-1>", on_button_click)

# Configure the grid weights for button frame
for i in range(4):
    button_frame.grid_rowconfigure(i, weight=1)
    button_frame.grid_columnconfigure(i, weight=1)

# Start the Tkinter main loop
root.mainloop()