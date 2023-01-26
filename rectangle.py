from polygon import Polygon

class Rectangle(Polygon):
    def getArea(self):
        return super().getArea()
    def getPerimeter(self):
        return super().getPerimeter()

rect =Rectangle(6, 7)

print(rect.getArea())
print(rect.getPerimeter())