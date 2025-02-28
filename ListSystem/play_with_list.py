
def find_max_in_list(input_list):
    # return max(list(filter(lambda x: str(x).isnumeric(), input_list)))
    max_num = float('-inf')
    for num in input_list:
        if str(num).isnumeric() and num > max_num:
            max_num = num
    return max_num

def find_min_in_list(input_list):
    # return min(list(filter(lambda x: str(x).isnumeric(), input_list)))
    min_num = float('inf')
    for num in input_list:
        if str(num).isnumeric() and num < min_num:
            min_num = num
    return min_num

def insert_at_index(input_list = [], postion = 0, add_value = 0):
    # input_list.insert(postion, add_value)
    return  input_list[postion:] + [add_value] + input_list[:postion]

def pop_at_index(input_list = [], postion = 0, add_value = 0):
    return input_list.pop(postion)

def sort_ascending(input_list = []):
    # sorted(input_list)
    n = len(input_list)
    for i in range(n):
        for j in range(i+1, n):
            if input_list[i] > input_list[j]:
                input_list[i], input_list[j] = input_list[j], input_list[i]
    return input_list

def sort_descending(input_list = []):
    # sorted(input_list)
    n = len(input_list)
    for i in range(n):
        for j in range(i+1, n):
            if input_list[i] < input_list[j]:
                input_list[i], input_list[j] = input_list[j], input_list[i]
    return input_list

def length_of_list(input_list = []):
    # len(input_list)
    count = 0
    for val in input_list:
        count += 1
    return count

def list_add_new_element_at_end(input_list = [], value = 0):
    # input_list.append(value)
    length = length_of_list(input_list)
    input_list = input_list + [0]
    input_list[length + 1] = value
    return input_list

def remove_specific_value(input_list = [], value = 0):
    return input_list.remove(value)

def count_value_occurrence_in_list(input_list = [], value = 0):
    # input_list.count(value)
    # count = count + 1 for val in input_list if val == value
    count = 0
    for val in input_list:
        if val == value:
            count += 1
    return count

def reverse_a_list(input_list = []):
    # input_list[::-1]
    list_len = len(input_list)
    new_list = []
    for index in range(list_len - 1, -1, -1):
        new_list.append(input_list[index])
    return new_list

def sum_of_elements(input_list):
    # sum(val for val in input_list)
    # sum(input_list)
    sum_list = 0
    for val in input_list:
        sum_list += val
    return sum_list

