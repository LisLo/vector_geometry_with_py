import math


class MyMethods():
    def add(a, b):
        result = (a[0] + b[0], a[1] + b[1], a[2] + b[2])
        return result

    def sub(a, b):
        result = (a[0] - b[0], a[1] - b[1], a[2] - b[2])
        return result

    def multiply(c, a):
        result = (c * a[0], c * a[1], c * a[2])
        return result

    def norm(a):
        result = math.sqrt((a[0] * a[0] + a[1] * a[1] + a[2] * a[2]))
        return result
    
    def dotp(a, b):
        result = (a[0] * b[0] + a[1] * a[1] + b[2] * b[2])
        return result

    def crossp(a, b):
        result = (a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0])
        return result
