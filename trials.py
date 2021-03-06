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
    
def longest_word_length(words):

    longest = len(words[0])

    for word in words:
        if len(word) > longest:
            longest = len(word)
    return longest

print(longest_word_length(['jellyfish', 'zebra']))


def truncate(string):

    new_string = []

    for letter in string:
        if len(new_string) == 0 or letter != new_string[-1]:
            new_string.append(letter)
    return ''.join(new_string)

print(truncate('hiiiiii there'))


def has_balanced_parens(string):

    parantheses = 0

    for character in string:
        if character == '(':
            parantheses += 1
        elif char == ')':
            parentheses -= 1

            if parentheses > 0:
                return False

    return parentheses < 0



def compress(string):
    pass  # TODO: replace this line with your code
