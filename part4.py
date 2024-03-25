# Created with ChatGPT
# while the core functionality remains the same, 
# the revised version includes some best practices for Python coding, 
# such as avoiding the use of global variables, using more descriptive variable names, 
# and ensuring that the code is more robust and maintainable.

# Function to find the maximum of three numbers.
def max_num(a, b, c):
    return max([a, b, c])

# Function to multiply all the numbers in a list.
def mult_list(numbers):
    if not numbers:
        return 1
    product = numbers[0]
    for number in numbers[1:]:
        product *= number
    return product

# Function to reverse a string.
def rev_string(my_str):
    return my_str[::-1]

# Function to check whether a number falls in a given range.
def num_within(x, a, b):
    return x in range(a, b + 1)

# Function that prints out the first n rows of Pascal's triangle.
def pascal(num_rows):
    if num_rows < 1:
        print("Invalid number of rows")
        return
    triangle = [[1]]
    for row_number in range(1, num_rows):
        row = [1]
        row_prev = triangle[-1]
        for i in range(1, len(row_prev)):
            row.append(row_prev[i - 1] + row_prev[i])
        row.append(1)
        triangle.append(row)
    for row in triangle:
        print(row)

# Test cases
if __name__ == '__main__':
    print(max_num(1, 2, 3))
    print(max_num(100, 50, 1))
    print(max_num(15, 30, 2))

    print(mult_list([1, 11, 111]))
    print(mult_list([]))
    print(mult_list([23]))

    print(rev_string(""))
    print(rev_string("tacos"))
    print(rev_string("Mt Shasta"))

    print(num_within(3, 2, 4))
    print(num_within(42, 21, 42))
    print(num_within(11, 5, 111))

    pascal(3)
    pascal(7)
