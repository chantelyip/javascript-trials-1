"""Python functions for JavaScript Trials 1."""


def output_all_items(items):
    for item in items:
        print(item)
    

def get_all_evens(nums):

    even_nums = []

    for number in nums:
        if number % 2 == 0:
            even_nums.append(number)

    return even_nums

def get_odd_indices(items):

    odd_indices = []

    for index, item in enumerate(items):
        if index % 2 != 0:
            odd_indices.append(index)

    return odd_indices


def print_as_numbered_list(items):
    i = 1
    
    for item in items:
        print(f'#{i}:{item}')
        i += 1


def get_range(start, stop):
    
    nums = []
    for num in range(start, stop):
        nums.append(num)

    return nums


def censor_vowels(word):

    vowels = 'aeiou'
    
    for letter in word:
        if letter in vowels:
            print()


def snake_to_camel(string):
    pass  # TODO: replace this line with your code


def longest_word_length(words):
    pass  # TODO: replace this line with your code


def truncate(string):
    pass  # TODO: replace this line with your code


def has_balanced_parens(string):
    pass  # TODO: replace this line with your code


def compress(string):
    pass  # TODO: replace this line with your code
