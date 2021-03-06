# arrays_strings/strings.py
#
# Author: Daniel Clark, 2016

'''
This module contains functions to solve problems related to string
manipulation and testing
'''

def check_unique_chars(input_str):
    '''
    Function to check if string is composed of all unique characters

    Time complexity: O(n)

    Paramters
    ---------
    input_str : string
        input string to test for unique-ness

    Returns
    -------
    is_unique : boolean
        flag indicating whether string is unique or not
    '''

    # Check input type
    if not isinstance(input_str, str):
        err_msg = 'Input: %s is not string!' % str(input_str)
        raise TypeError(err_msg)

    # Init variables
    chars_dict = {}
    is_unique = True

    # Iterate through string chars
    for char in input_str:
        if not chars_dict.has_key(char):
            chars_dict[char] = 1
        else:
            is_unique = False
            break

    # Return flag
    return is_unique


def check_unique_chars2(input_str):
    '''
    Function to check if string is composed of all unique characters
    using no other external data structures

    Time complexity: O(n^2)

    Paramters
    ---------
    input_str : string
        input string to test for unique-ness

    Returns
    -------
    is_unique : boolean
        flag indicating whether string is unique or not
    '''

    # Check input type
    if not isinstance(input_str, str):
        err_msg = 'Input: %s is not string!' % str(input_str)
        raise TypeError(err_msg)

    # Init variables
    is_unique = True

    # Iterate through string chars
    for idx, char in enumerate(input_str):
        rest_of_str = input_str[idx+1:]
        if char in rest_of_str:
            is_unique = False
            break

    # Return flag
    return is_unique


def reverse_cstyle_str(input_str):
    '''
    Reverse a c-style string (ending in null char: '\0')

    Parameters
    ----------
    input_str : string
        the c-style string to reverse and return

    Returns
    -------
    rev_str : string
        the reversed input string
    '''

    # Check input type
    if not isinstance(input_str, str):
        err_msg = 'Input: %s is not string!' % str(input_str)
        raise TypeError(err_msg)

    # Init variables
    str_length = len(input_str)-1 # Ignore null char
    rev_str = '\0'

    # Iterate through string from end to beginning
    for idx in range(str_length):
        rev_idx = str_length - 1 - idx
        rev_char = input_str[rev_idx]
        rev_str = rev_str + rev_char

    # Return reversed string
    return rev_str


def remove_dup_chars(input_str):
    '''
    Remove all duplicate characters while preserving input_str order

    Parameters
    ----------
    input_str : string
        input string to remove dups from

    Returns
    -------
    input_str : string
        the input string without duplicate chars
    '''

    # Check input type
    if not isinstance(input_str, str):
        err_msg = 'Input: %s is not string!' % str(input_str)
        raise TypeError(err_msg)

    # Iterate through input
    for idx, char in enumerate(input_str):
        if char in input_str[idx+1:]:
            input_str = input_str[:idx+1] + \
                        input_str[idx+1:].replace(char, '')

    # Return input_str
    return input_str


def remove_dup_chars2(input_str):
    '''
    Remove all duplicate characters while presering input_str order;
    this method does not use the python replace() function

    Parameters
    ----------
    input_str : string
        input string to remove dups from

    Returns
    -------
    input_str : string
        the input string without duplicate chars
    '''

    # Init variables
    itr = 0
    chk = 1 

    # While checker is still in string
    while chk < len(input_str):
        # Iterate through all chars before checker and compare
        while itr < chk:
            # If there's a match, omit chk char from new string
            if input_str[itr] == input_str[chk]:
                if chk == len(input_str)-1:
                    input_str = input_str[:chk]
                    break
                else:
                    input_str = input_str[:chk] + input_str[chk+1:]
                itr = 0
            # Otherwise, check next itr char
            else:
                itr += 1
        # Iterator made it to checker, increment checker and reset iterator
        chk += 1
        itr = 0

    # Return unique'd string
    return input_str


def check_anagrams(str1, str2):
    '''
    Function to check if two strings are anagrams of eachother
    '''

    # Init variables
    dict1 = {}
    dict2 = {}

    # Build dict from str1
    for char in str1:
        if dict1.has_key(char):
            dict1[char] += 1
        else:
            dict1[char] = 1

    # Build dict from str2
    for char in str2:
        if dict2.has_key(char):
            dict2[char] += 1
        else:
            dict2[char] = 1

    # If they are equal, return True
    if dict1 == dict2:
        return True
    else:
        return False


def find_largest_palindrome(in_str):
    '''
    Function to find the largest palindrome in a given string using
    double for loop

    Parameters
    ----------
    in_str : string
        string to find palindrome in

    Returns
    -------
    largest : string
        the largest palindrome from in_str
    '''

    # Init variables
    largest = ''

    # For each start char
    for start, _ in enumerate(in_str):
        # For every other char
        for end, _ in enumerate(in_str[start:]):
            # Grab substring and reverse it
            substr = in_str[start:end+1]
            revstr = substr[::-1]
            # If it is equal to its reverse and its length is bigger
            # than before
            if substr == revstr and len(substr) > len(largest):
                largest = substr

    # Return largest found
    return largest


def palindrome(in_str):
    if len(in_str) < 2:
        return in_str

    long = in_str[0]
    for i in xrange(0, len(in_str)):
        j = 1+2
        if j < len(in_str):
            pal = in_str[i:j]
            while pal == pal[::-1]:
                long = pal
                j += 1
                pal = in_str[i:j]


def find_largest_palindrome2(in_str):
    '''
    Function to find the largest palindrome in a given string using
    while loop

    Parameters
    ----------
    in_str : string
        string to find palindrome in

    Returns
    -------
    largest : string
        the largest palindrome from in_str
    '''

    # Init variables
    largests = []
    largest = in_str
    i = 0

    # While the beg index less than length of input
    while i < len(in_str):
        # No palindrome
        if largest != largest[::-1]:
            # Take off last char
            largest = largest[:-1]
            # If its only 1 char
            if len(largest) < 2:
                # Increment beg index and take off beg char
                i += 1
                largest = in_str[i:]
        # Found palindrome
        else:
            largests.append(largest)
            i += 1
            largest = in_str[i:]

    # Return longest palindrome
    return max(largests, key=len)


def find_permutations(in_str):
    '''
    Find all possible permutations of string
    '''

    # Base case
    if len(in_str) < 2:
        return [in_str]

    # Recursively call until we get last char only
    prevs = find_permutations(in_str[1:])
    nexts = []

    # For each previous permutation found
    for i in xrange(len(prevs)):
        prev = prevs[i]
        # Put first char of passed in str in each location of prev perm
        for j in xrange(len(in_str)):
            new_str = prev[:j] + in_str[0] + prev[j:]
            # If we haven't already seen it, add it to next perms out list
            if new_str not in nexts:
                nexts.append(new_str)

    # Return next level permutations
    return nexts


def find_valid_parentheses(in_str):
    '''
    Find if the input has a valid sequence of parentheses

    :param in_str:
    :return:
    '''

    pctr = 0
    for char in in_str:
        if char == '(':
            pctr += 1
        if char == ')':
            if pctr == 0:
                return False
            else:
                pctr -= 1
    if pctr != 0:
        return False
    else:
        return True


