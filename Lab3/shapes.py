from abc import ABC, abstractmethod

import variant as V


class Shape(ABC):
    def __init__(self, x, y):
        self.x1 = self.x2 = x
        self.y1 = self.y2 = y

    def set_end(self, x, y):
        self.x2, self.y2 = x, y

    @abstractmethod
    def draw(self, canvas, rubber=False):
        pass

    @staticmethod
    def _color(rubber):
        return V.RUBBER_COLOR if rubber else "black"


class PointShape(Shape):
    def draw(self, canvas, rubber=False):
        color = self._color(rubber)
        canvas.create_oval(
            self.x2 - 2,
            self.y2 - 2,
            self.x2 + 2,
            self.y2 + 2,
            fill=color,
            outline=color,
        )


class LineShape(Shape):
    def draw(self, canvas, rubber=False):
        canvas.create_line(self.x1, self.y1, self.x2, self.y2, fill=self._color(rubber))


class RectShape(Shape):
    def draw(self, canvas, rubber=False):
        canvas.create_rectangle(
            self.x1,
            self.y1,
            self.x2,
            self.y2,
            outline=self._color(rubber),
            fill="" if rubber else V.RECT_FILL,
        )


class EllipseShape(Shape):
    def draw(self, canvas, rubber=False):
        canvas.create_oval(
            2 * self.x1 - self.x2,
            2 * self.y1 - self.y2,
            self.x2,
            self.y2,
            outline=self._color(rubber),
        )
