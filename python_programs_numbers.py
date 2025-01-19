import math

"""
Handle Precision Value 
Input - Number/Decimal/Floating Input and decimal plances
Output - Value with percision
"""
def return_percision_value(num = 0, precision_upto = 1):
    return f"""Percision value for {num} is: {round(num, precision_upto)}"""
print(return_percision_value(1234.1234567, 5))
print("\n")

"""
Reverse a Number
Input: 12345
Output: 54321
"""
def reverse_a_num(num = 0):
    # ''.join(list(reversed(str(num))))
    reverse_num = 0
    while num != 0:
        reverse_num = (reverse_num * 10) + (num % 10)        
        num = num // 10
    return f"Reverse Number for {num} is: {reverse_num} "
print(reverse_a_num(1234))
print("\n")


"""
Armstrong Number - A number when splitted and added again as num^3 will result in same number
Input: 153 
Output: 153
"""
def is_armstrong_number(num = 0):
    num = str(num)
    num_len = len(num)
    arm_number = sum(int(digit)** num_len for digit in num )
    if arm_number != int(num):
        return f"{num} is not an armstrong number"
    return f"{num} is an armstrong number"
print(is_armstrong_number(150))
print("\n")

"""
Prime Number - A number which is divisible only by itself
Input: 1, 2, 3, 8, 10, 13 
Ouput: {num} is a prime number/Not a Prime Number
"""
def is_prime_number(num):
    if (num <= 1) or (num % 2 == 0):
        return f"{num} is not a Prime Number"
    if num == 2:
        return f"{num} is a Prime Number"
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return f"{num} is not a Prime Number"
    return f"{num} is a Prime Number"
print(is_prime_number(29))
print("\n")

"""
Fibonacci Series - A series of number which when added to its previous number result in the next number
Input: 0, 1
Output: 0, 1, 1, 2, 3, 5, 8, 13, 21, .........
"""
def is_fibonacci_series(num):
    # [0, 1, 1, 2, 3, 5, 8]
    result_list = [0, 1]
    first, second = 0 , 1
    while len(result_list) < num:
        first, second = second, first + second
        result_list.extend([second])
    return result_list
print(is_fibonacci_series(5))
print("\n")

"""
Palindrom Number - A number when reversed result in exact same number
Input: 12321, 16461
Output: 12321, 16461
"""
def is_palindrom(num):
    # reversed_num = "".join(reversed(str(num)))
    original_num = num
    reversed_num = 0
    while num > 0:
        remainder = num % 10
        reversed_num = (reversed_num * 10) + remainder
        num = num // 10
    return f"{original_num} is a palindrom number" if int(original_num) == int(reversed_num) else f"{original_num} is not a palindrom number"
print(is_palindrom(16461))
print("\n")

"""
Even or Odd Number
Input: 2, 3, 19, 7, 8
Output: Even, Odd, Odd, Odd, Even
"""
def is_num_even_odd(num):
    return f"{num} is an Even Number" if num % 2 == 0 else f"{num} is an Odd Number"
print(is_num_even_odd(10))
print("\n")

"""
Largest Among Three Numbers
Input: 10, 12, 7
Output: 12
"""
def is_max_number(num1, num2, num3):
    # Way 1
    if type(num1) == 'list':
        return f"{max(num1)} is the largest number"
    # Way 2 
    numbers_list = []
    numbers_list.append(num1) 
    numbers_list.append(num2) 
    numbers_list.append(num3)
    return f"{max(numbers_list)} is the largest number"
    # Way 3
    if num1 >= num2 and num1 >= num3:
        return f"{num1} is the largest number"
    elif num2 >= num1 and num2 >= num3:
        return f"{num2} is the largest number"
    else:
        return f"{num3} is the largest number"
    #  Way 4:
    max_num = float('-inf')
    if a > max_num:
        max_num = a
    if b > max_num:
        max_num = b
    if c > max_num:
        max_num
    return f"{max_num} is the largest number"
