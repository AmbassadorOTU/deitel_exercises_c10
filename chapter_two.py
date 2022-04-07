# 2.1
x = 2; y = 3
print('x =', x)
print('Value of', x, '+', x, 'is', (x + x))
print('x =')
print((x + y), '=', (y + x))
print()

# 2.2
# rating = input('Enter an integer rating between 1 and 10 ')
# rating = int(rating)
# print(type(rating))
# print()

# 2.3
grade = 91
if grade >= 90:
    print('Congratulations! Your grade of', grade, 'earns you an A in this course.')
print()

# 2.4
print(27.5 + 2)
print(27.5 - 2)
print(27.5 * 2)
print(27.5 / 2)
print(27.5 // 2)
print(27.5 ** 2)
print()

# 2.5
radius = 2
pi = 3.14159
diameter = 2 * radius
circumference = 2 * pi * radius
area = pi * radius * radius
print(diameter, circumference, area)
print()

# 2.6
# n = int(input('Enter a digit: '))
# if n % 2 == 0:
#     print('Digit is even')
# else:
#     print('Digit is not even')
# print()

# 2.7
if 1024 % 4 == 0 and 10 % 2 == 0:
    print('1024 and 10 is a multiple of 4 and 2 respectively')
else:
    print('1024 and 10 is not a multiple of 4 and 2 respectively')
print()

# 2.8a
print('number\tsquare\tcube')
print(f'{0}\t\t{0**2}\t\t{0*0*0}')
print(f'{1}\t\t{1**2}\t\t{1*1*1}')
print(f'{2}\t\t{2**2}\t\t{2*2*2}')
print(f'{3}\t\t{3**2}\t\t{3*3*3}')
print(f'{4}\t\t{4**2}\t\t{4*4*4}')
print(f'{5}\t\t{5**2}\t\t{5*5*5}')
print()

# 2.9
print('A:',ord('A'))
print('B:',ord('B'))
print('C:',ord('C'))
print('b:',ord('b'))
print('c:',ord('c'))
print('d:',ord('d'))
print('0:',ord('0'))
print('1:',ord('1'))
print('2:',ord('2'))
print('$:',ord('$'))
print('*:',ord('*'))
print('+:',ord('+'))
print()

# 2.10
first_digit = int(input('Enter first digit: '))
second_digit = int(input('Enter second digit: '))
third_digit = int(input('Enter third digit: '))
sum = first_digit + second_digit + third_digit
average = (first_digit + second_digit + third_digit) / 3
product = first_digit * second_digit * third_digit
smallest = 0
largest = 0
print('Sum =', sum)
print('Average =', average)
print('Product =', product)
if smallest < first_digit:
    smallest = first_digit
if second_digit < smallest:
    smallest = second_digit
if third_digit < smallest:
    smallest = third_digit
print(smallest)
if first_digit > largest:
    largest = first_digit
if second_digit > largest:
    largest = second_digit
if third_digit > largest:
    largest = third_digit
print(largest)