class Rectangle:
    def __init__(self, w, h):
        self.width = w
        self.height = h
    def __repr__(self):
        return "Rectangle(width={}, height={})".format(self.width,self.height)
    def set_width(self, w):
        self.width = w
    def set_height(self, h):
        self.height = h
    def get_area(self):
        area = self.width*self.height
        return area
    def get_perimeter(self):
        perimeter = 2*(self.width) + 2*(self.height)
        return perimeter
    def get_diagonal(self):
        diagonal = (self.width**2 + self.height**2)**0.5
        return diagonal
    def get_picture(self):
        ## If the width or height is larger than 50, 
        ## this should return the string: "Too big for picture."
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        else:
            stars = "*"*self.width + "\n"
            stars *= self.height
            return stars
    def get_amount_inside(self, shape):
        ## Becareful of float
        num = self.get_area() // shape.get_area()
        return num
## Check subclass using issubclass(Square, Rectangle)
class Square(Rectangle):
    def __init__(self, s):
        self.side = s
        super().__init__(s, s)
    ### Correct the width and height
    ### Without these methods, width and height may not be the same value
    def set_width(self, w):
        self.set_side(w)
    def set_height(self, h):
        self.set_side(h)
    ################################
    def __repr__(self):
        return "Square(side={})".format(self.side)
    def set_side(self, s):
        self.side = s
        super().set_width(s)
        super().set_height(s)