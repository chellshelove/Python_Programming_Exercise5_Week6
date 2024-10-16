def search_common(list1, list2):
    # Find common values using set intersection and convert back to list
    common_values = list(set(list1) & set(list2))
    
    return common_values

# Example usage
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

result = search_common(list1, list2)
print("Common values:", result)