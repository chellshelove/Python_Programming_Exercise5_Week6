def search_common0(list1, list2):
    # Find common values between the two lists using set intersection
    common_values = [value for value in list1 if value in list2]
    
    # Return the list of common values
    return common_values

# Example usage
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common_values = search_common0(list1, list2)
print("Common values:", common_values)