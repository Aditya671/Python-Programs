"""
Here's a cheat sheet of Python's string methods to help you quickly reference and use them:
-------------------------------------------------------------------------------------------------------------------------
| Method                           | Description                                                                        |
|----------------------------------|------------------------------------------------------------------------------------|
| `capitalize()`                   | Capitalizes the first character of the string.                                     |
| `casefold()`                     | Converts the string to lowercase, more aggressive than `lower()`.                  |
| `center(width, fillchar)`        | Centers the string, padding it with `fillchar`.                                    |
| `count(sub, start, end)`         | Counts occurrences of `sub` in the string.                                         |
| `encode(encoding, errors)`       | Encodes the string using the specified encoding.                                   |
| `endswith(suffix, start, end)`   | Checks if the string ends with `suffix`.                                           |
| `expandtabs(tabsize)`            | Expands tabs in the string to multiple spaces.                                     |
| `find(sub, start, end)`          | Finds the first occurrence of `sub` in the string.                                 |
| `format(*args, **kwargs)`        | Formats the string using specified arguments.                                      |
| `format_map(mapping)`            | Formats the string using a dictionary.                                             |
| `index(sub, start, end)`         | Finds the first occurrence of `sub` in the string. Raises ValueError if not found. |
| `isalnum()`                      | Checks if all characters in the string are alphanumeric.                           |
| `isalpha()`                      | Checks if all characters in the string are alphabetic.                             |
| `isascii()`                      | Checks if all characters in the string are ASCII.                                  |
| `isdecimal()`                    | Checks if all characters in the string are decimal characters.                     |
| `isdigit()`                      | Checks if all characters in the string are digits.                                 |
| `isidentifier()`                 | Checks if the string is a valid identifier.                                        |
| `islower()`                      | Checks if all characters in the string are lowercase.                              |
| `isnumeric()`                    | Checks if all characters in the string are numeric.                                |
| `isprintable()`                  | Checks if all characters in the string are printable.                              |
| `isspace()`                      | Checks if all characters in the string are whitespace.                             |
| `istitle()`                      | Checks if the string is in title case.                                             |
| `isupper()`                      | Checks if all characters in the string are uppercase.                              |
| `join(iterable)`                 | Joins elements of an iterable with the string as a separator.                      |
| `ljust(width, fillchar)`         | Left-justifies the string, padding it with `fillchar`.                             |
| `lower()`                        | Converts all characters to lowercase.                                              |
| `lstrip(chars)`                  | Removes leading characters specified in `chars`.                                   |
| `maketrans(x, y, z)`             | Creates a translation table.                                                       |
| `partition(sep)`                 | Splits the string into a tuple at the first occurrence of `sep`.                   |
| `replace(old, new, count)`       | Replaces occurrences of `old` with `new`.                                          |
| `rfind(sub, start, end)`         | Finds the last occurrence of `sub` in the string.                                  |
| `rindex(sub, start, end)`        | Finds the last occurrence of `sub` in the string. Raises ValueError if not found.  |
| `rjust(width, fillchar)`         | Right-justifies the string, padding it with `fillchar`.                            |
| `rpartition(sep)`                | Splits the string into a tuple at the last occurrence of `sep`.                    |
| `rsplit(sep, maxsplit)`          | Splits the string from the right using `sep`.                                      |
| `rstrip(chars)`                  | Removes trailing characters specified in `chars`.                                  |
| `split(sep, maxsplit)`           | Splits the string using `sep`.                                                     |
| `splitlines(keepends)`           | Splits the string at line breaks.                                                  |
| `startswith(prefix, start, end)` | Checks if the string starts with `prefix`.                                         |
| `strip(chars)`                   | Removes leading and trailing characters specified in `chars`.                      |
| `swapcase()`                     | Swaps the case of all characters in the string.                                    |
| `title()`                        | Capitalizes the first character of each word in the string.                        |
| `translate(table)`               | Translates the string using a translation table.                                   |
| `upper()`                        | Converts all characters to uppercase.                                              |
| `zfill(width)`                   | Pads the string with zeros on the left to fill the specified width.                |
-------------------------------------------------------------------------------------------------------------------------
"""

