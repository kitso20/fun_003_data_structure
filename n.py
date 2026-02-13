
def find_number_of_even_numbers(numbers):
    """Find the total number of even numbers in the list 'numbers' and return 
    the number as an integer"""
    return len(list(n for n in numbers if n % 2 == 0))

print(find_number_of_even_numbers([1, 2, 3, 4, 5]))