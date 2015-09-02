""" Compute the factorial of a set of numbers stored in a file. """

def factorial(n):
    if n == 0:
        return 1
    else:
        return factorial(n-1) * n


def read_data(filename):
    numbers = []
    with open(filename, 'r') as f:
        for line in f:
            number = int(line)
            numbers.append(number)
    return numbers


def compute_factorials_for_list(numbers):
    factorials = []
    for number in numbers:
        result = factorial(number)
        factorials.append(result)
    return factorials
    

def main():
    numbers = read_data('numbers.txt')
    factorials = compute_factorials_for_list(numbers)


if __name__ == '__main__':
    main()