def no_of_occurrence_of_word_in_string(input_string, word = None):
    word_count = 0
    if word is None:
        word = input_string.split()[0]
    # input_string.count(word)
    for w in input_string.split():
        if word in w or word == w:
            word_count += 1
    return f"Occurence of word `{word}` is: {word_count} and calculated on the basis of similar pattern presence in statement and as a word"
print(no_of_occurrence_of_word_in_string('This is a practice statement and is for prac', 'is'))
print('\n')

def no_of_vowels_in_string(input_string):
    actual_vowels = "aeiou"
    original_string = str(input_string)
    vowel_count = 0
    actual_vowels_count = {}
    for char in input_string.lower():
        if char in actual_vowels and char.isalpha():
            vowel_count += 1
            if char in actual_vowels_count.keys():
                actual_vowels_count[char] = int(actual_vowels_count.get(char,0)) + 1
            else:
                actual_vowels_count[char] = 1
    return f"Total Count of Vowels: {vowel_count} and vowels list count: {actual_vowels_count}"
print(no_of_vowels_in_string('This is a practice statement'))
print('\n')

def length_of_string(input_string):
    str_len = 0
    # str_len = len(input_string)
    for char in input_string.replace(" ", ''):
        str_len += 1
    return f"Length of String (exclusing spaces): {str_len}"
print(length_of_string('This is    a  practice  statement'))
print('\n')

def no_of_consonants_in_string(input_string):
    vowels = 'aeiou'
    original_string = str(input_string)
    non_vowel_count = 0
    actual_non_vowels_count = {}
    for char in input_string.lower():
        if char not in actual_non_vowels_count and char.isalpha() and char not in vowels:
            non_vowel_count += 1
            actual_non_vowels_count[char] = 1
        if char in actual_non_vowels_count.keys() and char not in vowels:
            actual_non_vowels_count[char] = int(actual_non_vowels_count.get(char, 0)) + 1                
    return f"Total Count of Consonants: {non_vowel_count} and Consonants list count: {actual_non_vowels_count}"
print(no_of_consonants_in_string('This is a practice statement and is for practice'))
print('\n')

def reverse_a_string(input_string):
    original_string = str(input_string)
    reversed_string = ''
    for index in range(len(original_string) - 1, -1, -1):
        reversed_string += str(original_string[index])
    return f"Reversed String: {reversed_string}"
print(reverse_a_string('This is a statement'))
print('\n')

def reverse_word_in_string(input_string):
    original_string = str(input_string)
    words_list = []
    formed_word = ""
    reversed_string = ""
    for char in original_string:
        if char != " ":
            formed_word += char
        else:
            words_list.append(formed_word)
            formed_word = ""
    # Append the last formed word
    if formed_word:
        words_list.append(formed_word)

    for index in range(len(words_list) - 1, -1, -1):
        reversed_string += words_list[index] + " "
    return f"Reversed String: {reversed_string}"
