# factorial exercise
number = int(input('Enter number: '))
n = 10
i = 1
while i < 10:
    number *= i
    n *= i
    i += 1
print('Factorial of number =', number)
print(n)

# fibonacci exercise
a = 0
b = 1
i = 0
while i <= 3:
    fibonacci_sum = a + b
    a = b
    b = fibonacci_sum
    i += 1
print(fibonacci_sum)