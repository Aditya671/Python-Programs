# Python Number System Utilities

## Usage For NumberSystem

The `NumberSystem` class provides a set of methods to perform various operations on numbers. Here's an example of how to use the class:

```python
from __init__ import NumberSystem

number_system = NumberSystem()

# Get the precision value of a number
precision_value = number_system.percision_value(3.14159)
print(precision_value)  # Output: 5

# Reverse a number
reversed_number = number_system.reverse_number(12345)
print(reversed_number)  # Output: 54321

# Check if a number is an Armstrong number
is_armstrong = number_system.armstrong_number(153)
print(is_armstrong)  # Output: True
```

## API

The `NumberSystem` class provides the following methods:

- `percision_value(input_num)`: Returns the precision value of the input number.
- `reverse_number(input_num)`: Reverses the input number.
- `armstrong_number(input_num)`: Checks if the input number is an Armstrong number.
- `perfect_number(input_num)`: Checks if the input number is a perfect number.
- `prime_number(input_num)`: Checks if the input number is a prime number.
- `prime_number_list(input_num)`: Returns a list of prime numbers up to the input number.
- `composite_number(input_num)`: Checks if the input number is a composite number.
- `palindrom_number(input_num)`: Checks if the input number is a palindrome.
- `even_odd_number(input_num)`: Checks if the input number is even or odd.
- `perfect_square(input_num)`: Checks if the input number is a perfect square.
- `common_divisor(input_num_1, input_num_2)`: Finds the common divisor of two input numbers.
- `least_common_divisor(input_num_1, input_num_2)`: Finds the least common divisor of two input numbers.
- `decimal_form_from_binary(input_num)`: Converts a binary number to its decimal form.
- `binary_form_from_decimal(input_num)`: Converts a decimal number to its binary form.
- `factorial_number(input_num)`: Calculates the factorial of the input number.
- `sum_of_all_digits(input_num)`: Calculates the sum of all digits in the input number.
- `number_raise_to_power(input_num, to_power)`: Raises the input number to the specified power.
- `maximum_among_three(input_num_1, input_num_2, input_num_3)`: Finds the maximum among three input numbers.
- `smallest_amoung_three(input_num_1, input_num_2, input_num_3)`: Finds the smallest among three input numbers.
- `fibonacci_series(input_num)`: Generates the Fibonacci series up to the input number.
- `nth_fibonacci_number(input_num)`: Calculates the nth Fibonacci number.
- `strong_number(input_num)`: Checks if the input number is a strong number.
- `sum_of_squares_of_numbers(input_num)`: Calculates the sum of squares of all digits in the input number.
- `harshad_number(input_num)`: Checks if the input number is a Harshad number.
- `min_max_num_list(input_num_list)`: Finds the minimum and maximum values in the input list of numbers.
- `pascal_triangle(input_num)`: Generates the Pascal triangle up to the input number.
- `sum_of_cubes_of_numbers(input_num)`: Calculates the sum of cubes of all digits in the input number.
- `prime_factor(input_num)`: Finds the prime factors of the input number.
- `missing_number_in_regual_list(input_num_list)`: Finds the missing number in a regular list of numbers.


# # Python List System Utilities

## Usage For ListSystem

The `ListSystem` class is designed to execute various methodologies related to lists. Here's an example of how to use it:

```python
from __init__ import ListSystem

# Create a ListSystem instance with one or more input lists
list_system = ListSystem([1, 2, 3], ['a', 'b', 'c'])

# Get the maximum value in a list
max_value = list_system.max_in_list([1, 2, 3])
print(max_value)  # Output: 3
```

## API

- `percision_value(input_num)`: Returns the precision value of the input number.
The `ListSystem` class has the following methods:

### `__init__(self, *input_lists)`
- Initializes the `ListSystem` instance with one or more input lists.
- `max_in_list(self, input_list)`: Returns the maximum value in the given input list.
