import tkinter as tk

from utils import center_window_over_parent


def _on_ok(dialog, entry, result_holder):
    result_holder['value'] = entry.get()
    result_holder['accepted'] = True
    dialog.destroy()
    
def _on_cancel(dialog, result_holder):
    result_holder['accepted'] = False
    dialog.destroy()
    
def show_work2_dialog(parent):
    dialog = tk.Toplevel(parent)
    dialog.title('Work2 - Enter text')
    dialog.resizable(False, False)
    dialog.transient(parent)
    
    result_holder = {'accepted': False, 'value': None}
    
    entry = tk.Entry(dialog, width=35)
    entry.pack(padx=15, pady=15)
    entry.focus_set()
    
    buttons_frame = tk.Frame(dialog)
    buttons_frame.pack(pady=(0, 15))
    
    ok_button = tk.Button(
        buttons_frame, text='Yes', width=10,
        command=lambda: _on_ok(dialog, entry, result_holder),
        )
    ok_button.pack(side='left', padx=10)
    
    cancel_button = tk.Button(
        buttons_frame, text='Cancel', width=10,
        command=lambda: _on_cancel(dialog, result_holder),
    )
    cancel_button.pack(side='left', padx=10)
    
    dialog.protocol("WM_DELETE_WINDOW", lambda: _on_cancel(dialog, result_holder))
    
    center_window_over_parent(dialog, parent)
    
    dialog.grab_set()
    parent.wait_window(dialog)
    
    if result_holder['accepted']:
        return result_holder['value']
    return None
