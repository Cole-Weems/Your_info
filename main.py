import tkinter as tk

root = tk.Tk(screenName="Ava", baseName="Ava", className="Ava", useTk=1)

label = tk.Label(root, text="Welcome to Ava, your local voice assistant")
label.pack()


label = tk.Label(root, text="You can use the below button to shutdown the assistant at any time")
label.pack()

button = tk.Button(root, text="Shutdown", width=25, command=root.destroy)
button.pack()


tk.Label(root, text="First Name").grid(row=0, column=0)
tk.Label(root, text="Last Name").grid(row=1, column=0)

entry1 = tk.Entry(root)
entry2 = tk.Entry(root)

entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)


root.mainloop()