print(reverse_word_in_string('This is a statement'))
print('\n')
"""
Convert a string to uppercase.

Convert a string to lowercase.

Capitalize the first letter of each word in a string.

Replace a specific substring in a string with another substring.

Check if a string is a palindrome.

Find the index of the first occurrence of a substring in a string.

Find the index of the last occurrence of a substring in a string.

Extract a substring from a string.

Split a string into a list of words.

Join a list of words into a string.

Remove leading and trailing whitespace from a string.

Remove all whitespace from a string.

Count the number of words in a string.

Find the most frequent character in a string.

Find the least frequent character in a string.

Replace all vowels in a string with a specific character.

Replace all consonants in a string with a specific character.

Check if a string contains only digits.

Check if a string contains only alphabets.

Check if a string contains only alphanumeric characters.

Convert a string to a list of characters.

Convert a list of characters to a string.

Remove all digits from a string.

Remove all special characters from a string.

Find the number of uppercase letters in a string.

Find the number of lowercase letters in a string.

Check if a string starts with a specific substring.

Check if a string ends with a specific substring.

Find the longest word in a string.

Find the shortest word in a string.

Count the number of sentences in a string.

Find the first word in a string.

Find the last word in a string.

Swap the case of all characters in a string.

Check if a string contains a specific substring.

Create a string from the first n characters of another string.

Create a string from the last n characters of another string.

Find the ASCII value of a character.

Convert an ASCII value to a character.

Check if two strings are anagrams.

Find all substrings of a string.

Create a string with n repetitions of a specific character.

Create a string with n repetitions of a specific substring.

Find the first non-repeating character in a string.

Find the first repeating character in a string.

Find the longest common prefix of two strings.

Find the longest common suffix of two strings.

Check if a string contains only unique characters.

Find all permutations of a string.

Reverse the words in a string.

Replace all occurrences of a character in a string with another character.

Replace the first occurrence of a character in a string with another character.

Replace the last occurrence of a character in a string with another character.

Check if a string is a valid email address.

Check if a string is a valid URL.

Check if a string is a valid IP address.

Convert a string to title case.

Find the longest palindromic substring in a string.

Find the shortest palindromic substring in a string.

Create a string with the characters in a specific range of Unicode values.

Find the number of occurrences of each character in a string.

Count the number of specific words in a string.

Extract all digits from a string.

Extract all alphabets from a string.

Extract all special characters from a string.

Check if two strings are rotations of each other.

Check if a string is a valid identifier.

Convert a string to a list of words in reverse order.

Convert a list of words in reverse order to a string.

Find the longest sequence of consecutive identical characters in a string.

Find the longest sequence of consecutive different characters in a string.

Create a string with the unique characters in a string.

Create a string with the duplicate characters in a string.

Check if a string contains only whitespace characters.

Convert a string to a list of integers.

Convert a list of integers to a string.

Create a string with the characters in the middle of a string.

Create a string with the characters at the beginning and end of a string.

Create a string with the characters in alternating uppercase and lowercase.

Create a string with the characters in alternating lowercase and uppercase.

Find the position of a substring in a string.

Check if a string is a valid palindrome ignoring spaces, punctuation, and case.

Find the longest word that can be formed from the characters of a string.

Find the shortest word that can be formed from the characters of a string.

Create a string with the characters in every nth position of a string.

Create a string with the characters in every even position of a string.

Create a string with the characters in every odd position of a string.

Create a string with the characters in every prime position of a string.

Create a string with the characters in every composite position of a string.

Create a string with the characters at the positions of another string.

Create a string with the characters in the reverse order of their positions.

Create a string with the characters in the positions of a rotated string.

Create a string with the characters in the positions of an anagram string.

Create a string with the characters in the positions of a palindrome string.

Create a string with the characters in the positions of a unique character string.

Create a string with the characters in the positions of a duplicate character string.

Create a string with the characters in the positions of a whitespace character string.

Create a string with the characters in the positions of a non-whitespace character string.

Create a string with the characters in the positions of a digit character string.

Create a string with the characters in the positions of a non-digit character string.

Create a string with the characters in the positions of an alphabet character string.

Create a string with the characters in the positions of a non-alphabet character string.

Create a string with the characters in the positions of an alphanumeric character string.

Create a string with the characters in the positions of a non-alphanumeric character string.

Create a string with the characters in the positions of a special character string.

Create a string with the characters in the positions of a non-special character string.

Create a string with the characters in the positions of an uppercase character string.

Create a string with the characters in the positions of a lowercase character string.

Create a string with the characters in the positions of a title case character string.

Create a string with the characters in the positions of a swapped case character string.

Create a string with the characters in the positions of a valid email address string.

Create a string with the characters in the positions of a valid URL string.

Create a string with the characters in the positions of a valid IP address string.

Create a string with the characters in the positions of a valid identifier string.

Create a string with the characters in the positions of a valid palindrome string.
"""