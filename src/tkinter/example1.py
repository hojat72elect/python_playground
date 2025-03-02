import tkinter

if __name__ == '__main__':
    root = tkinter.Tk()
    root.title("Example 1 of tkinter GUI")
    root.geometry("200x100")

    button1 = tkinter.Button(root, text="Button 1")
    button1.pack()

    button2 = tkinter.Button(root, text="Button 2")
    button2.pack()

    button3 = tkinter.Button(root, text="Button 3")
    button3.pack()

    root.mainloop()
