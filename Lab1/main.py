import tkinter as tk

from module1 import show_work1_dialog
from module2 import show_work2_dialog


def on_work1():
    selected = show_work1_dialog(root)
    if selected is not None:
        result_var.set(f'Selected group: {selected}')

def on_work2():
    entered = show_work2_dialog(root)
    if entered is not None:
        result_var.set(f'Entered text: {entered}')

root = tk.Tk()
root.title('LAb1')
root.geometry('600x300')

menubar = tk.Menu(root)
menubar.add_command(label='Work1', command=on_work1)
menubar.add_command(label='Work2', command=on_work2)
root.config(menu=menubar)

result_var = tk.StringVar(value='')
result_label = tk.Label(
    root, textvariable=result_var, font=('Arial', 12),
    wraplength=450, justify='left',
)
result_label.pack(padx=20, pady=20, anchor='w')

root.mainloop()
