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

def create_pdf(first, last, age, height, weight, country, eye_color, male, female):
    status_label.config(text="Generating")
    root.update_idletasks()

    fileName = 'info.pdf'
    documentTitle = 'Result'

    if male == False and female == True:
        sex_v = "Sex: Female"
    elif male == True and female == False:
        sex_v = "Sex: Male"
    else:
        sex_v = None


    pdf = canvas.Canvas(fileName)
    pdf.setTitle(documentTitle)
    pdf.setFont("Helvetica-Bold", 36)
    pdf.setFillColorRGB(0, 0, 0)

    # The added "_v" differentiates between the variables passed into the function and the new variables created within the function
    first_v = str(("First name: " + first))
    last_v = str(("Last name: " + last))
    age_v = str(("Age: " + age))
    height_v = str(("Height (in): " + height))
    weight_v = str(("Weight (lbs): " + weight))
    country_v = str(("Country of residence: " + country))
    eye_color_v = str(("Eye color: " + eye_color))


    textLines = [
        first_v,
        last_v,
        age_v,
        height_v,
        weight_v,
        country_v,
        eye_color_v,
        sex_v,
    ]

    text = pdf.beginText(40, 680)
    text.setFont("Courier", 18)
    text.setFillColor(colors.red)

    for line in textLines:
        text.textLine(line)

    pdf.drawText(text)

    # for debug
    # print("Generating")

    pdf.save()
    status_label.config(text="Generation complete")
    root.update_idletasks()

root = tk.Tk()
root.title("Your Info")

label = tk.Label(root, text="A simple script to save your info to a pdf for printing")
label.pack()


first = entry_field("first", "First name:", 12)

last = entry_field("last", "Last name:", 12)

label = tk.Label(root, text="Sex:")
label.pack()

male = tk.BooleanVar()
female = tk.BooleanVar()


# 2. Link the variable to the Checkbutton using the 'variable' parameter
checkbox = tk.Checkbutton(root, text="Male", variable=male)
checkbox.pack()

checkbox = tk.Checkbutton(root, text="Female", variable=female)
checkbox.pack()



height = entry_field("height", "Height (in):", 12)

weight = entry_field("weight", "Weight (lbs):", 12)

country = entry_field("country", "Country of residence:", 18)

age = entry_field("age", "Age:", 12)

eye_color = entry_field("eye", "Eye color:", 18)

label = tk.Label(root, text="You can use the below button to export to a pdf")
label.pack()

label = tk.Label(root, text="Status:")
label.pack()

status = "Generation on standby"
status_label = tk.Label(root, text=status)
status_label.pack()

button = tk.Button(root, text="Export", width=25, command=lambda: create_pdf(
        first.get(),
        last.get(),
        age.get(),
        height.get(),
        weight.get(),
        country.get(),
        eye_color.get(),
        male.get(),
        female.get()
))
button.pack()



root.mainloop()