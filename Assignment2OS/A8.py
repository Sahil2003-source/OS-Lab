def reverse_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    for line in reversed(lines):
        print(line.strip())

reverse_file("example.txt")
