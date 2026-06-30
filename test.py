import tkinter as tk

def show_value():
    # 3. Use the .get() method to read the value
    print("Checkbox Value:", male.get())
    print("Checkbox Value:", female.get())

root = tk.Tk()

# 1. Create a Tkinter variable to track the state
male = tk.BooleanVar()
female = tk.BooleanVar()


# 2. Link the variable to the Checkbutton using the 'variable' parameter
checkbox = tk.Checkbutton(root, text="Male", variable=male)
checkbox.pack()

checkbox = tk.Checkbutton(root, text="Female", variable=female)
checkbox.pack()

btn = tk.TkButton = tk.Button(root, text="Check Value", command=show_value)
btn.pack()

root.mainloop()
