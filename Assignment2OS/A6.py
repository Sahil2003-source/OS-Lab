file = open("example.txt", "w")
file.write("First line\nSecond line\nThird line\n")
file.close()

file = open("example.txt", "r")
content = file.read()
print("Read content:\n", content)
file.close()

file = open("example.txt", "r")
line = file.readline()
print("First line:", line.strip())
file.close()

file = open("example2.txt", "w")
file.writelines(["Line 1\n", "Line 2\n", "Line 3\n"])
file.close()

file = open("example2.txt", "r")
print("example2.txt content:\n", file.read())
file.close()
