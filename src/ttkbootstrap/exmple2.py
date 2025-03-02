import tkinter
import ttkbootstrap

if __name__ == '__main__':
    root = tkinter.Tk()

    style = ttkbootstrap.Style(theme='darkly')
    root.title('Example 2 of ttkbootstrap GUI')
    root.geometry('200x100')

    button1 = ttkbootstrap.Button(root, text='Button 1', style='info')
    button1.pack()

    button2 = ttkbootstrap.Button(root, text='Button 2', style='success')
    button2.pack()

    button3 = ttkbootstrap.Button(root, text='Button 3', style='warning')
    button3.pack()

    root.mainloop()