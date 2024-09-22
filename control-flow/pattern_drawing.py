#!/bin/python3

pattern_size = int(input("Enter the size of the pattern: "))
row = 1

while row <= pattern_size:
    col = 1
    while col <= pattern_size:
        print("*", end = "")
        col += 1
    print()
    row += 1
