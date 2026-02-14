
def find_number_of_even_numbers(numbers):
    """Find the total number of even numbers in the list 'numbers' and return 
    the number as an integer"""
    return [(numbers[n],numbers[n+1]) for n in range(len(numbers)-1) if (numbers[n] + numbers[n+1]) % 2 == 0]
    # result = []
    # for n in range(len(numbers)- 1):
    #     if (numbers[n] + numbers[n+1]) % 2 == 0:
    #         print(n+1)
    #         result.append((n,n+1))

    # return result
             

print(find_number_of_even_numbers([6, 2, 3, 5, 9, 4, 1, 11]))