import math

class Vec2:
    def __init__(self, rec:tuple = (1,0), pol:tuple = (1,0)):
        if rec == pol == (1,0):
            self.x = 1;
            self.y = 0;

    @property
    def mag(self) -> float:
        return math.sqrt(self.x * self.x + self.y * self.y);

    @property:
    def arg(self) -> float:
        return math.atan(self.x / self.y);

    @property:
    def norm(self):
        mag:float = self.mag;
        return Vec2(self.x / mag, self.y / mag);

    

# class Vector:
#     def __init__(self, x: (float or int), y: (float or int)):
#         self.x, self.y = x, y

#     @property
#     def mag(self):
#         return math.sqrt(abs(self.x**2 + self.y**2))

#     @property
#     def angle(self):
#         a = math.atan2(self.y, self.x)
#         a += 2*math.pi if a < 0 else 0
#         return a

#     @property
#     def normal(self):
#         try:
#             return self * (1 / self.magnatude)
#         except ZeroDivisionError:
#             return self

#     @staticmethod
#     def to_radians(r):
#         return math.radians(r)

#     def cross(self, b):
#         return self.x * b.y - self.y * b.x

#     def dot(self, b):
#         return self.x * b.x + self.y * b.y

#     def rotate(self, r: (float or int)):
#         return self.__class__(math.cos(r), math.sin(r)) * self.x + self.__class__(-math.sin(r), math.cos(r)) * self.y

#     def __int__(self):
#         return self.__class__(int(self.x), int(self.y))

#     def __iter__(self):
#         yield self.x
#         yield self.y

#     def __abs__(self):
#         return self.__class__(abs(self.x), abs(self.y))

#     def __add__(self, other):
#         if type(other) in (float, int): return self.__class__(self.x + other, self.y + other)
#         if type(other) == self.__class__: return self.__class__(self.x + other.x, self.y + other.y)

#     def __sub__(self, other):
#         if type(other) in (float, int): return self.__class__(self.x - other, self.y - other)
#         if type(other) == self.__class__: return self.__class__(self.x - other.x, self.y - other.y)

#     def __mul__(self, other):
#         if type(other) in (float, int): return self.__class__(self.x * other, self.y * other)
#         if type(other) == self.__class__: return self.__class__(self.x * other.x, self.y * other.y)

#     def __eq__(self, other):
#         return True if self.x == other.x and self.y == other.y else False

#     def __getattr__(self, name):
#         if name in ('magnatude', 'mag'): return self.magnatude
#         if name in ('angle', 'r', 'rotation'): return self.angle
#         raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{name}'")

#     def __str__(self):
#         return f"{self.x} {self.y}"