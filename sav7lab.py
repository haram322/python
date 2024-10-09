import math
def triangle_area(base, height):
    return 0.5 * base * height
def circle_area(radius):
    return math.pi * radius ** 2
def rectangle_area(lenght, width):
    return lenght * width
def main():
    shape = input("Введите фигуру( треугольник, круг, прямоугольник): ").lower()
    if shape == "треугольник":
        base = float(input("Введите основание треугольника: "))
        height = float(input("Введите высоту треугольника: "))
        area = triangle_area(base, height)
        print(f"Площадь треугольника: {area}")
    elif shape == "круг":
        radius = float(input("Введите радиус круга: "))
        area = circle_area(radius)
        print(f"Площадь круга: {area} ")
    elif shape == "прямоугольник":
        length = float(input("Введите длину прямоугольника: "))
        width = float(input("Введите ширину прямоугольника: "))
        area = rectangle_area(length, width)
        print(f"Площадь прямоугольника: {area}")  
    else:
        print("Введена неверная фигура")
if __name__ == "__main__": main()