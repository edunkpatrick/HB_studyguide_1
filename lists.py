"""List Practice
Edit the functions until all of the doctests pass when
you run this file.
"""


def print_list(items):
    """Print each item in the input list.
    
    For example::
    
        >>> print_list([1, 2, 6, 3, 9])
        1
        2
        6
        3
        9
    """

    for item in items:
        print(item)



def long_words(words):
    """Return words in input list that longer than 4 characters.
    
    For example::
    
        >>> long_words(["hello", "a", "b", "hi", "muffin", "muffin"])
        ['hello', 'muffin', 'muffin']
    
    (If there are duplicates, show both --- notice "muffin" appears
    twice in output)
    
    If no words are longer than 4 characters, return an empty list::
    
        >>> long_words(["all", "are", "tiny"])
        []
    """
    longer_than_4 = []
    for word in words:
        if len(word) > 4:
            longer_than_4.append(word)
    return longer_than_4


def n_long_words(words, n):
    """Return words in list longer than `n` characters.
    
    For example::
    
        >>> n_long_words(
        ...     ["hello", "hey", "spam", "spam", "muffin", "muffin"],
        ...     3
        ... )
        ['hello', 'spam', 'spam', 'muffin', 'muffin']
        >>> n_long_words(["I", "like", "apples", "bananas", "you"], 5)
        ['apples', 'bananas']
    """

    longer_than_n = []
    for word in words:
        if len(word) > n:
            longer_than_n.append(word)

    return longer_than_n

def smallest_int(numbers):
    """Find the smallest integer in a list of integers and return it.
    **DO NOT USE** the built-in function `min()`!
    
    For example::
    
        >>> smallest_int([-5, 2, -5, 7])
        -5
        >>> smallest_int([3, 7, 2, 8, 4])
        2
    
    If the input list is empty, return `None`::
    
        >>> smallest_int([]) is None
        True
    """
    
    # make list of sorted numbers
    sort_numbers = sorted(numbers)
    
    # check if list contains values
    if len(sort_numbers) > 0:
        # return smallest number if list contains values
        return sort_numbers[0]

    # return None if list is empty
    return


def largest_int(numbers):
    """Find the largest integer in a list of integers and return it.
    **DO NOT USE** the built-in function `max()`!
    
    For example::
    
        >>> largest_int([-5, 2, -5, 7])
        7
        >>> largest_int([3, 7, 2, 8, 4])
        8
    
    If the input list is empty, return None::
    
        >>> largest_int([]) is None
        True
    """
    # make list of sorted numbers
    sort_numbers = sorted(numbers)
    
    # check if list contains values
    if len(sort_numbers) > 0:
        # return largest number if list contains values
        return sort_numbers[-1]

    # return None if list is empty
    return


def halvesies(numbers):
    """Return list of numbers from input list, each divided by two.
    
    For example::
    
        >>> halvesies([2, 6, -2])
        [1.0, 3.0, -1.0]
   
    If any of the numbers are odd, make sure you don't round off
    the half::
   
        >>> halvesies([1, 5])
        [0.5, 2.5]
    """

        # make an empty list for divided numbers
    divided_by_2 = []

    # iterate through the input list
    for number in numbers:
        # convert input number to float
        number = float(number)
        # divide float by 2
        divided = number / 2
        # append divided_by_2 list
        divided_by_2.append(divided)

    return divided_by_2


def word_lengths(words):
    """Return the length of words in the input list.
    
    For example::
    
        >>> word_lengths(["hello", "hey", "hello", "spam"])
        [5, 3, 5, 4]
    """
    length_of_words = []

    for word in words:
        length_of_words.append(len(word))
    
    return length_of_words


def sum_numbers(numbers):
    """Return the sum of all of the numbers in the list.
    Python has a built-in function, `sum()`, which already does
    this --- but for this exercise, you should not use it.
    
    For example::
    
        >>> sum_numbers([1, 2, 3, 10])
        16
    
    Any empty list should return the sum of zero::
    
        >>> sum_numbers([])
        0
    """

    sum_of_nums = 0

    for number in numbers:
        sum_of_nums += number

    return sum_of_nums


def mult_numbers(numbers):
    """Return product (result of multiplication) of numbers in list.
    
    For example::
    
        >>> mult_numbers([1, 2, 3])
        6
    
    Obviously, if there is a zero in input, the product is zero::
    
        >>> mult_numbers([10, 20, 0, 50])
        0
    
    As explained at http://en.wikipedia.org/wiki/Empty_product,
    if the list is empty, the product should be 1::
    
        >>> mult_numbers([])
        1
    """
    # start at 1 bc anything multiplied by 0 will be 0
    product = 1
    
    for number in numbers:
        product *= number

    return product


def join_strings(words):
    """Return a string of all input strings joined together.
    Python has a built-in method, `list.join()` --- but for
    this exercise, **you should not use it**.
    
    For example::
    
        >>> join_strings(["spam", "spam", "muffin", "balloonicorn"])
        'spamspammuffinballoonicorn'
    
    For an empty list, you should return an empty string::
    
        >>> join_strings([])
        ''
    """

    joined_strings = ''

    for word in words:
        joined_strings += word

    return joined_strings


