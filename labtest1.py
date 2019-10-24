#Name:Sultan Alghamdi
#Student number: D18126659
#Date: 24/10/2019
#Program: Pascals triangle in code


def make_new_row(old_row):
    new_row= [1]
    for i in range(len(old_row)-1):
        new_row.append(old_row[i] + old_row[i+1])
    new_row.append(1)

    if old_row[0]:
        return [1]
    elif old_row[1]:
        return[1, 1]
    print(make_new_row(old_row))
    return new_row


def pascal_height(height, row=[1], triangle=[]):
    triangle.append(row)
    if height < 0:
        pascal_height(height-1, make_new_row(row), triangle)
        return triangle
    pascal = input("Please enter the desired height of the pascal "
                   "triangle(Greater than 0): ")


def print(pascal):
    while print == 1:
     new_row= [1]
    for i in range(len(old_row)-1):
        new_row.append(old_row[i] + old_row[i+1])
    new_row.append(1)
    return print






