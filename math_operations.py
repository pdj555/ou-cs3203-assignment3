def sum_of_list(numbers):
    return sum(numbers)

def product_of_list(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

def main():
    user_input = input("Enter a list of numbers separated by spaces: ")
    numbers = [int(num) for num in user_input.split()]

    sum_result = sum_of_list(numbers)
    product_result = product_of_list(numbers)

    print(f"Sum: {sum_result}, Product: {product_result}")

if __name__ == "__main__":
    main()