"""
Find the average of all elements in a list.

Find the median of a list.

Find the mode of a list.

Check if a specific element is in a list.

Concatenate two lists.

Create a list of even numbers.

Create a list of odd numbers.

Find the index of the first occurrence of an element in a list.

Find the index of the last occurrence of an element in a list.

Remove duplicates from a list.

Find the difference between the largest and smallest elements in a list.

Find the product of all elements in a list.

Create a list of squares of numbers from 1 to 10.

Create a list of cubes of numbers from 1 to 10.

Create a list of prime numbers up to a certain number.

Create a list of Fibonacci numbers up to a certain number.

Find the second largest number in a list.

Find the second smallest number in a list.

Create a list of random numbers.

Sort a list of strings.

Sort a list of tuples based on the first element.

Sort a list of tuples based on the second element.

Merge two sorted lists into one sorted list.

Create a list from the keys of a dictionary.

Create a list from the values of a dictionary.

Create a list of the first n natural numbers.

Create a list of the first n odd numbers.

Create a list of the first n even numbers.

Create a list of the first n multiples of 5.

Create a list of the first n multiples of 7.

Find the intersection of two lists.

Find the union of two lists.

Find the difference of two lists.

Find the symmetric difference of two lists.

Create a list of characters from a string.

Create a list of words from a string.

Create a list of the lengths of each word in a string.

Create a list of vowels from a string.

Create a list of consonants from a string.

Create a list of numbers divisible by a specific number.

Create a list of palindromes from a list of strings.

Create a list of anagrams from a list of strings.

Create a list of factorials for numbers from 1 to 10.

Create a list of lists (2D list).

Create a list of lists and flatten it.

Transpose a 2D list.

Find the maximum element in each row of a 2D list.

Find the minimum element in each row of a 2D list.

Calculate the row sums of a 2D list.

Calculate the column sums of a 2D list.

Remove all instances of a specific element from a list.

Create a list with elements in random order.

Create a list with elements in sorted order.

Create a list of the first n factorials.

Create a list of strings in uppercase.

Create a list of strings in lowercase.

Create a list of the lengths of each string in a list.

Create a list of strings with a specific prefix.

Create a list of strings with a specific suffix.

Create a list of strings that start with a specific letter.

Create a list of strings that end with a specific letter.

Create a list of strings containing a specific substring.

Remove leading and trailing whitespace from each string in a list.

Convert a list of integers to a list of strings.

Convert a list of strings to a list of integers.

Create a list of the squares of the first n even numbers.

Create a list of the squares of the first n odd numbers.

Create a list of the cubes of the first n even numbers.

Create a list of the cubes of the first n odd numbers.

Create a list of the first n perfect squares.

Create a list of the first n perfect cubes.

Create a list of the first n powers of 2.

Create a list of the first n powers of 3.

Create a list of the first n powers of 4.

Create a list of the first n harmonic numbers.

Create a list of the first n triangular numbers.

Create a list of the first n tetrahedral numbers.

Create a list of the first n pentagonal numbers.

Create a list of the first n hexagonal numbers.

Create a list of the first n heptagonal numbers.

Create a list of the first n octagonal numbers.

Create a list of strings sorted by length.

Create a list of tuples where each tuple contains a number and its square.

Create a list of tuples where each tuple contains a number and its cube.

Create a list of tuples where each tuple contains a number and its factorial.

Create a list of the squares of numbers in a given range.

Create a list of the cubes of numbers in a given range.

Create a list of the factorials of numbers in a given range.

Find the second maximum number in a list.

Find the second minimum number in a list.

Insert multiple elements at specific indices in a list.

Pop multiple elements from specific indices in a list.

Sort a list of tuples based on the sum of their elements.

Create a list of prime factors for a given number.

Find the GCD of all elements in a list.

Find the LCM of all elements in a list.

Create a list of elements that are common in two lists.

Create a list of elements that are unique to each list in two lists.

Create a list of the differences between consecutive elements in a list.

Create a list of the cumulative sum of elements in a list.

Create a list of the cumulative product of elements in a list.

Find the maximum product of any two elements in a list.

Find the maximum sum of any two elements in a list.

Rotate a list to the right by a given number of steps.

Rotate a list to the left by a given number of steps.

Check if a list is sorted in ascending order.

Check if a list is sorted in descending order.

Create a list of all possible pairs of elements from two lists.

Create a list of all possible combinations of elements from two lists.

Find the longest consecutive subsequence in a list.

Find the longest increasing subsequence in a list.

Find the longest decreasing subsequence in a list.

Create a list of elements that are present in all given lists.

Create a list of elements that are present in at least one of the given lists.

Create a list of elements that are present in exactly one of the given lists.

Create a list of elements that are present in an odd number of the given lists.

Find the maximum difference between any two elements in a list.

Find the maximum sum of a sublist in a list.

Find the maximum product of a sublist in a list.

Check if a list is a palindrome.

Create a list of palindromic sublists in a list.

Create a list of anagram pairs in a list.

Find the longest word in a list of strings.

Find the shortest word in a list of strings.

Create a list of the indices of all occurrences of an element in a list.

Create a list of the indices of all even elements in a list.

Create a list of the indices of all odd elements in a list.

Create a list of all sublists of a given list.

Create a list of all sublists of a given length in a list.

Find the longest common prefix of a list of strings.

Find the longest common suffix of a list of strings.
"""