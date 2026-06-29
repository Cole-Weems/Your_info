import tkinter as tk
from reportlab.pdfgen import canvas
from reportlab.lib import colors

def entry_field(identifier, label, width):
    entry = ((identifier) + "_entry")
    frame = ((identifier) + "_frame")



    frame = tk.Frame(root)
    frame.pack(fill="x", padx=10, pady=5)

    tk.Label(
        frame,
        text=str(label),
        width=width,
        anchor="w"
    ).pack(side="left")

    entry = tk.Entry(frame)
    entry.pack(side="left", fill="x", expand=True)




    return entry

def create_pdf(first, last, age, height, weight, country, eye_color):
    fileName = 'info.pdf'
    documentTitle = 'Result'

    pdf = canvas.Canvas(fileName)
    pdf.setTitle(documentTitle)
    pdf.setFont("Helvetica-Bold", 36)

    textLines = [
        str(("First name:" + first)),
        ("Last name:" + last),
        ("Age:" + age),
        ("Height" + height),
        ("Weight:" + weight),
        ("Country of residence:" + country),
        ("Eye color:" + eye_color)
    ]

    text = pdf.beginText(40, 680)
    text.setFont("Courier", 18)
    text.setFillColor(colors.red)

    for line in textLines:
        text.textLine(line)

    pdf.drawText(text)

    pdf.save()

root = tk.Tk()
root.title("Your Info")

label = tk.Label(root, text="A simple script to save your info to a pdf for printing")
label.pack()


first = entry_field("first", "First name:", 12)

last = entry_field("last", "Last name:", 12)

label = tk.Label(root, text="Sex:")
label.pack()

lb = tk.Listbox(root)
lb.insert(1, "Male")
lb.insert(2, "Female")

lb.pack()


height = entry_field("height", "Height:", 12)

weight = entry_field("weight", "Weight:", 12)

country = entry_field("country", "Country of residence:", 18)

age = entry_field("age", "Age:", 12)

eye_color = entry_field("eye", "Eye color:", 18)

label = tk.Label(root, text="You can use the below button to export to a pdf")
label.pack()

button = tk.Button(root, text="Export", width=25, command=create_pdf(first, last, age, height, weight, country, eye_color))
button.pack()

root.mainloop()