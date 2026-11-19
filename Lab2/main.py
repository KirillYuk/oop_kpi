import tkinter as tk
from tkinter import messagebox

import variant as V
from editor import ShapeEditor
from shapes import EllipseShape, LineShape, PointShape, RectShape

APP_NAME = "Lab2"
SHAPES = [
    ("Крапка", PointShape),
    ("Лінія", LineShape),
    ("Прямокутник", RectShape),
    ("Еліпс", EllipseShape),
]


class App:
    def __init__(self, root):
        self.root = root
        root.geometry("800x600")
        root.title(f"{APP_NAME} - {SHAPES[0][0]}")

        canvas = tk.Canvas(root, bg="white", highlightthickness=0)
        canvas.pack(fill="both", expand=True)
        self.editor = ShapeEditor(canvas, self.on_array_full)
        self.create_menu()

    def create_menu(self):
        menubar = tk.Menu(self.root, tearoff=0)

        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Вихід", command=self.root.destroy)
        menubar.add_cascade(label="Файл", menu=file_menu)

        objects_menu = tk.Menu(menubar, tearoff=0)
        for name, shape_class in SHAPES:
            objects_menu.add_command(
                label=name,
                command=lambda n=name, c=shape_class: self.select_type(n, c))
        menubar.add_cascade(label="Об'єкти", menu=objects_menu)

        help_menu = tk.Menu(menubar, tearoff=0)
        help_menu.add_command(label="Про програму", command=self.show_about)
        menubar.add_cascade(label="Довідка", menu=help_menu)

        self.root.config(menu=menubar)

    def select_type(self, name, shape_class):
        self.editor.shape_class = shape_class
        self.root.title(f"{APP_NAME} - {name}")

    def on_array_full(self):
        messagebox.showwarning(
            APP_NAME, f"Масив заповнено: максимум {V.ARRAY_SIZE} об'єктів.")

    def show_about(self):
        messagebox.showinfo(
            "Про програму",
            f"{APP_NAME} - графічний редактор об'єктів\n"
            f"Група ІМ-51, Ж = {V.ZH}")


def main():
    root = tk.Tk()
    App(root)
    root.mainloop()


if __name__ == "__main__":
    main()