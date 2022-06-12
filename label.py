# The general syntax is:
# w=Label(master, option=value)
# master is the parameter used to represent the parent window.
# There are number of options which are used to change the format of the widget. Number of options can be passed as parameters separated by commas. Some of them are listed below.
#
# bg: to set he normal background color.
# bg to set he normal background color.
# command: to call a function.
# font: to set the font on the button label.
# image: to set the image on the button.
# width: to set the width of the button.
# height” to set the height of the button.


from tkinter import *

root = Tk()
root.geometry("50x50")
w = Label(root, text='learning tkinter')
w.pack()
root.mainloop()
