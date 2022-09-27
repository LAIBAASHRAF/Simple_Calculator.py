num_1 = int(input("number:"))
char = str(input("operator:"))
num_2 = int(input("number:"))
if char == '+':
    sum = num_1 + num_2
    print(sum)
elif char == '-':
    diff = num_1 - num_2
    print(diff)
elif char == '*':
    product = num_1 * num_2
    print(product)
elif char == '/':
    quotient = num_1 / num_2
    print(quotient)
elif char == '%':
    rem = num_1 % num_2
    print(rem)