print(is_max_number(10, 12, 7))
print("\n")

"""
Factorial of a number.
Input: 5
Output 5x4x3x2x1 = 120 
"""
def factorial_of_number(num):
    original_num = num
    factorial_val = 1
    while num > 0:
        factorial_val *= num
        num -= 1
    return f"{factorial_val} is the factorial value of {original_num}"
print(factorial_of_number(5))
print('\n')

"""
Number is a perfect square.
Input: 25
Output: 25 is a perfect square of 5
"""
def is_perfect_square(num):
    original_num = num
    sq_value = original_num ** 0.5
    is_square = sq_value ** 2
    return f"{original_num} is a perfect square of {int(sq_value)}" if is_square == original_num else f"{original_num} is not related to perfect square"
print(is_perfect_square(20))
print('\n')

"""
Greatest Common Divisor (GCD) of two numbers.
Input: 24, 28
Output: 4
"""
def is_common_divisor(num1 = None, num2 = None):
    original_num1, original_num2 = num1, num2
    while num2 != 0:
        num1, num2 = num2, num1 % num2
    return f"Common Divisor for {original_num1}, {original_num2} is: {num1}"
print(is_common_divisor(24, 28))
print('\n')

"""
Least Common Multiple (LCM) of two numbers.
Input: 24, 28
Output: 4
"""
def is_least_common(num1 = None, num2 = None):
    original_num1, original_num2 = num1, num2
    while num2 != 0:
        num1, num2 = num2, num2 % num1
    lcm = (original_num1 * original_num2) // num1
    return f"Least Common Multiple for {original_num1}, {original_num2} is: {lcm}"
print(is_least_common(12, 15))
print('\n')

"""
Binary number to a decimal.
Input: 1011
Output: 11
"""
def is_decimal_from_binary(b_num):
    original_num = b_num
    d_num = 0
    str_num = "".join(reversed(str(b_num)))
    for index, char in enumerate(str_num):
        d_num += int(char) * (2**index)
    return f"{d_num}"
print(is_decimal_from_binary(1011))
print('\n')

"""
Decimal number to a binary
Input: 11
Output: 1011
"""
def is_binary_from_decimal(num):
    original_num = num
    list = []
    b_num = ""
    while num > 0:
        b_num = str(num % 2) + b_num
        num = num // 2
    return f"Binary Representation for {original_num} is: {b_num}"
print(is_binary_from_decimal(11))
print('\n')


"""
First N prime numbers.
Input: 10
Output: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, ......
"""
def get_prime_number_list(num):
    original_num = num
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    primes = []
    candidate = 2
    while len(primes) < num:
        if is_prime(candidate):
            primes.append(candidate)
        candidate += 1
    return f'List of {original_num} Prime Numbers: {", ".join((map(str, primes)))}'
print(get_prime_number_list(10))
print('\n')

"""
Number is a perfect number.
Input: 28
Output: 1,2,4,7,14
"""
def is_perfect_number(num):
    original_num = num
    divisors_list = []
    divisors_num = 0
    for i in range(1, num):
        if num % i == 0:
            divisors_num  += i
            if divisors_num != 28:
                divisors_list.append(divisors_num)
    return f'{original_num} is a Perfect Number as sum of following divisors: {", ".join((map(str, divisors_list)))} is equal to it'
print(is_perfect_number(28))
print('\n')

"""
Sum of digits of a number.
Input: 112
Output: 4
"""
def is_sum_of_digits_of_number(num):
    original_num = num
    sum_of_digits = 0
    for digit in str(num):
        sum_of_digits += int(digit)
    return f'Sum of digits for number {original_num} is: {sum_of_digits}'
print(is_sum_of_digits_of_number(28))
print('\n')

"""
Power of a number without using the built-in function.
"""
def power_of_number(base_num, exponent):
    result = 1
    for i in range(exponent):
        result *= base_num
    return f"Power for provided number {base_num} is: {result}"
