import math

a = input("Enter number a: ")
b = input("Enter number b: ")
c = input("Enter number c: ")

sqrt_number = int(b) ** 2 - 4 * int(a) * int(c)

output_1 = ((0 - int(b)) - ((int(sqrt_number) ** 0.5))) / (2 * int(a))
output_2 = ((0 - int(b)) + ((int(sqrt_number) ** 0.5))) / (2 * int(a))

print("Output 1: ", output_1)
print("Output 2: ", output_2)

