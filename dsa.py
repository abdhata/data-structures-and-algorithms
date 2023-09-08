# Question1

def is_balanced(expression):
    stack = []
    brackets = {')': '(', '}': '{', ']': '['}

    for char in expression:
        if char in '({[':
            stack.append(char)
        elif char in ')}]':
            if not stack or stack.pop() != brackets[char]:
                return False

    return not stack

expression1 = "([]{})"
expression2 = "([)]"
print(is_balanced(expression1))  # Output: True
print(is_balanced(expression2))  # Output: False


# Question 2

def remove_duplicates(sequence):
    seen = set()
    result = []
    
    for item in sequence:
        if item not in seen:
            seen.add(item)
            result.append(item)
    
    return result

input_sequence = [2, 3, 2, 4, 5, 3, 6, 7, 5]
result = remove_duplicates(input_sequence)
print(result)  # Output: [2, 3, 4, 5, 6, 7]


# Question 3

import re

def word_frequency(sentence):
    words = re.findall(r'\w+', sentence.lower())
    frequency = {}
    
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    
    return frequency

sentence = "This is a test sentence. This sentence is a test."
result = word_frequency(sentence)
print(result)