print(power_of_number(4, 2))
print('\n')

# Find the n-th Fibonacci number.

# Calculate the sum of the first N natural numbers.

# Check if a number is a strong number.

# Generate the first N terms of the Fibonacci series.

# Check if a number is an Armstrong number.

# Calculate the sum of the squares of the first N natural numbers.

# Find the smallest among three numbers.

# Check if a number is a Harshad number.

# Find the maximum and minimum in a list of numbers.

# Calculate the sum of the first N even numbers.

# Calculate the sum of the first N odd numbers.

# Check if a number is a prime number.

# Generate the first N composite numbers.

# Check if a number is a happy number.

# Calculate the sum of the cubes of the first N natural numbers.

# Find the missing number in an array of consecutive numbers.

# Check if two numbers are amicable numbers.

# Generate a Pascal's Triangle.

# Check if a number is a Mersenne prime.

# Find the prime factors of a number.

# Calculate the digital root of a number.

# Check if a number is a Kaprekar number.

# Generate the Collatz sequence for a number.

# Check if a number is a Magic number.

# Calculate the sum of the first N terms of an arithmetic series.

# Find the roots of a quadratic equation.

# Check if a number is a Duck number.

# Generate the first N terms of a geometric series.

# Check if a number is a Catalan number.

# Calculate the sum of the first N terms of a harmonic series.

# Check if a number is a Smith number.

# Calculate the sum of prime numbers up to N.

# Check if a number is a Perfect square.

# Find the number of trailing zeroes in a factorial.

# Check if a number is a Fermat prime.

# Generate the first N Bell numbers.

# Check if a number is a Keith number.

# Calculate the nth term of a Lucas series.

# Check if a number is a Lychrel number.

# Find the N-th term of a Tribonacci series.

# Check if a number is a Sophie Germain prime.

# Generate a sequence of prime numbers up to N.

# Calculate the sum of the first N terms of a geometric series.

# Check if a number is a Sphenic number.

# Calculate the product of digits of a number.

# Check if a number is a Twin prime.

# Generate the first N terms of a Pell series.

# Check if a number is a Super prime.

# Generate the Ulam sequence up to N.

# Check if a number is a Carmichael number.

# Calculate the sum of factorials of digits of a number.

# Check if a number is a Happy prime.

# Find the number of prime numbers between two numbers.

# Check if a number is a Self number.

# Generate the first N terms of an Eulerian series.

# Check if a number is a Circular prime.

# Calculate the product of the first N natural numbers.

# Find the next prime number greater than N.

# Check if a number is a Friedman number.

# Generate the first N terms of a Stern's diatomic series.

# Check if a number is a Pseudoprime.

# Find the N-th term of a Jacobsthal series.

# Check if a number is a Tetranacci number.

# Generate the first N terms of a Motzkin number series.

# Check if a number is a Nearly perfect number.

# Calculate the sum of the first N terms of a Bernoulli series.

# Check if a number is a Primorial prime.

# Generate the first N terms of a Thue-Morse sequence.

# Check if a number is an Achilles number.

# Calculate the sum of digits of a number raised to a power.

# Check if a number is a Narcissistic number.

# Generate the first N terms of a Fibonacci-like sequence.

# Check if a number is a Star number.

# Calculate the product of prime numbers up to N.

# Check if a number is an Ore number.

# Generate the first N terms of a Lagged Fibonacci series.

# Check if a number is a Practical number.

# Find the sum of digits of a number.

# Check if a number is an Extravagant number.

# Generate the first N terms of a Lucas-Carmichael number series.

# Check if a number is a Happy number.

# Calculate the sum of the digits of a number until a single digit is obtained.

# Check if a number is an Economical number.

# Generate the first N terms of a Fibonacci-like series.

# Check if a number is a Triangular number.

# Calculate the sum of the first N terms of a Fibonacci series.