def average(numbers):
    """Return the average (mean) of the list of numbers given.
    
    For example::
    
        >>> average([2, 4])
        3.0
    
    This should handle cases where the result isn't an integer::
    
        >>> average([2, 12, 3])
        5.666666666666667
    
    There is no defined answer if the list given is empty;
    it's fine if this raises an error when given an empty list.
    (Think of the best way to handle an empty input list, though,
    a feel free to provide a good solution here.)
    """

    # start with getting the sum
    total = 0

    for number in numbers:
        total += number

    # to handle if list is empty:
    if len(numbers) > 0:
        # divide sum of list by length of list to get average
        average_of_numbers = total / len(numbers)
        return average_of_numbers
    # return None if list is empty
    else:
        return


def join_strings_with_comma(words):
    """Return ['list', 'of', 'words'] like "list, of, words".
    
    For example::
     
        >>> join_strings_with_comma(
        ...     ["Labrador", "Poodle", "French Bulldog"]
        ...     )
        'Labrador, Poodle, French Bulldog'
    
    If there's only one thing in the list, it should return just that
    thing, of course::
   
        >>> join_strings_with_comma(["Pretzel"])
        'Pretzel'
    """

    strings_list = ', '.join(words)

    return strings_list  


def reverse_list(items):
    """Return the input list, reversed.
    **Do not use** the python function `reversed()` or the method
    `list.reverse()`.
    
    For example::
    
        >>> reverse_list([1, 2, 3])
        [3, 2, 1]
        >>> reverse_list(["cookies", "love", "I"])
        ['I', 'love', 'cookies']
    
    You should do this without changing the original list::
    
        >>> orig = ["apple", "berry", "cherry"]
        >>> reverse_list(orig)
        ['cherry', 'berry', 'apple']
        >>> orig
        ['apple', 'berry', 'cherry']
    """

    reversed_items = items[-1::-1]

    return reversed_items


def reverse_list_in_place(items):
    """Reverse the input list `in place`.
    Reverse the input list given, but do it "in place" --- that is,
    do not create a new list and return it, but modify the original
    list.
    **Do not use** the python function `reversed()` or the method
    `list.reverse()`.
    
    For example::
    
        >>> orig = [1, 2, 3]
        >>> reverse_list_in_place(orig)
        >>> orig
        [3, 2, 1]
        >>> orig = ["cookies", "love", "I"]
        >>> reverse_list_in_place(orig)
        >>> orig
        ['I', 'love', 'cookies']
    """
    # loop that pops off last item at index i
    for i in range(len(items)):
        last_item = items.pop()
        # then inserts the last_item at index i
        items.insert(i, last_item)


def duplicates(items):
    """Return list of words from input list which were duplicates.
    Return a list of words which are duplicated in the input list.
    The returned list should be in ascending order.
   
    For example::
   
        >>> duplicates(
        ...     ["apple", "banana", "banana", "cherry", "apple"]
        ... )
        ['apple', 'banana']
        >>> duplicates([1, 2, 2, 4, 4, 4, 7])
        [2, 4]
   
    You should do this without changing the original list::
   
        >>> orig = ["apple", "apple", "berry"]
        >>> duplicates(orig)
        ['apple']
        >>> orig
        ['apple', 'apple', 'berry']
    """

    # create list of unique items
    unique_list = []
    duplicate_list = []

    # for loop to iterate through each item in list
    for item in items:
        # check if the item is in unique list
        if item not in unique_list:
            # append item to unique list if its not in list already
            unique_list.append(item)

        # if item in unique list, check if its in the duplicate list
        elif item not in duplicate_list:
            # append item to duplicate list if not in list already
            duplicate_list.append(item)

    # return sorted duplicate_list    
    return sorted(duplicate_list)


def find_letter_indices(words, letter):
    """Return list of indices where letter appears in each word.
    Given a list of words and a letter, return a list of integers
    that correspond to the index of the first occurrence of the letter
    in that word.
    **DO NOT** use the `list.index()` method.
    
    For example::
    
        >>> find_letter_indices(['odd', 'dog', 'who'], 'o')
        [0, 1, 2]
    
    ("o" is at index 0 in "odd", is at index 1 in "dog", and at
    index 2 in "who")
    
    If the letter doesn't occur in one of the words, use `None` for
    that word in the output list. For example::
    
        >>> find_letter_indices(['odd', 'dog', 'who', 'jumps'], 'o')
        [0, 1, 2, None]
    
    ("o" does not appear in "jumps", so the result for that input is
    `None`.)
    """

    # make a list for indices values to add to
    indices = []

    # iterate over each word in list
    for word in words:
        # iterate of each letter in word
        for i in word:
            # if the letter == argument letter, find index of letter
            if i == letter:
                letterindex = word.index(letter)
                # append index of letter to list of indices
                indices.append(letterindex)
        # if the letter is not in the word
        if letter not in word:
            # return "None"
            indices.append(None)
 
    return indices


#####################################################################
# END OF PRACTICE: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    result = doctest.testmod()
    if not result.failed:
        print("\nALL TESTS PASSED. GOOD WORK!\n")