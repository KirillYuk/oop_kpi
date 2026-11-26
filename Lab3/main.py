import tkinter as tk
from tkinter import messagebox

import icons
import variant as V
from editor import ShapeEditor
from shapes import EllipseShape, LineShape, PointShape, RectShape
from tooltip import Tooltip

APP_NAME = "Lab3"
SHAPES = [
    ("Крапка", PointShape, icons.POINT),
    ("Лінія", LineShape, icons.LINE),
    ("Прямокутник", RectShape, icons.RECT),
    ("Еліпс", EllipseShape, icons.ELLIPSE),
]


class App:
    def __init__(self, root):
        self.root = root
        root.geometry("800x600")
        root.title(APP_NAME)

        self.type_var = tk.IntVar(value=0)
        self.icons = []

        self.create_toolbar()
        canvas = tk.Canvas(root, bg="white", highlightthickness=0)
        canvas.pack(fill="both", expand=True)
        self.editor = ShapeEditor(canvas, self.on_array_full)
        self.create_menu()

    def create_toolbar(self):
        toolbar = tk.Frame(self.root, relief="raised", borderwidth=1)
        toolbar.pack(side="top", fill="x")
        for index, (name, _shape_class, pattern) in enumerate(SHAPES):
            icon = icons.make_icon(pattern)
            self.icons.append(icon)
            button = tk.Radiobutton(
                toolbar,
                image=icon,
                indicatoron=False,
                variable=self.type_var,
                value=index,
                command=self.select_type,
            )
            button.pack(side="left", padx=2, pady=2)
            Tooltip(button, name)

    def create_menu(self):
        menubar = tk.Menu(self.root, tearoff=0)

        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Вихід", command=self.root.destroy)
        menubar.add_cascade(label="Файл", menu=file_menu)

        objects_menu = tk.Menu(menubar, tearoff=0)
        for index, (name, _shape_class, _pattern) in enumerate(SHAPES):
            objects_menu.add_radiobutton(
                label=name,
                variable=self.type_var,
                value=index,
                command=self.select_type,
            )
        menubar.add_cascade(label="Об'єкти", menu=objects_menu)

        help_menu = tk.Menu(menubar, tearoff=0)
        help_menu.add_command(label="Про програму", command=self.show_about)
        menubar.add_cascade(label="Довідка", menu=help_menu)

        self.root.config(menu=menubar)

    def select_type(self):
        self.editor.shape_class = SHAPES[self.type_var.get()][1]

    def on_array_full(self):
        messagebox.showwarning(
            APP_NAME, f"Масив заповнено: максимум {V.ARRAY_SIZE} об'єктів."
        )

    def show_about(self):
        messagebox.showinfo(
            "Про програму",
            f"{APP_NAME} - графічний редактор об'єктів\nГрупа ІМ-51, Ж = {V.ZH}",
        )


def main():
    root = tk.Tk()
    App(root)
    root.mainloop()


if __name__ == "__main__":
    main()
