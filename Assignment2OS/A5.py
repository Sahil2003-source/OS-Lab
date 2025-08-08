def lensort(strings):
    return sorted(strings, key=len)

def extsort(files):
    return sorted(files, key=lambda x: x.split('.')[-1] if '.' in x else '')
    
strings = ["banana", "fig", "apple", "kiwi"]
files = ["report.doc", "data.csv", "image.png", "archive.zip", "notes.txt"]

print(lensort(strings))
print(extsort(files))
