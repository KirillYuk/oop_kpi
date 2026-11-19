import variant as V
from shapes import PointShape


class ShapeEditor:
    def __init__(self, canvas, on_full):
        self.canvas = canvas
        self.on_full = on_full
        self.shape_class = PointShape
        self.current = None
        self.pcshape: list = [None] * V.ARRAY_SIZE
        self.count = 0

        canvas.bind("<ButtonPress-1>", self.on_press)
        canvas.bind("<B1-Motion>", self.on_motion)
        canvas.bind("<ButtonRelease-1>", self.on_release)

    def on_press(self, event):
        if self.count >= V.ARRAY_SIZE:
            self.on_full()
            return
        self.current = self.shape_class(event.x, event.y)
        self.redraw()

    def on_motion(self, event):
        if self.current is None:
            return
        self.current.set_end(event.x, event.y)
        self.redraw()

    def on_release(self, event):
        if self.current is None:
            return
        self.current.set_end(event.x, event.y)
        self.pcshape[self.count] = self.current
        self.count += 1
        self.current = None
        self.redraw()

    def redraw(self):
        self.canvas.delete("all")
        for shape in self.pcshape[:self.count]:
            shape.draw(self.canvas)
        if self.current is not None:
            self.current.draw(self.canvas, rubber=True)
