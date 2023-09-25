from tkinter import *
from PIL import Image, ImageTk
root = Tk()
root.title("TIME TABLE")
label=Label(text="JAYPEE UNIVERSITY OF \n INFORMATION TECHNOLOGY",font=("poppins",25,"bold"))
label.pack()
image = Image.open('C:\Users\Asus\Documents\GitHub\Timetable\juit1.png')
photo = ImageTk.PhotoImage(image)
image_label = Label(root, image=photo)
image_label.image = photo  # Keep a reference to the image to prevent it from being garbage collected
image_label.pack()
root.mainloop()


# import tkinter as tk
# from PIL import Image, ImageTk

# root = tk.Tk()
# root.title("TIME TABLE")

# label = tk.Label(text="JAYPEE UNIVERSITY OF\nINFORMATION TECHNOLOGY", font=("poppins", 25, "bold"))
# label.pack()

# # Load and display an image using PIL
# image = Image.open('C:/Users/Asus/Downloads/juit1.png')
# photo = ImageTk.PhotoImage(image)
# image_label = tk.Label(root, image=photo)
# image_label.image = photo  # Keep a reference to the image to prevent it from being garbage collected
# image_label.pack()

# root.mainloop()