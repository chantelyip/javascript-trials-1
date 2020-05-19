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

    censored_word = []

    vowels = 'aeiou'
    
    for letter in word:
        if letter in vowels:
            censored_word.append('*')
        else: 
            censored_word.append(letter)

    return ''.join(censored_word)


def snake_to_camel(string):

    camel_list = []

    for word in string.split('_'):
        print(word)
        camel_list.extend([word.title()])

    return "".join(camel_list)

print(snake_to_camel('hello_world'))
    

def longest_word_length(words):
    pass  # TODO: replace this line with your code


def truncate(string):
    pass  # TODO: replace this line with your code


def has_balanced_parens(string):
    pass  # TODO: replace this line with your code


def compress(string):
    pass  # TODO: replace this line with your code
