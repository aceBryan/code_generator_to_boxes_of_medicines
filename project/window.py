from tkinter import *
from codegenerator import code_generator

BUTTON_WIDTH = 60
BUTTON_HEIGHT = 2

def click():
    result = code_generator()
    label["text"] = result

# Creating the main window
window = Tk()
window.geometry("640x480")
window.title("Medicine Box Code Generator")
window.resizable(width=False, height=False)
    
# Adding an icon to the window
window.iconbitmap("images/medicine2.ico")

# Adding my background image
background = PhotoImage(file=r"images/background.png")
label_image = Label(window, image=background)
label_image.place(relwidth=1, relheight=1)

# Creating a quit button
button1 = Button(window, text="Exit program", bg="light grey", command=window.quit)
button1.pack(side=BOTTOM)

# Creating the button to trigger the generation
button2 = Button(window, text="Generate code", bg="antique white", width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
result = button2.configure(command=click)
button2.pack(side=TOP)

# Creating a label to show the code
label = Label(window, bg="light gray", text="Your code here")
label.bind(button2)
label.pack(side=TOP, anchor=CENTER, pady=180)      

window.mainloop()
