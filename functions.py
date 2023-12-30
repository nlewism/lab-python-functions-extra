def get_unique_list_f(list):
    """
    Takes a list as an argument and returns a new list with unique elements from the first list.

    Parameters:
    lst (list): The input list.

    Returns:
    list: A new list with unique elements from the input list.
    """
    
    user_input = input("Enter a list of numbers, repeat as you wish:")
    number_list = []

    for character in user_input:
        if character.isdigit():
            number_list.append(int(character))

    return list(set(number_list))

def count_case_f(string):
    """
    Returns the number of uppercase and lowercase letters in the given string.

    Parameters:
    string (str): The string to count uppercase and lowercase letters in.

    Returns:
    A tuple containing the count of uppercase and lowercase letters in the string.
    """
    # my code
    string = input("Enter your favorite quote or poem:")

    count_lower = 0
    count_upper = 0

    for char in string:
        if char.islower():
            count_lower += 1
        elif char.isupper():
            count_upper += 1

    return tuple((count_lower, count_upper))

def remove_punctuation_f(sentence):
    """
    Removes all punctuation marks (commas, periods, exclamation marks, question marks) from a sentence.

    Parameters:
    sentence (str): A string representing a sentence.

    Returns:
    str: The sentence without any punctuation marks.
    """
    # your code goes here
    
    sentence = sentence.replace(",","").replace(".","").replace("!","").replace("?","").replace(":","")
    
    return sentence

def word_count_f(sentence):
    """
    Counts the number of words in a given sentence. To do this properly, first it removes punctuation from the sentence.
    Note: A word is defined as a sequence of characters separated by spaces. We can assume that there will be no leading or trailing spaces in the input sentence.
    
    Parameters:
    sentence (str): A string representing a sentence.

    Returns:
    int: The number of words in the sentence.
    """
    sentence = sentence.replace(",","").replace(".","").replace("!","").replace("?","").replace(":","")
    words = sentence.split()
    count = len(words)
    return sentence, count

def calculate_f(operator,*operands):
    
    result = operands[0]
    
    for operand in operands[1:]:
    
        if operator == '+':
            result += operand
        elif operator == '-':
            result -= operand
        elif operator == '*':
            result *= operand
        elif operator == '/':
            result /= operand
        else:
            print("Error: Invalid Operator")
            result = None
            
    return result
