import tkinter as tk
#from tkinter import ttk, LEFT, END
from PIL import Image, ImageTk



##############################################+=============================================================
root = tk.Tk()
root.configure(background="black")
# root.geometry("1300x700")


w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("Face Mask + Social Distancing Detection System")

# 43

# ++++++++++++++++++++++++++++++++++++++++++++
#####For background Image
# image2 = Image.open('crop5.jpg')
# image2 = image2.resize((w,h), Image.ANTIALIAS)

# background_image = ImageTk.PhotoImage(image2)

# background_label = tk.Label(root, image=background_image)

# background_label.image = background_image

# background_label.place(x=0, y=0)  # , relwidth=1, relheight=1)


#
lbl = tk.Label(root, text="Face mask detection and social distancing", font=('Elephant', 35,' bold '),bg="White",fg="Black")
lbl.place(x=150, y=10)




img=ImageTk.PhotoImage(Image.open("slide1.jpg"))

img2=ImageTk.PhotoImage(Image.open("slide2.jpg"))

img3=ImageTk.PhotoImage(Image.open("imges.png"))


logo_label=tk.Label()
logo_label.place(x=0,y=95)



# using recursion to slide to next image
x = 1

# function to change to next image
def move():
	global x
	if x == 4:
		x = 1
	if x == 1:
		logo_label.config(image=img,width=1800,height=700)
	elif x == 2:
		logo_label.config(image=img2,width=1800,height=700)
	elif x == 3:
		logo_label.config(image=img3,width=1800,height=700)
	x = x+1
	root.after(2000, move)

# calling the function
move()


frame_alpr = tk.LabelFrame(root, text="  ", width=600, height=100, bd=5, font=('times', 14, ' bold '),bg="#F0F8FF")
frame_alpr.grid(row=0, column=0)
frame_alpr.place(x=70, y=80)

frame_alpr = tk.LabelFrame(root, text="  ", width=700, height=300, bd=5, font=('times', 14, ' bold '),bg="#F0FFFF")
frame_alpr.grid(row=0, column=0)
frame_alpr.place(x=350, y=340)



lbl = tk.Label(frame_alpr, text='Social Distancing Only works ', font=('Lucida Calligraphy', 15,' bold '),bg="#F0FFFF",fg="black")
lbl.place(x=170, y=40)

lbl = tk.Label(frame_alpr, text="If We all Participate", font=('Lucida Calligraphy', 15,' bold '),bg="#F0FFFF",fg="black")
lbl.place(x=210, y=90)

lbl = tk.Label(frame_alpr, text="And Slowing down or Preventing ", font=('Lucida Calligraphy', 15,' bold '),bg="#F0FFFF",fg="black")
lbl.place(x=140, y=140)

lbl = tk.Label(frame_alpr, text=" The Spread of the virus", font=('Lucida Calligraphy', 15,' bold '),bg="#F0FFFF",fg="black")
lbl.place(x=190, y=190)

lbl = tk.Label(frame_alpr, text=' will save Lives !! ', font=('Lucida Calligraphy', 15,' bold '),bg="#F0FFFF",fg="black")
lbl.place(x=220, y=240)

#frame_alpr = tk.LabelFrame(root, text=" --Login & Register-- ", width=800, height=300, bd=5, font=('times', 14, ' bold '),bg="grey")
#frame_alpr.grid(row=0, column=0, sticky='nw')
#frame_alpr.place(x=400, y=400)


def log():
#T1.tag_configure("center", justify='center')
#T1.tag_add("center", 1.0, "end")

################################$%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

    from subprocess import call
    call(["python","login.py"])
    #root.destroy()
    
def reg():
    from subprocess import call
    call(["python","registration.py"])
    #root.destroy()
    
def window():
  root.destroy()
  


#####################################################################################################################

button1 = tk.Button( text="Login", command=log, width=15, height=1,font=('times', 15, ' bold '), bg="green", fg="white")
button1.place(x=70, y=100)

button2 = tk.Button( text="Registration",command=reg,width=15, height=1,font=('times', 15, ' bold '), bg="green", fg="white")
button2.place(x=260, y=100)

button3 = tk.Button( text="Exit",command=window,width=14, height=1,font=('times',15, ' bold '), bg="red", fg="white")
button3.place(x=450, y=100)





root.mainloop()