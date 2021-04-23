import math

def RectangleArea(_length, _width):
    _area = _length * _width
    return _area    
def CircleArea(_radius):
    _area = _radius * _radius * math.pi
    return _area

def SquareArea(_side):
    _area = _side * _side
    return _area

def TriangleArea(_base, _height):
    _area = _base * _height /2
    return _area
