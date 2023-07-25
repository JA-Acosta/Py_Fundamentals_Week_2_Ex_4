'''
>>> JAAR
>>> 07/24/2023
>>> Practicing Fundamentals Program 10
>>> Version 1
'''

'''
>>> Asks the user for a list of numbers then calculates the sum of all even numbers as well as determines which value is the largest.
'''

def verify_list()-> list :
    '''
    >>> Verifies if a user input is a list comprized solely of integer values then returns that list. Otherwise, will ask the user for another input.

    >>> Return: (list) int_list
    '''
    while True :
        try :
            int_list = list(map(int, input().split(', ')))
        except ValueError :
            print('Your input was invalid\n\tEnter a list of numbers: ', end = '')
        else :
            return int_list

def main() :
    print('Enter a list of numbers where each element is separated by a comma and a space: ', end = '')
    int_list = verify_list()
    print(f'Sum of Evens = {sum(filter(lambda x: x % 2 == 0, int_list))}')
    print(f'Max Value = {max(int_list)}')

if __name__ == '__main__' :
    main()