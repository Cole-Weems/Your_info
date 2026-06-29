import tkinter as tk


def entry_field(identifier, label, width):
    entry = ((identifier), "_entry")
    frame = ((identifier), "_frame")

    entry = tk.Entry(frame)
    entry.pack(side="left", fill="x", expand=True)

    frame = tk.Frame(root)
    frame.pack(fill="x", padx=10, pady=5)

    tk.Label(
        frame,
        text=label,
        width=width,
        anchor="w"
    ).pack(side="left")

    entry = tk.Entry(frame)
    entry.pack(side="left", fill="x", expand=True)

    return entry


root = tk.Tk()
root.title("Your Info")

label = tk.Label(root, text="A simple script to save your info to a pdf for printing")
label.pack()


label = tk.Label(root, text="You can use the below button to export to a pdf")
label.pack()

button = tk.Button(root, text="Export", width=25, command=root.destroy)
button.pack()


entry_field("first_name", "First name:", 12)

entry_field("last_name", "Last name:", 12)

label = tk.Label(root, text="Sex:")
label.pack()

lb = tk.Listbox(root)
lb.insert(1, "Male")
lb.insert(2, "Female")

lb.pack()


entry_field("height", "height:", 12)


entry_field("country", "Country of residence:", 18)

entry_field("age", "Age:", 12)

root.mainloop()