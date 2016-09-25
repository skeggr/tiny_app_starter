from tkinter import Tk, Button, Frame
from tkinter import RAISED
from tkinter import messagebox
from subprocess import check_call, CalledProcessError
from sys import argv


def start_app():
    try:
        if len(argv) > 1:
            check_call([argv[1]])
        else:
            from config import APPLICATION
            check_call(APPLICATION)
    except CalledProcessError as err:
        messagebox.showerror('Error', 'Error: '+str(err))
    finally:
        pass


def logoff():
    try:
    #   check_call(['shutdown', '/l', '/f'])
        check_call(['calc'])
    except CalledProcessError as err:
        messagebox.showerror('Error', 'Error: '+str(err))


if __name__ == "__main__":
    gui = Tk()
    gui.overrideredirect(True)
    frame = Frame(gui, width=180, height=100, borderwidth=2, relief=RAISED)
    start_btn = Button(frame, text='Запуск приложения', command=start_app)
    logoff_btn = Button(frame, text='Выход из системы', command=logoff)
    frame.pack_propagate(False)
    frame.pack()
    start_btn.pack(pady=10)
    logoff_btn.pack()
    gui.mainloop()
