# returns the sum of a list of numbers
def sum_of_list(numbers):
    return sum(numbers)

# returns the product of a list of numbers
def product_of_list(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

def reverse_list(numbers):
    return numbers[::-1]

def main():
    # take in user input
    user_input = input("Enter a list of numbers separated by spaces: ")
    numbers = [int(num) for num in user_input.split()]

    # store the sum and product of the list provided by the user
    sum_result = sum_of_list(numbers)
    product_result = product_of_list(numbers)
    reverse_result = reverse_list(numbers)

<<<<<<< HEAD
    print(f"Sum: {sum_result}, Product: {product_result}, Reverse: {reverse_result}")
=======
    # print the results 
    print(f"Sum: {sum_result}, Product: {product_result}")
>>>>>>> 5832fbd (added comments)

if __name__ == "__main__":
    main()

