# The general syntax is:
# w = Listbox(master, option=value)
# master is the parameter used to represent the parent window.
# There are number of options which are used to change the format of the widget. Number of options can be passed as parameters separated by commas. Some of them are listed below.
#
# highlightcolor: To set the color of the focus highlight when widget has to be focused.
# bg: to set he normal background color.
# bd: to set the border width in pixels.
# font: to set the font on the button label.
# image: to set the image on the widget.
# width: to set the width of the widget.
# height: to set the height of the widget.


from tkinter import *

top = Tk()
Lb = Listbox(top)
Lb.insert(1, 'ABES ENFINEERING COLLEGE')
Lb.insert(2, 'AJAY KUMAR GARG')
Lb.insert(3, 'KRISHNA INSTITUTE OF EC')
Lb.insert(4, 'JSS ACADEMY')
Lb.pack()
top.mainloop()
