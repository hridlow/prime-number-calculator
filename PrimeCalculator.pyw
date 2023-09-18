from tkinter import *
import itertools

root = Tk()
root.title("Prime Calculator")
root.resizable(False,False)

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan = 3, padx = 10, pady = 10)
e.state=DISABLED


# BUTTON OPERATIONS

def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def button_clear():
    e.delete(0, END)

def button_compute():
    m = int(e.get())
    print("Number:", m)
    t = 0
    y = 2
    z = m // 2
    if m == 1:
        t += 1

    for a in itertools.repeat(None, z):
        if m != y:
            if m % y == 0:
                t += 1
                break
            else:
                y += 1
                continue

    if t == 0:
        print("Prime")
        e.insert(m, " IS a prime number!")
    else:
        print("Not prime")
        e.insert(m, " IS NOT a prime number!")



# Define buttons

button_1 = Button(root, text="1", padx = 40, pady = 20, command =lambda : button_click(1))
button_2 = Button(root, text="2", padx = 40, pady = 20, command =lambda: button_click(2))
button_3 = Button(root, text="3", padx = 40, pady = 20, command =lambda: button_click(3))
button_4 = Button(root, text="4", padx = 40, pady = 20, command =lambda: button_click(4))
button_5 = Button(root, text="5", padx = 40, pady = 20, command =lambda: button_click(5))
button_6 = Button(root, text="6", padx = 40, pady = 20, command =lambda: button_click(6))
button_7 = Button(root, text="7", padx = 40, pady = 20, command =lambda: button_click(7))
button_8 = Button(root, text="8", padx = 40, pady = 20, command =lambda: button_click(8))
button_9 = Button(root, text="9", padx = 40, pady = 20, command =lambda: button_click(9))
button_0 = Button(root, text="0", padx = 40, pady = 20, command =lambda: button_click(0))
button_clear1 = Button(root, text="Clear", padx = 30, pady = 20, command =lambda: button_clear())
button_compute1 = Button(root, text="Compute", padx = 16, pady = 20, command =lambda: button_compute())

# Put buttons on screen

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=1)
button_clear1.grid(row=4, column = 0)
button_compute1.grid(row=4, column=2)

# run app
root.mainloop()