from tkinter import Tk, Button, Frame, DISABLED, NORMAL, RAISED
from tkinter import messagebox
from subprocess import check_call, CalledProcessError, PIPE, Popen
from sys import argv
from threading import Thread


def start_app():
    try:
        if len(argv) == 2:
            new_proc([argv[1]])
        else:
            from config import APPLICATION
            if APPLICATION:
                new_proc(APPLICATION)
            else:
                messagebox.showerror('Ошибка', '''Не задано приложение для запуска.''')
    except CalledProcessError as err:
        messagebox.showerror('Error', 'Error: '+str(err))
    finally:
        pass


def start_thread(fn):
    def wrapper(app):
        c = Thread(target=fn, args=(app,))
        c.start()
    return wrapper


@start_thread
def new_proc(app):
    with Popen([app], stdout=PIPE) as proc:
        start_btn.configure(state=DISABLED)
        while True:
            if proc.poll() is not None:
                start_btn.configure(state=NORMAL)
                break


def logoff():
    try:
       check_call(['shutdown', '/l', '/f'])
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
