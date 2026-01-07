"""a=int(input("enter the first number: "))
b=int(input("enter the second number: "))
print(f"the sum is {a+b}")
"""
#explicit casting
"""a=10
print(type(a))
print(float(a))
"""
#many values to multiple variables
"""a,b,z=10,13,44
print(f"a={a}")
print(f"b={b}")
print(f"z={z}")"""
# one value to many variables
"""x=y=c=20
print(f"x={x},y={y},z={z}") """


# Demonstrating Python Escape Sequences
"""
print("\' Single Quote Will Display")
print('\" Double Quote Will Display')
print('\\ Backslash Will Display')
print('\\\\ Two Backslash Will Display')
print('\n Used For New Line')
print('First Line\nSecond Line')
print('\t To Get Tab')
print('Column1\tColumn2')
print('\t\t To Get Two Tab')
print('Column1\t\tColumn2')
print('Backspace Example: ABC\bD')
print('Backspace Example: ABC\b\bD')
"""

"""
#operations on complex numbers
print("1. Addition")
print("2. Subtraction")
print("3. Division")
print("4. Multiplication")

# Taking user choice
choice = int(input("Enter your choice: "))

# Validating choice
if 1 <= choice <= 4:
    a = complex(input("Enter the first complex number: "))
    b = complex(input("Enter the second complex number: "))

    # Performing the chosen operation
    if choice == 1:
        print(f"Sum = {a + b}")
    elif choice == 2:
        print(f"Subtraction = {a - b}")
    elif choice == 3:
        print(f"Division = {a / b}")
    elif choice == 4:
        print(f"Multiplication = {a * b}")
else:
    print(f"The choice {choice} is not valid")
"""

"""#star programs
print("* "*20 + "\n"+ "* "*20+"\n"+ "* "*20+"\n"+ "* "*20)
print("\n")
print("\n")
print("* \n" + "* "*2 + "\n" + "* "*3 + "\n" + "* "*4)
print("\n")
print("\n")



print("* "*20+"\n* \t \t \t \t \t\t\t\t\t  *"+"\n"+"* "*20)
"""
"""
a='good dad and poor dad'
print(a[::-1])
print(a[0:2]+a[-2:])
print(a.replace(a[0],'$'))
print(a.replace('good','rich'))
print(a.upper())
print(a.capitalize())
print(a.title())
"""

"""
a = 5
b = 3
and_result = a & b
or_result = a | b

print(f"AND operation: {a} & {b} = {and_result}")
print(f"OR operation: {a} | {b} = {or_result}")
"""
"""
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(5))
"""
def bin_search(arr,low, high, n):
    mid = (low + high) // 2
    if n == arr[mid]:
        return mid
    elif n < mid:
        return bin_search(arr,low, mid-1, n)
    else:
        return bin_search(arr,mid+1, n, high)

print(bin_search([10,11,33,222,32,3,5,66,21],5, 10, 5))