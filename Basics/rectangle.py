from math import sqrt

def rectangle(perimeter:float, area:float):
    D = perimeter**2-16*area
    largest = (perimeter+sqrt(D))/4.0
    smallest = area/largest
    return round(largest) if largest.is_integer() and smallest.is_integer() else False

perimeter = int(input("Enter perimeter:"))
area = int(input("Enter area:"))
print(rectangle(perimeter,area))
