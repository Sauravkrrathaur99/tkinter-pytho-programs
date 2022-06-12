# The general syntax is:
# w=Button(master, option=value)
# master is the parameter used to represent the parent window.
# There are number of options which are used to change the format of the Buttons. Number of options can be passed as parameters separated by commas. Some of them are listed below.
#
# activebackground: to set the background color when button is under the cursor.
# activeforeground: to set the foreground color when button is under the cursor.
# bg: to set he normal background color.
# command: to call a function.
# font: to set the font on the button label.
# image: to set the image on the button.
# width: to set the width of the button.
# height: to set the height of the button.


import tkinter as tk
r = tk.Tk()
r.title('tkinter-Button')
button = tk.Button(r, text='Stop', width=50, command=r.destroy)
button.pack()
r.mainloop()
