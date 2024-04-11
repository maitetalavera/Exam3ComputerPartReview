import tkinter as tk

###############################################################################
# TODO: 1.
#
#   The todos in this module are in one comment because you will be modifying
#   the same bit of code each time. Here you will create a dialpad for a phone.
#
#   For this _todo_, you will create a window with the title "Phone" and call
#   its mainloop() method so it runs.
#
#   Once you have done this, then change the above _TODO_ to DONE.
#
#
# TODO: 2.
#
#   For this _todo_, you will create a label where the number will appear that
#   the user is dialing. This label's text should be empty initially.
#
#   Once you have done this, then change the above _TODO_ to DONE.
#
#
# TODO: 3.
#
#   For this _todo_, you will create all the buttons that the user needs:
#
#       - One for each digit 0-9
#       - A clear button
#       - A call button
#
#   They should be in the standard configuration for a dialpad (see the images
#   in the README file on GitHub). Each button is 50px by 50px.
#
#   HINT: I used a frame to surround the buttons and grid for this.
#
#   Once you have done this, then change the above _TODO_ to DONE.
#
#
# TODO: 4.
#
#   For this _todo_, using the command keyword on each button to have each
#   number button type that digit in the label above (just like you would if
#   you were dialing a number). Pressing each button should add that number to
#   end of the text in the label.
#
#   HINT: I found that the easiest way to accomplish this was to use a
#   different handler for each button.
#
#   You also need a handler for the clear and call buttons.
#
#   The clear button should simply empty the label text so there are no more
#   numbers in it.
#
#   The call button should check if the number is 10 digits. If it isn't, it
#   should print "Invalid Number. Call Failed." to the console. If it is 10
#   digits, it should print "Calling... <ENTERED PHONE NUMBER>" to the console.
#
#   Once you have done this, then change the above _TODO_ to DONE.
#
# TODO: 5.
#
#   For this _todo_, bind the window to any keypress so that if the user types
#   a number, it also types that number into the dialpad. Remember, you can use
#   isdigit() to check if the key pressed is a digit.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################


window=tk.Tk()
window.title("Phone")

lbl_number=tk.Label(master=window, text="")
lbl_number.pack()

frame_a=tk.Frame(master=window)
frame_a.rowconfigure([0,1,2,3], weight=1, minsize=50)
frame_a.columnconfigure([0,1,2], weight=1, minsize=50)
frame_a.pack()

def handler_1():
    lbl_number['text']=lbl_number['text']+"1"

def handler_2():
    lbl_number['text']=lbl_number['text']+"2"

def handler_3():
    lbl_number['text']=lbl_number['text']+"3"

def handler_4():
    lbl_number['text']=lbl_number['text']+"4"
def handler_clear():
    lbl_number['text'] = ""

def handler_call():
    if len(lbl_number["text"])==10:
        print(f"calling {lbl_number['text']}")
    else:
        print("invalid number ")


btn1= tk.Button(master=frame_a, text="1", comman=handler_1)


btn1.grid(row=0, column=0, stickey="nsew")
btn_clear.grid(row=3, column=0, stickey="nsew")
btn_call.grid()

def handle_keypress(event):
    if event.keysym.isdigit():
        lbl_number['text']=lbl_number['text']+event.keysym

window.bind("<Key>", handle_keypress)
window.mainloop()


