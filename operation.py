# Arithmatic Operations
a = 10
b =5
print("Addition:", a + b)        # Addition
print("Subtraction:", a - b)     # Subtraction
print("Multiplication:", a * b)  # Multiplication
print("Division:", a / b)        # Division
print("Modulus:", a % b)         # Modulus
print("Exponentiation:", a ** b) # Exponentiation
print("Floor Division:", a // b) # Floor Division

# Comparison Operations
print("Equal:", a == b)          # Equal
print("Not Equal:", a != b)      # Not Equal
print("Greater than:", a > b)    # Greater than
print("Less than:", a < b)       # Less than
print("Greater than or Equal:", a >= b) # Greater than or Equal
print("Less than or Equal:", a <= b)    # Less than or Equal

# Logical Operations
x = True
y = False
print("AND:", x and y)           # AND
print("OR:", x or y)             # OR
print("NOT x:", not x)           # NOT
print("NOT y:", not y)           # NOT
print("x AND (NOT y):", x and not y) # x AND (NOT y)
print("y OR (NOT x):", y or not x)   # y OR (NOT x)
print("(x AND y) OR (NOT x):", (x and y) or (not x)) # (x AND y) OR (NOT x)
print("(x OR y) AND (NOT y):", (x or y) and (not y)) # (x OR y) AND (NOT y)
print("x XOR y:", x ^ y)         # XOR
print("x NAND y:", not (x and y)) # NAND
print("x NOR y:", not (x or y))   # NOR
print("x XNOR y:", not (x ^ y))   # XNOR


# Assignment Operations
c = 10
c += 5  # c = c + 5
print("c after += 5:", c)
c -= 3  # c = c - 3
print("c after -= 3:", c)
c *= 2  # c = c * 2
print("c after *= 2:", c)
c /= 4  # c = c / 4
print("c after /= 4:", c)
c %= 3  # c = c % 3
print("c after %= 3:", c)
c **= 2 # c = c ** 2
print("c after **= 2:", c)
c //= 2 # c = c // 2
print("c after //= 2:", c)
