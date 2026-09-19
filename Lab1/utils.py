def center_window_over_parent(window, parent):
    window.update_idletasks()
    
    parent_x = parent.winfo_rootx()
    parent_y = parent.winfo_rooty()
    parent_w = parent.winfo_width()
    parent_h = parent.winfo_height()
    
    win_w = window.winfo_width()
    win_h = window.winfo_height()
    
    x = parent_x + (parent_w - win_w) // 2
    y = parent_y + (parent_h - win_h) // 2
    
    window.geometry(f'+{x}+{y}')
