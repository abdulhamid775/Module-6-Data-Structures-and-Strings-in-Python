def demonstrate_list_slicing():
    # Create a list from 1 to 10
    numbers = list(range(1, 11))
    print("Original list:", numbers)

    # Extract the first five elements
    first_five = numbers[:5]
    print("Extracted first five elements:", first_five)

    # Reverse the extracted elements
    reversed_five = first_five[::-1]
    print("Reversed extracted elements:", reversed_five)

if __name__ == "__main__":
    demonstrate_list_slicing()
