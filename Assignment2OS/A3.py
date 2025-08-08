def duplicate(nums):
    duplicates = []
    seen = set()
    for num in nums:
        if num in seen and num not in duplicates:
            duplicates.append(num)
        seen.add(num)
    return duplicates

numbers = [1, 2, 3, 4, 2, 5, 6, 3, 7, 8]
print("Duplicates:", duplicate(numbers))
