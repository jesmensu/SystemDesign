# Abstraction interface
class Shape:
    def __init__(self, drawing):
        self._drawing = drawing

    def draw(self):
        pass

# Refined abstraction
class Circle(Shape):
    def draw(self):
        print("Drawing Circle")
        self._drawing.draw_circle()

# Implementation interface
class Drawing:
    def draw_circle(self):
        pass

# Concrete implementation
class VectorDrawing(Drawing):
    def draw_circle(self):
        print("Drawing Circle in Vector")

# Concrete implementation
class RasterDrawing(Drawing):
    def draw_circle(self):
        print("Drawing Circle in Raster")

# Client code
vector_drawing = VectorDrawing()
raster_drawing = RasterDrawing()

circle_in_vector = Circle(vector_drawing)
circle_in_vector.draw()

circle_in_raster = Circle(raster_drawing)
circle_in_raster.draw()
