from tkinter import *

def click(event):
    global value

    text = event.widget.cget("text")
    
    if text == "=":
        if value.get().isdigit():
            newvalue = int(value.get())

        else:
            try:
                newvalue = eval(screen.get())
            except Exception as e:
                value.set("Invalid")

        value.set(newvalue)
        screen.update()

    elif text == "C":
        value.set("")
        screen.update()

    elif text == "EXIT":
        root.destroy()
        quit()

    else:
        value.set(value.get() + text)
        screen.update()

root = Tk()
root.geometry("350x500")
root.minsize(width=350, height=500)
root.title("Calclator")


value = StringVar()
value.set("")
screen = Entry(root, textvariable=value, font="lucida 18 bold", bg="Lightgrey", borderwidth=10, relief=RIDGE)
screen.pack(padx=10,pady=10, fill="x",ipady=10)

f = Frame(root, bg="grey",padx=15, pady=10)
b = Button(f, text="EXIT", padx=25, pady=5, font="lucida 19 bold", bg="lightgreen", border=2)
b.pack(side=LEFT,padx=10)
b.bind("<Button-1>", click)
b = Button(f, text="C", padx=43, pady=5, font="lucida 19 bold", bg="lightblue")
b.pack(side=LEFT,padx=10)
b.bind("<Button-1>", click)
f.pack(fill="x",padx=10)

f = Frame(root, bg="grey",padx=15, pady=10)
b = Button(f, text="7", padx=10, pady=4, font="lucida 19 bold")
b.pack(side=LEFT,padx=10)
b.bind("<Button-1>", click)
b = Button(f, text="8", padx=10, pady=4, font="lucida 19 bold")
b.pack(side=LEFT,padx=10)
b.bind("<Button-1>", click)
b = Button(f, text="9", padx=10, pady=4, font="lucida 19 bold")
b.pack(side=LEFT,padx=10)
b.bind("<Button-1>", click)
b = Button(f, text="/", padx=10, pady=4, font="lucida 19 bold")
b.pack(side=LEFT,padx=10)
b.bind("<Button-1>", click)
f.pack(fill="x",padx=10)

f = Frame(root, bg="grey",padx=15, pady=10)
b = Button(f, text="4", padx=10, pady=4, font="lucida 19 bold")
b.pack(side=LEFT,padx=10)
b.bind("<Button-1>", click)
b = Button(f, text="5", padx=10, pady=4, font="lucida 19 bold")
b.pack(side=LEFT,padx=10)
b.bind("<Button-1>", click)
b = Button(f, text="6", padx=10, pady=4, font="lucida 19 bold")
b.pack(side=LEFT,padx=10)
b.bind("<Button-1>", click)
b = Button(f, text="*", padx=9, pady=4, font="lucida 19 bold")
b.pack(side=LEFT,padx=10)
b.bind("<Button-1>", click)
f.pack(fill="x",padx=10)

f = Frame(root, bg="grey",padx=15, pady=10)
b = Button(f, text="1", padx=10, pady=4, font="lucida 19 bold")
b.pack(side=LEFT,padx=10)
b.bind("<Button-1>", click)
b = Button(f, text="2", padx=10, pady=4, font="lucida 19 bold")
b.pack(side=LEFT,padx=10)
b.bind("<Button-1>", click)
b = Button(f, text="3", padx=10, pady=4, font="lucida 19 bold")
b.pack(side=LEFT,padx=10)
b.bind("<Button-1>", click)
b = Button(f, text="-", padx=10, pady=4, font="lucida 19 bold")
b.pack(side=LEFT,padx=10)
b.bind("<Button-1>", click)
f.pack(fill="x",padx=10)

f = Frame(root, bg="grey",padx=15, pady=10)
b = Button(f, text="0", padx=10, pady=4, font="lucida 19 bold")
b.pack(side=LEFT,padx=10)
b.bind("<Button-1>", click)
b = Button(f, text="+", padx=10, pady=4, font="lucida 19 bold")
b.pack(side=LEFT,padx=10)
b.bind("<Button-1>", click)
b = Button(f, text="=", padx=43, pady=4, font="lucida 19 bold", bg="yellow")
b.pack(side=LEFT,padx=10)
b.bind("<Button-1>", click)
f.pack(fill="x",padx=10)

root.mainloop()
