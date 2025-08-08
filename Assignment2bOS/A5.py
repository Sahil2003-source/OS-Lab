numbers = [4, 7, 2, 4, 9, 7, 6, 2, 1, 3]

duplicates = []
seen = set()

for num in numbers:
    if num in seen and num not in duplicates:
        duplicates.append(num)
    seen.add(num)

print("Duplicate elements:", duplicates)
