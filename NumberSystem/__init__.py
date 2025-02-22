"""
Here's a handy cheat sheet for Python operators. Operators allow you to perform operations on variables and values. They can be classified into different categories:

### Arithmetic Operators
| Operator | Description                 | Example        |
|----------|-----------------------------|----------------|
| `+`      | Addition                    | `a + b`        |
| `-`      | Subtraction                 | `a - b`        |
| `*`      | Multiplication              | `a * b`        |
| `/`      | Division                    | `a / b`        |
| `%`      | Modulus (remainder)         | `a % b`        |
| `**`     | Exponentiation (power)      | `a ** b`       |
| `//`     | Floor division              | `a // b`       |

### Comparison Operators
| Operator | Description                 | Example        |
|----------|-----------------------------|----------------|
| `==`     | Equal to                    | `a == b`       |
| `!=`     | Not equal to                | `a != b`       |
| `>`      | Greater than                | `a > b`        |
| `<`      | Less than                   | `a < b`        |
| `>=`     | Greater than or equal to    | `a >= b`       |
| `<=`     | Less than or equal to       | `a <= b`       |

### Assignment Operators
| Operator | Description                 | Example        |
|----------|-----------------------------|----------------|
| `=`      | Assign                      | `a = b`        |
| `+=`     | Add and assign              | `a += b`       |
| `-=`     | Subtract and assign         | `a -= b`       |
| `*=`     | Multiply and assign         | `a *= b`       |
| `/=`     | Divide and assign           | `a /= b`       |
| `%=`     | Modulus and assign          | `a %= b`       |
| `**=`    | Exponentiation and assign   | `a **= b`      |
| `//=`    | Floor division and assign   | `a //= b`      |

### Logical Operators
| Operator | Description                 | Example        |
|----------|-----------------------------|----------------|
| `and`    | Logical AND                 | `a and b`      |
| `or`     | Logical OR                  | `a or b`       |
| `not`    | Logical NOT                 | `not a`        |

### Bitwise Operators
| Operator | Description                 | Example        |
|----------|-----------------------------|----------------|
| `&`      | Bitwise AND                 | `a & b`        |
| `|`      | Bitwise OR                  | `a | b`        |
| `^`      | Bitwise XOR                 | `a ^ b`        |
| `~`      | Bitwise NOT                 | `~a`           |
| `<<`     | Bitwise left shift          | `a << b`       |
| `>>`     | Bitwise right shift         | `a >> b`       |

### Membership Operators
| Operator | Description                      | Example         |
|----------|----------------------------------|-----------------|
| `in`     | True if value is in sequence     | `a in list`     |
| `not in` | True if value is not in sequence | `a not in list` |

### Identity Operators
| Operator | Description                                    | Example      |
|----------|------------------------------------------------|--------------| 
| `is`     | True if both variables are the same object     | `a is b`     |
| `is not` | True if both variables are not the same object | `a is not b` |

### Unary Operators
| Operator | Description                 | Example        |
|----------|-----------------------------|----------------|
| `+`      | Unary plus                  | `+a`           |
| `-`      | Unary minus (negation)      | `-a`           |
| `not`    | Logical NOT                 | `not a`        |


"""
import play_with_numbers as pn
class NumberSystem:
    def __init__(self):
        self.description = 'Class to Execute various methodologies related to numbers'
    
    percision_value = lambda self, input_num : pn.return_percision_value(input_num)

    reverse_number = lambda input_num : pn.reverse_a_num(input_num)

    armstrong_number = lambda self, input_num : pn.is_armstrong_number(input_num)

    perfect_number = lambda input_num : pn.is_perfect_number(input_num)

    prime_number = lambda input_num : pn.is_prime_number(input_num)

    prime_number_list = lambda input_num : pn.get_prime_number_list(input_num)
    
    composite_number = lambda input_num : pn.is_composite_number(input_num)

    palindrom_number = lambda input_num : pn.is_palindrom_number(input_num)

    even_odd_number = lambda input_num : pn.is_num_even_odd(input_num)

    perfect_square = lambda input_num: pn.is_perfect_square(input_num)

    common_divisor = lambda input_num_1, input_num_2 : pn.is_common_divisor(input_num_1, input_num_2)
    
    least_common_divisor = lambda input_num_1, input_num_2 : pn.is_least_common(input_num_1, input_num_2)

    decimal_form_from_binary = lambda input_num: pn.is_decimal_from_binary(input_num)

    binary_form_from_decimal = lambda input_num : pn.is_binary_from_decimal(input_num)

    factorial_number = lambda input_num : pn.factorial_of_number(input_num)

    sum_of_all_digits = lambda input_num : pn.is_sum_of_digits_of_number(input_num)

    number_raise_to_power = lambda input_num, to_power : pn.power_of_number(input_num, to_power)

    maximum_among_three = lambda input_num_1, input_num_2, input_num_3 : pn.is_max_among_three_number(input_num_1, input_num_2, input_num_3) 
        
    fibonacci_series = lambda input_num: pn.is_fibonacci_series(input_num)

number_system = NumberSystem()

# Call the methods
percision_value_result = number_system.armstrong_number(111.456)
NumberSystem().__init__()