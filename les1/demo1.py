import tkinter as tk

window = tk.Tk()
window.title('demo')
window.geometry('300x400')

var = tk.StringVar()
var.set('who am i')
l = tk.Label(window, textvariable=var, bg='pink', font=('Arial', 12), width=30, height=2)
l.pack()
on_hit = False


def hit_me():
    global on_hit
    if not on_hit:
        on_hit = True
        var.set('nation')
    else:
        on_hit = False
        var.set('')


b = tk.Button(window, text='hit me', width=15, height=2, command=hit_me)
b.pack()

aLabel = tk.Label(window, text="A Label", font=("Arial", 12))
aLabel.pack()


def clickMe():
    global action
    action.configure(text="clicked")
    aLabel.configure(foreground='red')


action = tk.Button(window, text='Hit me', command=clickMe)
action.pack()

window.mainloop()
