def reverse_lines(filename):
    with open(filename, 'r') as file:
        for line in file:
            print(line.strip()[::-1])

reverse_lines("example.txt")
